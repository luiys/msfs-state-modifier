import os
import sys
import time
import threading
import logging
import tkinter as tk
from tkinter import messagebox
from SimConnect import SimConnect, AircraftRequests
from state_modifier import main as state_modifier
from pystray import Icon, MenuItem, Menu
from PIL import Image

# Diretório e arquivo de log para a main.py
log_dir = os.path.join(os.environ.get("LOCALAPPDATA"), "MSFSStateModifier")
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, "msfs-state-modifier.log")

# Logger exclusivo da main
main_logger = logging.getLogger("main_logger")
main_logger.setLevel(logging.INFO)

if not main_logger.handlers:
    handler = logging.FileHandler(log_file, encoding="utf-8")
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s", "%Y-%m-%d %H:%M:%S")
    handler.setFormatter(formatter)
    main_logger.addHandler(handler)

# Variável de controle de parada
stop_event = threading.Event()

def connect_to_simulator():
    try:
        main_logger.info("🌐 Trying to connect to the simulator...")
        sm = SimConnect()
        aq = AircraftRequests(sm, _time=2000)
        main_logger.info("✅ Connection established successfully!")
        print("✅ Connection established successfully!")
        state_modifier()
        return sm, aq
    except Exception as e:
        main_logger.error(f"❌ Failed to connect to the simulator: {e}")
        print(f"❌ Failed to connect to the simulator: {e}")
        return None, None

def monitor_ground_altitude():
    sm = None
    aq = None
    state = "menu"
    last_logged_state = None

    main_logger.info("🔍 Monitoring the simulator's state...")
    print("🔍 Monitoring the simulator's state...")

    while not stop_event.is_set():
        if sm is None or aq is None:
            sm, aq = connect_to_simulator()
            if sm is None or aq is None:
                main_logger.warning("🔄 Trying to reconnect in 5 seconds...")
                print("🔄 Trying to reconnect in 5 seconds...")
                time.sleep(5)
                continue

        try:
            ground_altitude = aq.get("GROUND_ALTITUDE")
            title = aq.get("TITLE")

            if isinstance(ground_altitude, bytes):
                ground_altitude = float(ground_altitude.decode('utf-8'))
            if isinstance(title, bytes):
                title = title.decode('utf-8')

            if ground_altitude is None:
                if state != "loading":
                    main_logger.info("⏳ Loading detected...")
                    print("⏳ Loading detected...")
                    if state == "flying":
                        state_modifier()
                    state = "loading"

            elif ground_altitude == 0:
                if state != "menu":
                    main_logger.info("🏠 Returned to the main menu.")
                    print("🏠 Returned to the main menu.")
                    state = "menu"

            elif ground_altitude > 0:
                if state != "flying":
                    main_logger.info("🛫 Simulator active with scenery loaded.")
                    if title and "PMDG 737-800" in title:
                        main_logger.info("🚀 Flight with 737-800 started!")
                        print("🚀 Flight with 737-800 started!")
                    state = "flying"

            if state != last_logged_state:
                main_logger.info(f"[STATE]: {state}")
                last_logged_state = state

            print(f"[STATE]: {state}")
            time.sleep(2)

        except Exception as e:
            main_logger.error(f"⚠️ Error during communication with the simulator: {e}")
            print(f"⚠️ Error during communication with the simulator: {e}")
            main_logger.warning("🔄 Reconnecting to the simulator...")
            print("🔄 Reconnecting to the simulator...")
            sm = None
            aq = None
            time.sleep(5)

def open_interface():
    import json
    from tkinter import ttk

    window = tk.Tk()
    window.title("MSFS State Modifier")
    window.geometry("300x220")
    window.resizable(False, False)

    icon_path = os.path.join(os.path.dirname(sys.executable), "icon.ico") if getattr(sys, 'frozen', False) else "icon.ico"
    if os.path.exists(icon_path):
        window.iconbitmap(icon_path)

    # Caminho do config na AppData
    config_path = os.path.join(os.environ.get("LOCALAPPDATA"), "MSFSStateModifier", "config.json")

    # Carrega perfis e perfil atual
    with open(config_path, "r", encoding="utf-8") as file:
        config_data = json.load(file)

    profiles = list(config_data.get("probability_profiles", {}).keys())
    current_profile = config_data.get("selected_profile", profiles[0] if profiles else "")

    tk.Label(window, text="Simulator being monitored!", font=("Arial", 12)).pack(pady=10)

    # Dropdown de perfis
    tk.Label(window, text="Realism level:", font=("Arial", 10)).pack()
    profile_var = tk.StringVar(value=current_profile.capitalize())
    dropdown = ttk.Combobox(window, textvariable=profile_var, values=[p.capitalize() for p in profiles], state="readonly")
    dropdown.pack(pady=5)

    def save_profile_selection(event=None):
        selected = dropdown.get().lower()
        config_data["selected_profile"] = selected
        with open(config_path, "w", encoding="utf-8") as file:
            json.dump(config_data, file, indent=2)
        main_logger.info(f"Perfil alterado para: {selected}")

    dropdown.bind("<<ComboboxSelected>>", save_profile_selection)

    def randomize_now():
        save_profile_selection()  # garante que o perfil selecionado foi salvo antes de randomizar
        state_modifier()
        messagebox.showinfo("State", "Random modification applied!")

    tk.Button(window, text="Randomize now", command=randomize_now).pack(pady=5)
    tk.Button(window, text="Exit", command=lambda: (stop_event.set(), icon.stop(), window.destroy())).pack(pady=5)

    window.mainloop()


def create_tray_icon():
    try:
        icon_path = os.path.join(os.path.dirname(sys.executable), "icon.ico") if getattr(sys, 'frozen', False) else "icon.ico"
        image = Image.open(icon_path)
    except:
        image = Image.new("RGB", (64, 64), color="black")

    return Icon(
        "MSFS Modifier",
        image,
        "MSFS State Modifier",
        menu=Menu(
            MenuItem("Open", lambda _: threading.Thread(target=open_interface).start()),
            MenuItem("Exit", lambda _: (stop_event.set(), icon.stop()))
        )
    )

if __name__ == "__main__":
    threading.Thread(target=monitor_ground_altitude, daemon=True).start()
    icon = create_tray_icon()
    icon.run()
