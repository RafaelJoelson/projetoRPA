import pyautogui
import time
import pandas as pd

def escolher_navegador(navegador):
    navegador_padrão = "Microsoft Edge"
    option = input(f"Deseja alterar o navegador padrão ({navegador_padrão})?  S/N ").upper()
    if option == 'S':
        confirma = 'N'
        while confirma == 'N':
            navegador_escolhido = input("\nDigite o nome do Navegador: ")
            confirma = input(f"\nNavegador {navegador_escolhido} selecionado. Confirma S/N? ")
        return navegador_escolhido
    else:
        print("Navegador padrão mantido.")
        return navegador_padrão

def carregar_coordenadas():
    coordenadas = {}
    with open("coordenadas.txt", "r") as file:
        for line in file:
            key, values = line.strip().split(": ")
            x, y = map(int, values.split(", "))
            coordenadas[key] = (x, y)
    return coordenadas
def tamanhoLote():
    tamanho_do_lote = 25
    print(f"Tamanho padrão do lote: {tamanho_do_lote}")
    option = input("Deseja alterar? S/N: ").upper()
    if option == 'S':
        try:
            tamanho_do_lote = int(input("Digite o tamanho desejado do lote: "))
        except ValueError:
            print("Por favor, insira um valor numérico válido.")
            tamanho_do_lote = 0
        print(f"Lote definido para {tamanho_do_lote}")
        return tamanho_do_lote
    else:
        print(f"Lote definido para: {tamanho_do_lote}")
        return tamanho_do_lote
def carregaTabela(tb):
    tb = pd.read_csv("tabelaNomes/RelatorioControleVisitas.csv")
    return tb

def carregaCheckpoint():
    try:
        with open("checkpoint.txt", "r") as f:
            ultima_linha_processada = int(f.read().strip())
    except FileNotFoundError:
        ultima_linha_processada = 0
    return ultima_linha_processada

def salvaCheckpoint(ultima_linha_processada):
    with open("checkpoint.txt", "w") as f:
        f.write(str(ultima_linha_processada))
def runCompleta(lote, navegador):
    navegador = navegador
    coordenadas = carregar_coordenadas()
    tabela = pd.DataFrame()
    tabela = carregaTabela(tabela)
    ultima_linha_processada = carregaCheckpoint()
    #Tempo de espera entre os comandos
    #1-Tecla Windows
    pyautogui.press('win')
    time.sleep(0.8)
    #2-Acessar Navegador Edge
    pyautogui.write(navegador)
    time.sleep(0.8)
    pyautogui.press('enter')
    time.sleep(2)
    #3-Ir para o site do sistema
    pyautogui.write('https://sistemas.elosis.com.br/santacruz/login')
    time.sleep(2)
    pyautogui.press('enter')
    #4-Click do Login
    time.sleep(2)
    pyautogui.click(*coordenadas['click_1'])
    time.sleep(2)
    #5-Click módulo ACS
    pyautogui.click(*coordenadas['click_2'])
    time.sleep(2)
    #6-Confirmar seleção do módulo
    for i in range(3):
        pyautogui.press('tab')
    pyautogui.press('space')
    time.sleep(2)
    #7-Ir em fichas
    for i in range(8):
        pyautogui.press('tab')
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(2)
    #8-ir em visita domiciliar territorial
    pyautogui.press('tab')
    pyautogui.press('enter')
    runCurta(lote)

def runCurta(lote):
    coordenadas = carregar_coordenadas()
    tabela = pd.DataFrame()
    tabela = carregaTabela(tabela)
    ultima_linha_processada = carregaCheckpoint()
    #Realiza a automação de acordo com o tamanho do lote informado.
    for i in range(lote):
        # Verifica se ainda há linhas na tabela para processar
        if ultima_linha_processada >= len(tabela):
            print("Todas as linhas foram processadas.")
            break

        linha = tabela.index[ultima_linha_processada]
        time.sleep(3)
        # 9-Click novo cadastro
        pyautogui.click(*coordenadas['click_3'])
        time.sleep(3)
        # 10 - Clicar no  ACS
        pyautogui.click(*coordenadas['click_4'])
        time.sleep(0.5)
        for i in range(8):
            pyautogui.press('tab')
        time.sleep(0.8)
        pyautogui.press('space')
        time.sleep(0.8)
        # 12 - Nome do paciente
        nome_paciente = tabela.loc[linha, 'nomePaciente']
        pyautogui.write(nome_paciente)
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1.5)
        pyautogui.press('tab')
        time.sleep(1.5)
        pyautogui.press('space')
        time.sleep(1)
        # 11 - Clicar no boneco
        pyautogui.click(*coordenadas['click_5'])
        time.sleep(1)
        for i in range(11):
            pyautogui.press('tab')
        pyautogui.write("Ori")
        pyautogui.press('enter')
        for i in range(12):
            pyautogui.press('tab')
        pyautogui.press('enter')
        time.sleep(3)
        for i in range(2):
            pyautogui.press('tab')
        pyautogui.press('space')
        # Atualiza o checkpoint
        ultima_linha_processada += 1
        salvaCheckpoint(ultima_linha_processada)

    print(f"Pacientes Lançados: {min(lote, len(tabela) - ultima_linha_processada)}")

def escolheRun(tamanho_do_lote):
    option = int(input("Informe tipo de Execução:\n1 - Do Início\n2 - Nova Visita Domiciliar\n3 - SAIR\n"))
    if option == 1:
        print("ATENÇÃO! AFASTE-SE DOS CONTROLES Á MENOS QUE QUEIRA INTERROMPER O PROGRAMA")
        time.sleep(3)
        for i in range(5):
            print(f"O ACSbot iniciará em {i+1} segundos...")
            time.sleep(1)  # Aguarda por 5 segundos
        runCompleta(tamanho_do_lote)
    elif option ==2:
        print("ATENÇÃO! CERTIFIQUE-SE QUE PÁGINA ESTÁ ABERTA!")
        time.sleep(3)
        for i in range(5):
            print(f"O ACSbot iniciará em {i+1} segundos...")
            time.sleep(1)  # Aguarda por 5 segundos
        runCurta(tamanho_do_lote)
    else:
        print("Programa encerrado.")
        exit(0)