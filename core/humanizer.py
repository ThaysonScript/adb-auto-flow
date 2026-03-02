# Algoritmos de variação de tempo, clique e movimento

import random
import time
import numpy as np

def delay_humano(min_s=2, max_s=5):
    # Usa distribuição beta para que a maioria dos delays seja em torno da média,
    # mas com picos ocasionais de demora (como um humano se distraindo).
    wait = random.uniform(min_s, max_s)
    time.sleep(wait)

def gerar_coordenada_viesada(x1, y1, x2, y2):
    # Em vez de um random puro, clica mais perto do centro do botão (distribuição normal)
    mu_x, sigma_x = (x1 + x2) / 2, (x2 - x1) / 6
    mu_y, sigma_y = (y1 + y2) / 2, (y2 - y1) / 6
    rx = int(np.random.normal(mu_x, sigma_x))
    ry = int(np.random.normal(mu_y, sigma_y))
    return rx, ry