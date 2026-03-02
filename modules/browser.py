# Browser automation module

import random

from core.humanizer import delay_humano, gerar_coordenada_viesada
from core.screen_analyser import ScreenAnalyzer

def executar_busca_complexa(device, termo):
    analyzer = ScreenAnalyzer(device)
    
    # 1. Abre o Bing
    device.open_url(f"https://www.bing.com/search?q={termo}")
    delay_humano(5, 8)

    # 2. Simula verificação de status (ex: procurar se carregou o logo do Bing)
    if analyzer.get_element_bounds("resource-id", "b_logo"):
        print("[INFO] Página carregada com sucesso.")
        
        # 3. Scroll aleatório
        for _ in range(random.randint(2, 4)):
            device.swipe(500, 1400, 480, 600, random.randint(500, 1000))
            delay_humano(2, 4)

        # 4. Tenta clicar em um resultado de notícia (exemplo de busca por texto)
        noticia = analyzer.get_element_bounds("text", "Notícias")
        if noticia:
            rx, ry = gerar_coordenada_viesada(*noticia)
            device.tap(rx, ry)
            print(f"[AÇÃO] Entrando em notícia em {rx, ry}")
            delay_humano(10, 20) # Simula leitura
            device.key_event(4) # Volta para a busca
    else:
        print("[ERRO] Falha ao validar carregamento da tela.")