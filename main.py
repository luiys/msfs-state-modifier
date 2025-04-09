import os
import sys
import time
import logging
from SimConnect import SimConnect, AircraftRequests
from state_modifier import main as state_modifier

# Configurar o sistema de logs em pasta com permissão de escrita
log_dir = os.path.join(os.environ.get("LOCALAPPDATA"), "MSFSStateModifier")
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, "msfs-state-modifier.log")

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

def get_simconnect_dll_path():
    if getattr(sys, 'frozen', False):
        return os.path.join(sys._MEIPASS, "SimConnect", "SimConnect.dll")
    else:
        return "SimConnect.dll"

def connect_to_simulator():
    try:
        logging.info("🌐 Tentando conectar ao simulador...")
        sm = SimConnect()
        aq = AircraftRequests(sm, _time=2000)
        logging.info("✅ Conexão estabelecida com sucesso!")
        print("✅ Conexão estabelecida com sucesso!")
        state_modifier()
        return sm, aq
    except Exception as e:
        logging.error(f"❌ Falha ao conectar ao simulador: {e}")
        print(f"❌ Falha ao conectar ao simulador: {e}")
        return None, None

def monitor_ground_altitude():
    sm = None
    aq = None
    state = "menu"

    logging.info("🔍 Monitorando estado do simulador...")
    print("🔍 Monitorando estado do simulador...")

    while True:
        if sm is None or aq is None:
            sm, aq = connect_to_simulator()
            if sm is None or aq is None:
                logging.warning("🔄 Tentando reconectar em 5 segundos...")
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

            logging.info(f"[GROUND_ALTITUDE] {ground_altitude} | [TITLE] {title}")
            print(f"[GROUND_ALTITUDE] {ground_altitude} | [TITLE] {title}")

            if ground_altitude is None:
                if state != "loading":
                    logging.info("⏳ Loading detectado...")
                    print("⏳ Loading detectado...")
                    if state == "em voo":
                        state_modifier()
                    state = "loading"

            elif ground_altitude == 0:
                if state != "menu":
                    logging.info("🏠 Retornou ao menu principal.")
                    print("🏠 Retornou ao menu principal.")
                    state = "menu"

            elif ground_altitude > 0:
                if state != "em voo":
                    logging.info("🛫 Simulador ativo com cenário carregado.")
                    if title and "PMDG 737-800" in title:
                        logging.info("🚀 Voo com 737-800 iniciado!")
                        print("🚀 Voo com 737-800 iniciado!")
                    state = "em voo"

            time.sleep(2)
            logging.info(f"[STATE]: {state}")
            print(f"[STATE]: {state}")

        except Exception as e:
            logging.error(f"⚠️ Erro durante a comunicação com o simulador: {e}")
            print(f"⚠️ Erro durante a comunicação com o simulador: {e}")
            logging.warning("🔄 Reconectando ao simulador...")
            print("🔄 Reconectando ao simulador...")
            sm = None
            aq = None
            time.sleep(5)

if __name__ == "__main__":
    monitor_ground_altitude()
