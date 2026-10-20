Dashboard de Criptomoedas
Aplicação desenvolvida em Python para consultar, armazenar e visualizar preços de criptomoedas utilizando a API da Coinbase, o banco de dados SQLite e o Streamlit.

Este projeto permite acompanhar os preços de Bitcoin (BTC), Ethereum (ETH) e Solana (SOL), armazenar o histórico das cotações e visualizar os dados em um dashboard interativo.

1. Funcionalidades
Consulta de preços de criptomoedas por meio da API da Coinbase.
Coleta de preços de BTC-USD, ETH-USD e SOL-USD.
Armazenamento dos dados em um banco SQLite.
Exibição do preço mais recente, maior preço e menor preço registrado.
Visualização do histórico de preços em gráficos.
Acesso ao dashboard pelo navegador.
Possibilidade de publicação online para acesso remoto.
2. Tecnologias utilizadas
Python 3.10 ou superior.
Streamlit.
Pandas.
Requests.
SQLite.
API da Coinbase.
Git e GitHub para versionamento e publicação.
3. Estrutura do projeto
Organize os arquivos da seguinte forma:


projeto_cripto/
├── coinbase.py
├── banco.py
├── coleta.py
├── dashboard.py
├── requirements.txt
├── README.md
└── coinbase5.db
Descrição dos arquivos:

coinbase.py: consulta os preços na API da Coinbase.
banco.py: cria a tabela e insere os preços no SQLite.
coleta.py: executa a coleta das cotações e salva os dados no banco.
dashboard.py: apresenta os indicadores e gráficos no Streamlit.
requirements.txt: lista as dependências do projeto.
README.md: contém as instruções de instalação e utilização.
coinbase5.db: banco de dados SQLite, criado automaticamente quando necessário.
O banco de dados pode não existir inicialmente. Nesse caso, ele será criado quando a coleta inicializar a tabela.

4. Pré-requisitos
Antes de começar, instale:

Python 3.10 ou superior.
pip, gerenciador de pacotes do Python.
Git, caso deseje clonar o repositório.
Conexão com a internet para consultar a API da Coinbase.
Para verificar as instalações, execute:


python --version
pip --version
git --version
O comando git --version é necessário somente se o Git estiver instalado e for utilizado.

5. Instalação local
5.1. Obter os arquivos do projeto
Se o projeto estiver em um repositório GitHub, clone-o:


git clone URL_DO_REPOSITORIO
Entre na pasta do projeto:


cd projeto_cripto
Substitua URL_DO_REPOSITORIO pelo endereço real do repositório.

Se os arquivos já estiverem no seu computador, abra o terminal diretamente na pasta do projeto.

5.2. Criar um ambiente virtual
O ambiente virtual ajuda a manter as dependências do projeto isoladas.

Windows:


python -m venv .venv
.venv\Scripts\activate
Linux ou macOS:


python3 -m venv .venv
source .venv/bin/activate
5.3. Instalar as dependências
Crie o arquivo requirements.txt com o seguinte conteúdo:


streamlit
pandas
requests
Com o ambiente virtual ativado, execute:


pip install -r requirements.txt
6. Executar a coleta de preços
A coleta é responsável por consultar as cotações e registrar os dados no banco SQLite.

Execute:


python coleta.py
O programa deverá:

Inicializar a tabela de preços, caso ela ainda não exista.
Consultar as criptomoedas configuradas.
Obter os preços retornados pela API.
Registrar os preços e as datas e horas no banco.
Exibir os resultados no terminal.
Cada execução bem-sucedida registra novas cotações. Para construir um histórico, execute a coleta periodicamente.

Se ocorrer um erro na consulta de uma moeda, verifique a mensagem exibida no terminal e confirme se a função consultar_preco() trata corretamente as falhas da API.

7. Executar o dashboard
Depois de executar a coleta inicial, inicie o Streamlit:


streamlit run dashboard.py
O terminal apresentará um endereço local, normalmente:

http://localhost:8501

Abra esse endereço no navegador.

Como utilizar o dashboard
Visualize os indicadores das criptomoedas disponíveis.
Consulte o maior e o menor preço registrado.
Escolha uma criptomoeda no menu de seleção.
Analise o histórico de preços no gráfico de linhas.
Os indicadores e gráficos dependem dos dados armazenados no banco.

O dashboard utiliza cache de dados com validade de 60 segundos. Isso significa que uma nova consulta ao banco poderá ocorrer após a expiração do cache, mas a coleta de novas cotações continua sendo uma tarefa separada.
