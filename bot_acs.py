import logging
from settingsRun import *
from bot_caption import *

# Apresentação inicial
print("||==============================================================================================||\n")
print("||                                   Bem-vindo(a) ao ACSbot                                     ||\n")
print("||==============================================================================================||\n")

# Opções de inicialização
option = int(
    input("||         1 - Iniciar       2 - Iniciar configurando       3 - Configuração dos Clicks         ||\n>"))

if option == 1:
    # Executar o ACSbot com configurações padrão
    escolheRun(25, "Microsoft Edge", data_bool=False, data_visita="", tipo_visita="Ori")
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
else:
    # Opção inválida
    logging.error(f"Opção inválida: {option}. Encerrando aplicação...")
    print("Opção inválida. Encerrando aplicação...")
