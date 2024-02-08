import logging
from settingsRun import *

def menuPrincipal():
    # Apresentação inicial
    print("||==============================================================================================||\n")
    print("||                                   Bem-vindo(a) ao ACSbot version.6                           ||\n")
    print("||==============================================================================================||\n")

    # Opções de inicialização
    option = int(
        input("||         1 - Iniciar       2 - Iniciar configurando       3 - Configuração dos Clicks         ||\n>"))

    if option == 1:
        # Executar o ACSbot com configurações padrão
        escolheRun(tamanho_do_lote=25,
                   navegador=ler_config()['navegador']['navegador_padrao'],
                   data_bool=False, data_visita="",
                   tipo_visita="Orientacao")
        menuPrincipal()

    elif option == 2:
        # Configurar e executar o ACSbot                                            
        exibe_checkpoint()
        zera_checkpoint()

        # Configurações personalizadas
        tamanho_do_lote = tamanhoLote()
        navegador = escolher_navegador()
        tipo_visita = configurar_visitas()
        data_bool, data_visita = escolher_data_visita()

        # Iniciar o ACSbot com configurações personalizadas
        escolheRun(tamanho_do_lote, navegador, data_bool, data_visita, tipo_visita)
    elif option == 3:
        # Configuração dos cliques
        capturar_coordenadas()
        menuPrincipal()
    else:
        # Opção inválida
        logging.error(f"Opção inválida: {option}. Encerrando aplicação...")
        print("Opção inválida. Encerrando aplicação...")
menuPrincipal()