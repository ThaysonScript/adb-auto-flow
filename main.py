from core.actions import UIActions
from core.adb_wrapper import ADBDevice
from core.humanizer import delay_humano
from core.screen_analyser import ScreenAnalyzer
from config import cfg

def main():
    device = ADBDevice()
    ui_actions = UIActions(device) 
    
    print(f"Abrindo o aplicativo: {cfg.APP_PACKAGE}")
    device.abrir_app(cfg.APP_PACKAGE)
    
    # 1. Espera o app carregar e tenta fechar a tela inicial (se ela aparecer)
    delay_humano(6, 10)
    id_intro = "com.microsoft.bing:id/sapphire_fre_bing_no_button"
    
    if ui_actions.clicar_por_id(id_intro):
        print("[FLUXO] Tela de intro fechada.")
        delay_humano(3, 5) # Espera a animação de transição para a Home
    else:
        print("[INFO] Tela de intro não detectada, seguindo para a Home.")

    # 2. Clicar no Perfil (ID extraído do seu view.xml)
    id_perfil = "com.microsoft.bing:id/sa_profile_button"
    print(f"[FLUXO] Tentando clicar no Perfil: {id_perfil}")
    
    if ui_actions.clicar_por_id(id_perfil):
        print("[SUCESSO] Perfil clicado!")
    else:
        print("[ERRO] Não foi possível encontrar o botão de perfil.")

if __name__ == "__main__":
    main()