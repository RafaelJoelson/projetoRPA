# Projeto RPA

Este é meu primeiro projeto de RPA desenvolvido em Python. O projeto foi criado para atender às minhas necessidades em um sistema específico.

## Objetivo do Projeto

O projeto RPA visa automatizar tarefas específicas em um determinado sistema, proporcionando eficiência e economia de tempo.

## Tecnologias Utilizadas

- Python 3.10

## Estrutura do Projeto

- `projetoRPA/`: Diretório principal do projeto no GitHub.
    - `botACS/`: Diretório do projeto.
        - `build/`: Diretório da build gerada pelo PyInstaller.
        - `dist/`: Diretório do executável construído pelo PyInstaller.
        - `tabelaNomes/`: Diretório para armazenar data frames em *.csv.
            - `arquivo.csv`: Lista com nomes de pessoas.
        - `checkpoint.txt`: Contém o ponto de parada da lista de execução do DataFrame.
        - `coordenadas.txt`: Armazena as coordenadas dos cliques da automação.
        - `requirements.txt`: Contém as dependências do ambiente Python.
        - `bot_acs.ico`: Ícone do executável.
        - `bot_acs.py`: Arquivo principal do programa.
        - `settingsRun.py`: Arquivo com as funções do programa.

## Instalação

1. **Clone o repositório:**
    ```bash
    git clone https://github.com/RafaelJoelson/projetoRPA.git
    ```

2. **Navegue até o diretório do projeto:**
    ```bash
    cd projetoRPA
    ```

3. **Crie e ative um ambiente virtual:**
   - Utilizando Anaconda:
     ```bash
     conda create --name pythonProject python=3.10
     conda activate pythonProject
     ```
   - Utilizando venv:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```

4. **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

5. **Compile o executável:**
    ```bash
    pyinstaller --onefile --icon=bot_acs.ico bot_acs.py
    ```

6. **Configuração dos Clicks do Mouse:**
    - Siga as instruções.

7. **Inicie a Automação:**
    - Execute o executável gerado e escolha entre as opções 1 (Completa) ou 2 (Curta).
    - Para interromper a aplicação, arraste o mouse para o canto superior esquerdo da tela.

## Autor

Rafael Joelson
