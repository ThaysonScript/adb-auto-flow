# adb-auto-flow/core/actions.py
from core.humanizer import gerar_coordenada_viesada, delay_humano
from core.screen_analyser import ScreenAnalyzer

class UIActions:
    def __init__(self, device):
        self.device = device
        self.analyzer = ScreenAnalyzer(device)
        
    def clicar_ate_sumir(self, resource_id, max_tentativas=3):
        """Clica no botão e verifica se ele realmente saiu do XML"""
        for i in range(max_tentativas):
            bounds = self.analyzer.get_element_bounds("resource-id", resource_id)
            if not bounds:
                return True # Botão sumiu, podemos seguir
            
            x, y = gerar_coordenada_viesada(bounds[0], bounds[1], bounds[2], bounds[3])
            print(f"[UI] Tentativa {i+1}: Clicando em {resource_id}...")
            self.device.tap(x, y)
            delay_humano(3, 5) # Dá tempo ao app de processar o clique
        return False

    def clicar_por_texto(self, texto, delay_pos=True):
        """Procura um elemento pelo texto e clica de forma humana"""
        bounds = self.analyzer.get_element_bounds("text", texto)
        return self._executar_clique(bounds, f"Texto: {texto}", delay_pos)

    def clicar_por_id(self, resource_id, delay_pos=True):
        """Procura um elemento pelo ID e clica de forma humana"""
        bounds = self.analyzer.get_element_bounds("resource-id", resource_id)
        return self._executar_clique(bounds, f"ID: {resource_id}", delay_pos)

    def _executar_clique(self, bounds, log_info, delay_pos):
        """Lógica interna para processar o clique e humanização"""
        if bounds:
            # Gera coordenadas aleatórias dentro da área do botão
            x, y = gerar_coordenada_viesada(bounds[0], bounds[1], bounds[2], bounds[3])
            print(f"[UI] Clicando em {log_info} nas coordenadas ({x}, {y})")
            self.device.tap(x, y)
            
            if delay_pos:
                delay_humano(2, 4) # Pausa natural após clicar
            return True
        
        print(f"[AVISO] Elemento não encontrado: {log_info}")
        return False
    
    
    def esperar_e_clicar(self, resource_id, tentativas=5):
        """
        Fica atualizando o XML até que o elemento apareça ou as tentativas acabem.
        Isso garante que você pegue o XML 'próximo' assim que a tela mudar.
        """
        for i in range(tentativas):
            print(f"[UI] Tentativa {i+1}: Aguardando elemento {resource_id}...")
            # get_element_bounds sempre gera um dump NOVO ao ser chamado
            bounds = self.analyzer.get_element_bounds("resource-id", resource_id)
            
            if bounds:
                x, y = gerar_coordenada_viesada(bounds[0], bounds[1], bounds[2], bounds[3])
                self.device.tap(x, y) #
                delay_humano(2, 4) #
                return True
            
            delay_humano(1, 2) # Espera um pouco antes de tentar o próximo dump
        
        print(f"[ERRO] Elemento {resource_id} não apareceu após {tentativas} tentativas.")
        return False