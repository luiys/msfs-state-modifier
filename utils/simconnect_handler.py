from SimConnect import SimConnect, AircraftRequests
import time

class SimConnectHandler:
    def __init__(self, retry_interval=2):
        self.retry_interval = retry_interval
        self.sm = None
        self.aq = None
        self._connect()

    def _connect(self):
        while True:
            try:
                self.sm = SimConnect()
                self.aq = AircraftRequests(self.sm, _time=2000)
                print("✅ Conectado ao simulador via SimConnect.")
                break
            except Exception as e:
                print(f"⛔ SimConnect não disponível. Tentando novamente em {self.retry_interval}s...")
                time.sleep(self.retry_interval)

    def get_variable(self, var_name):
        try:
            value = self.aq.get(var_name)
            return value
        except Exception as e:
            print(f"⚠️ Erro ao obter variável '{var_name}': {e}")
            return None
