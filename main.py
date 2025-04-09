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
        main_logger.info("🌐 Tentando conectar ao simulador...")
        sm = SimConnect()
        aq = AircraftRequests(sm, _time=2000)
        main_logger.info("✅ Conexão estabelecida com sucesso!")
        print("✅ Conexão estabelecida com sucesso!")
        state_modifier()
        return sm, aq
    except Exception as e:
        main_logger.error(f"❌ Falha ao conectar ao simulador: {e}")
        print(f"❌ Falha ao conectar ao simulador: {e}")
        return None, None

def monitor_ground_altitude():
    sm = None
    aq = None
    state = "menu"
    last_logged_state = None

    main_logger.info("🔍 Monitorando estado do simulador...")
    print("🔍 Monitorando estado do simulador...")

    while not stop_event.is_set():
        if sm is None or aq is None:
            sm, aq = connect_to_simulator()
            if sm is None or aq is None:
                main_logger.warning("🔄 Tentando reconectar em 5 segundos...")
                print("🔄 Tentando reconectar em 5 segundos...")
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
                    main_logger.info("⏳ Loading detectado...")
                    print("⏳ Loading detectado...")
                    if state == "em voo":
                        state_modifier()
                    state = "loading"

            elif ground_altitude == 0:
                if state != "menu":
                    main_logger.info("🏠 Retornou ao menu principal.")
                    print("🏠 Retornou ao menu principal.")
                    state = "menu"

            elif ground_altitude > 0:
                if state != "em voo":
                    main_logger.info("🛫 Simulador ativo com cenário carregado.")
                    if title and "PMDG 737-800" in title:
                        main_logger.info("🚀 Voo com 737-800 iniciado!")
                        print("🚀 Voo com 737-800 iniciado!")
                    state = "em voo"

            if state != last_logged_state:
                main_logger.info(f"[STATE]: {state}")
                last_logged_state = state

            print(f"[STATE]: {state}")
            time.sleep(2)

        except Exception as e:
            main_logger.error(f"⚠️ Erro durante a comunicação com o simulador: {e}")
            print(f"⚠️ Erro durante a comunicação com o simulador: {e}")
            main_logger.warning("🔄 Reconectando ao simulador...")
            print("🔄 Reconectando ao simulador...")
            sm = None
            aq = None
            time.sleep(5)

def open_interface():
    window = tk.Tk()
    window.title("MSFS State Modifier")
    window.geometry("300x150")
    window.resizable(False, False)

    icon_path = os.path.join(os.path.dirname(sys.executable), "icon.ico") if getattr(sys, 'frozen', False) else "icon.ico"
    if os.path.exists(icon_path):
        window.iconbitmap(icon_path)

    tk.Label(window, text="Simulador monitorado!", font=("Arial", 12)).pack(pady=20)

    def randomize_now():
        state_modifier()
        messagebox.showinfo("State", "Modificação aleatória aplicada!")

    tk.Button(window, text="Randomizar agora", command=randomize_now).pack(pady=5)
    tk.Button(window, text="Sair", command=lambda: (stop_event.set(), icon.stop(), window.destroy())).pack(pady=5)

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
            MenuItem("Abrir", lambda _: threading.Thread(target=open_interface).start()),
            MenuItem("Sair", lambda _: (stop_event.set(), icon.stop()))
        )
    )

if __name__ == "__main__":
    threading.Thread(target=monitor_ground_altitude, daemon=True).start()
    icon = create_tray_icon()
    icon.run()
