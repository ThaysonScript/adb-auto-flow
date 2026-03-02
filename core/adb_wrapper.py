# Comandos puros do ADB transformados em funções Python


import subprocess
from config import cfg

class ADBDevice:
    def __init__(self):
        # Limpa qualquer espaço em branco acidental vindo do .env
        raw_id = cfg.DEVICE_ID if cfg.DEVICE_ID else ""
        self.device_id = raw_id.strip()
        
        # LOG DE DEPURAÇÃO: Isso ajudará a ver exatamente o que está sendo carregado
        if not self.device_id:
            print("[SISTEMA] Usando dispositivo padrão (nenhum ID detectado)")
            self.base_cmd = "adb"
        else:
            print(f"[SISTEMA] Usando dispositivo específico: '{self.device_id}'")
            self.base_cmd = f"adb -s {self.device_id}"

    def shell(self, command):
        full_cmd = f"{self.base_cmd} shell {command}"
        return subprocess.getoutput(full_cmd)

    def abrir_app(self, package_name):
        """Abre o app usando a Activity específica do Bing"""
        activity = "com.microsoft.sapphire.app.main.SapphireMainActivity"
        cmd = f"am start -n {package_name}/{activity}"
        return self.shell(cmd)

    def tap(self, x, y):
        self.shell(f"input tap {x} {y}")

    def swipe(self, x1, y1, x2, y2, duration):
        self.shell(f"input swipe {x1} {y1} {x2} {y2} {duration}")

    def key_event(self, code):
        self.shell(f"input keyevent {code}")