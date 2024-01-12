import logging
from speedRun import *
from bot_caption import *
print("||==============================================================================================||\n")
print("||                                   Bem-vindo(a) ao ACSbot                                     ||\n")
print("||==============================================================================================||\n")
option = int(input("||         1 - Iniciar       2 - Iniciar configurando       3 - Configuração dos Clicks         ||\n>"))

if option == 1:
    escolheRun(25, "Microsoft Edge")
elif option == 2:
    exibe_checkpoint()
    zera_checkpoint()
    tamanho_do_lote = tamanhoLote()
    navegador = escolher_navegador()
    escolheRun(tamanho_do_lote, navegador)
elif option == 3:
    # Chamando a função para iniciar a captura
    capturar_coordenadas()
else:
    logging.error(f"Opção inválida: {option}. Encerrando aplicação...")
    print("Opção inválida. Encerrando aplicação...")
