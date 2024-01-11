#bot_lançador de produção
from speedRun import *
from bot_caption import *
print("||===========================================||\n")
print("||       Bem-vindo(a) ao ACSbot              ||\n")
print("||===========================================||\n")
option = int(input("||   1 - Iniciar       2 - Configuração      ||\n"))
if option == 1:
    tamanho_do_lote = tamanhoLote()
    escolheRun(tamanho_do_lote)
elif option == 2:
    # Chamando a função para iniciar a captura
    capturar_coordenadas()
else:
    print("Opção inválida. Encerrando aplicação...")