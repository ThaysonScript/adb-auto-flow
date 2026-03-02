# adb-auto-flow/core/screen_analyser.py
import xml.etree.ElementTree as ET
import re
import subprocess
import os # Necessário para apagar o ficheiro local

class ScreenAnalyzer:
    def __init__(self, device):
        self.device = device

    def get_element_bounds(self, search_attr, search_value):
        # 1. Garante que não existe lixo local de execuções anteriores
        if os.path.exists("view.xml"):
            os.remove("view.xml")
        
        # 2. Limpa e gera o dump no telemóvel
        self.device.shell("rm /sdcard/view.xml")
        self.device.shell("uiautomator dump /sdcard/view.xml")
        
        # 3. Pull com verificação real de transferência
        result = subprocess.run(["adb", "pull", "/sdcard/view.xml", "view.xml"], capture_output=True)
        
        # Se o ficheiro não existe localmente após o pull, o dump falhou no Android
        if not os.path.exists("view.xml"):
            print("[ERRO] Falha crítica: O XML não foi atualizado. Verifique se o telemóvel está ocupado.")
            return None
        
        try:
            tree = ET.parse("view.xml")
            root = tree.getroot()
            for node in root.iter('node'):
                val = node.attrib.get(search_attr, '')
                if search_value.lower() in val.lower():
                    bounds = node.attrib.get('bounds') # Ex: [48,2144][1392,2216]
                    return list(map(int, re.findall(r'\d+', bounds)))
        except Exception as e:
            print(f"[ERRO] Erro ao processar o novo XML: {e}")
            return None
        return None