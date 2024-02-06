import pyautogui
import time
import pandas as pd
import platform
from datetime import datetime

def escolher_navegador():
    navegadores_suportados = {
        '1': "Microsoft Edge",
        '2': "Google Chrome"
    }

    navegador_padrao = "Microsoft Edge"
    option = input(f"Alterar o navegador padrão({navegador_padrao})? (S/N): ").upper()

    if option == 'S':
        while True:
            print("Escolha um navegador:")
            print("1 - Microsoft Edge")
            print("2 - Google Chrome")

            escolha = input("Digite o número do navegador desejado: ")

            if escolha in navegadores_suportados:
                navegador_escolhido = navegadores_suportados[escolha]
                confirma = input(f"\nNavegador {navegador_escolhido} selecionado. Confirma? (S/N): ").upper()

                if confirma == 'S':
                    return navegador_escolhido
                else:
                    print("Escolha de navegador cancelada. Mantendo o navegador padrão.")
                    return navegador_padrao
            else:
                print("Escolha inválida. Por favor, escolha um navegador suportado.")
    else:
        print("Navegador padrão mantido.")
        return navegador_padrao
def configurar_visitas():
    visitas_suportadas = {
        '1': "Ori",
        '2': "Ação edu",
        '3': "Conv"
    }

    visita_padrao = "Ori"
    option = input(f"Alterar a visita padrão({visita_padrao})? (S/N): ").upper()

    if option == 'S':
        while True:
            print("Escolha o tipo de visita:")
            print("1 - Orientação e Prevenção")
            print("2 - Ação educativa")
            print("3 - Convite atividades coletivas/Campanha de Saúde")

            escolha = input("Digite o número da visita desejada: ")

            if escolha in visitas_suportadas:
                visita_escolhida = visitas_suportadas[escolha]
                confirma = input(f"\nTipo de visita '{visita_escolhida}' selecionada. Confirma? (S/N): ").upper()

                if confirma == 'S':
                    return visita_escolhida
                else:
                    print("Escolha de navegador cancelada. Mantendo o navegador padrão.")
                    return visita_padrao
            else:
                print("Escolha inválida. Por favor, escolha uma visita suportada.")
    else:
        print("Visita padrão mantida.")
        return visita_padrao


def escolher_data_visita():
    data_bool = False
    data_padrao = ""
    option = input("Deseja alterar a data? (S/N): ").upper()

    if option == 'S':
        data_escolhida = input("Somente números! Ex:16082024 Informe a data: ")

        # Formatar a data fornecida para o formato "DD/MM/YYYY"
        try:
            data_obj = datetime.strptime(data_escolhida, "%d%m%Y")
            data_escolhida_formatada = data_obj.strftime("%d/%m/%Y")
        except ValueError:
            print("Formato de data inválido. Certifique-se de usar o formato correto (DDMMYYYY).")
            return False

        confirma = input(f"\nData da visita: '{data_escolhida_formatada}' selecionada. Confirma? (S/N): ").upper()

        if confirma == 'S':
            print("A data foi atualizada.")
            data_bool = True
            return data_bool, data_escolhida_formatada
        else:
            print("Escolha de data cancelada. Mantendo a data padrão.")
            data_bool = False
            return data_bool, data_padrao
    else:
        print("Data padrão mantida.")
        data_bool = False
        return data_bool, data_padrao


def carregar_coordenadas():
    coordenadas = {}
    with open("coordenadas.txt", "r") as file:
        for line in file:
            key, values = line.strip().split(": ")
            x, y = map(int, values.split(", "))
            coordenadas[key] = (x, y)
    return coordenadas

def capturar_coordenadas():
    print("Modo captura do cursor - Coordenadas resetadas\n")
    print("Escolha qual click você quer configurar\n")
    print("| 1 - Click do Login       |\n| 2 - Click Módulo ACS     |\n| 3 - Click Novo Cadastro  |\n| 4 - Click no ACS         |\n| 5 - Click no Buscar nome      |\n")
    coordenadas = {}
    for i in range(5):
        option = input("Pronto para configurar capturar o click: (S/N): ").upper()
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
    print("Coordenadas dos clicks salvas com sucesso!")  # Aguarda pressionar uma tecla
    time.sleep(5)


def tamanhoLote():
    tamanho_do_lote = 25
    print(f"Tamanho padrão do lote: {tamanho_do_lote}")
    option = input("Deseja alterar? (S/N): ").upper()
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
def exibe_checkpoint():
    ultima_linha_processada = carregaCheckpoint()
    print(f"Último Checkpoint: {ultima_linha_processada}")


def zera_checkpoint():
    confirmacao = input("Deseja zerar o checkpoint? (S/N): ").upper()

    if confirmacao == 'S':
        salvaCheckpoint(0)
        print("Checkpoint zerado.")
    else:
        print("Operação de zerar checkpoint cancelada.")

def runCompleta(lote, navegador,data_bool,data_visita,tipo_visita):
    pyautogui.sleep(0.5)
    navegador_aberto = navegador
    coordenadas = carregar_coordenadas()
    tabela = pd.DataFrame()
    tabela = carregaTabela(tabela)
    ultima_linha_processada = carregaCheckpoint()
    # Verifica qual SO está rodando.
    sistema_operacional = platform.system()
    # Se for Windows, pressiona a tecla Windows
    # Se for Ubuntu (Debian Based), pressiona Super+A
    if sistema_operacional == 'Windows':
        pyautogui.press('win')
        print(sistema_operacional)
    elif sistema_operacional == 'Linux':
        pyautogui.hotkey('win','a')
        print(sistema_operacional)
    else:
        print("Sistema operacional não suportado.")
    time.sleep(0.8)
    #2-Acessar Navegador
    pyautogui.write(navegador_aberto)
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
    time.sleep(3)
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
    runCurta(lote, data_bool, data_visita, tipo_visita)


def runCurta(lote, data_bool, data_visita, tipo_visita):
    # Carrega as coordenadas para automação
    coordenadas = carregar_coordenadas()

    # Inicializa um DataFrame vazio para armazenar os dados da tabela
    tabela = pd.DataFrame()

    # Carrega os dados da tabela
    tabela = carregaTabela(tabela)

    # Carrega o checkpoint da última linha processada
    ultima_linha_processada = carregaCheckpoint()

    # Realiza a automação de acordo com o tamanho do lote informado.
    for i in range(lote):
        # Verifica se ainda há linhas na tabela para processar
        if ultima_linha_processada >= len(tabela):
            print("Todas as linhas foram processadas.")
            break

        # Obtém a linha a ser processada
        linha = tabela.index[ultima_linha_processada]

        # Aguarda 3 segundos antes de prosseguir
        time.sleep(3)

        # 9 - Clica em novo cadastro
        pyautogui.click(*coordenadas['click_3'])
        time.sleep(3)

        # 10 - Clica no ACS
        pyautogui.click(*coordenadas['click_4'])
        time.sleep(0.5)

        # Verifica se há uma data personalizada
        if data_bool:
            # Move o foco para o campo de data
            for i in range(3):
                pyautogui.press('tab')

            # Insere a data personalizada
            pyautogui.write(data_visita)
            time.sleep(0.2)

            # Navega para os campos seguintes
            for i in range(5):
                pyautogui.press('tab')
        else:
            # Se não houver data personalizada, navega diretamente para os campos seguintes
            for i in range(8):
                pyautogui.press('tab')

        # Aguarda 0.8 segundos antes de pressionar a tecla 'espaço'
        time.sleep(0.8)
        pyautogui.press('space')
        time.sleep(0.8)

        # 12 - Insere o nome do paciente
        nome_paciente = tabela.loc[linha, 'nomePaciente']
        pyautogui.write(nome_paciente)
        time.sleep(1.5)
        pyautogui.press('enter')
        time.sleep(3)
        pyautogui.press('tab')
        time.sleep(1.5)
        pyautogui.press('space')
        time.sleep(1)
        # 11 - Clica em Buscar nome:
        pyautogui.click(*coordenadas['click_5'])
        time.sleep(1)

        # Navega pelos campos até chegar ao campo de tipo de visita
        for i in range(11):
            pyautogui.press('tab')

        # 12 - Insere o tipo de visita
        pyautogui.write(tipo_visita)
        pyautogui.press('enter')

        # Navega pelos campos seguintes
        for i in range(12):
            pyautogui.press('tab')
        pyautogui.press('enter')
        time.sleep(3)

        # Navega pelos últimos campos
        for i in range(2):
            pyautogui.press('tab')
        pyautogui.press('space')

        # Atualiza o checkpoint
        ultima_linha_processada += 1
        salvaCheckpoint(ultima_linha_processada)

    # Exibe a quantidade de pacientes lançados
    print(f"Pacientes Lançados: {min(lote, len(tabela) - ultima_linha_processada)}")


def escolheRun(tamanho_do_lote, navegador, data_bool, data_visita, tipo_visita):
    option = int(input("Informe tipo de Execução:\n||1 - Do Início      2 - Nova Visita      3 - SAIR     ||\n>"))
    if option == 1:
        print("ATENÇÃO! AFASTE-SE DOS CONTROLES Á MENOS QUE QUEIRA INTERROMPER O PROGRAMA")
        time.sleep(3)
        for i in range(5):
            print(f"O ACSbot iniciará em {i+1} segundos...")
            time.sleep(1)  # Aguarda por 5 segundos
        runCompleta(tamanho_do_lote, navegador,data_bool,data_visita,tipo_visita)
    elif option ==2:
        print("ATENÇÃO! CERTIFIQUE-SE QUE PÁGINA ESTÁ ABERTA!")
        time.sleep(3)
        for i in range(5):
            print(f"O ACSbot iniciará em {i+1} segundos...")
            time.sleep(1)  # Aguarda por 5 segundos
        runCurta(tamanho_do_lote, data_bool,data_visita, tipo_visita)
    else:
        print("Programa encerrado.")
        exit(0)