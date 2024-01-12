# projetoRPA

Este é meu primeiro projeto de RPA desenvolvido em python.
Projeto criado para atender minhas necessidades em um determinado sistema.
## Tecnologias Utilizadas

- Python 3.12

## Conteúdo

Explicação sobre os principais arquivos e diretórios no seu projeto.
- `projetoRPA/`: Diretório do Github.
	- `botACS/`: Diretório do projeto.
		- `tabelaNomes/`: Diretório para armazenar data frames em *.csv.
				- arquivo.csv : Lista com nomes de pessoas.
        - checkpoint.txt : Contém o ponto de parada da lista de execução do dataframe.
        - coordenadas.txt : Armazena as coordenadas dos clicks da automação.
        - requirements.txt : Contém as dependências do ambiente python.

## Instalação

1. Clone o repositório:

    ```bash
    git clone https://github.com/RafaelJoelson/projetoRPA.git
    ```

2. Navegue até o diretório do projeto:

    ```bash
    cd projetoRPA
    ```

3. Crie e ative um ambiente virtual com o Anaconda prompt (recomendado):

	```bash
    conda create --name pythonProject python=3.12
    conda activate pythonProject
    ```
    Ou então:
    
    ```bash
    python3 -m venv venv
    venv\Scripts\activate
    ```

4. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

5. Compile o executável:

    ```bash
    pyinstaller --onefile --icon=bot_acs.ico bot_acs.py

    ```

6. Configure os clicks do mouse conforme as imagens:

    tutorial.jpg

7. Inicie a automação selecionando uma das duas opções:

    1 - Completa, 2 - Curta

8. Para interromper a aplicação arraste completamente o mouse para o canto superior esquerdo da tela.

	

## Autor

Rafael Joelson