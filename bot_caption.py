#Auxiliar para captura do cursor do mouse
import pyautogui
import time

def limpar_coordenadas():
    with open("coordenadas.txt", "w") as file:
        file.truncate(0)


def capturar_coordenadas():
    option = 'S'
    limpar_coordenadas()
    print("Modo captura do cursor - Coordenadas resetadas\n")
    print("Escolha qual click você quer configurar\n")
    print(
        "| 1 - Click do Login       |\n| 2 - Click Módulo ACS     |\n| 3 - Click Novo Cadastro  |\n| 4 - Click no ACS         |\n| 5 - Click no Buscar nome      |\n")
    coordenadas = {}
    for i in range(5):
        option = input("Pronto para configurar capturar o click: S/N: ").upper()
        if option == 'S':
            print(f"Posicione o cursor para o clique {i + 1} e aguarde...")
            time.sleep(5)
            coordenadas[f'click_{i + 1}'] = pyautogui.position()
            print(f"Clique {i + 1} salvo com sucesso!")
        else:
            print("Operação abortada. Tente de novo")
            exit(0)

    # Salvando as coordenadas em um arquivo
    with open("coordenadas.txt", "w") as file:
        for key, value in coordenadas.items():
            file.write(f"{key}: {value[0]}, {value[1]}\n")
        # Aguarda até que o usuário pressione uma tecla antes de encerrar
        print("Coordenadas dos clicks salvas com sucesso! Pressione qualquer tecla para sair", end='', flush=True)
        msvcrt.getch()  # Aguarda pressionar uma tecla




