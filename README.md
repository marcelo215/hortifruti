Painel Multimodal para Hortifruti - Checkpoint 3

Curso: Engenharia de Software

Disciplina: IA & ML

Professor: Wellington Cidade Silva

Turma: 3ESPA

Sobre o Projeto

Este projeto consiste em um Painel Multimodal para Hortifruti, desenvolvido como parte da avaliação do Checkpoint 3. A aplicação web interativa integra tecnologias de desenvolvimento front-end com processamento e computação científica em Python diretamente no navegador via PyScript.

O painel realiza tarefas como:

Exibição dinâmica da base de dados de produtos (dados.json).

Cálculo vetorial de embeddings (Norma Euclidiana utilizando a biblioteca numpy).

Validação de guardrails e controle de telemetria da aplicação.

Estrutura do Repositório

O projeto segue estritamente a arquitetura de pastas padronizada:

hortifruti/
├── index.html              # Página principal e integração do PyScript
├── integrantes.txt         # Arquivo de identificação (Nome, RM e Repositório)
├── README.md               # Documentação do projeto
├── .gitignore              # Configurações de arquivos ignorados pelo Git
└── src/
    ├── assets/             # Imagens e ícones dos produtos (SVGs)
    │   ├── banana.svg
    │   ├── laranja.svg
    │   ├── maca.svg
    │   └── uva.svg
    ├── css/
    │   └── estilo.css      # Estilização com variáveis, grid e responsividade
    └── python/
        ├── dados.json      # Base de dados estruturada das frutas
        └── main.py         # Lógica Python (Telemetria, Guardrails e Numpy)


Tecnologias Utilizadas

HTML5: Estrutura semântica do painel multimodal.

CSS3: Layout moderno com Grid/Flexbox, variáveis e estilização responsiva.

JSON: Armazenamento e manipulação dos dados dos produtos.

Python 3: Processamento lógico e cálculos de IA/ML.

PyScript: Execução de scripts Python diretamente no navegador.

NumPy: Biblioteca para operações matemáticas e cálculo vetorial de norma euclidiana.

Como Executar o Projeto

Como o projeto utiliza PyScript para carregar arquivos Python externos e JSON, é necessário rodá-lo através de um servidor HTTP local para evitar bloqueios de segurança do navegador (CORS).

Opção 1: VS Code - Extension Live Server (Recomendado)

Abra a pasta do projeto no VS Code.

Certifique-se de ter a extensão Live Server instalada.

Abra o arquivo index.html.

Clique no botão "Go Live" no canto inferior direito da barra de status.

O projeto abrirá automaticamente no endereço http://127.0.0.1:5500/.

Opção 2: Servidor HTTP do Python

Abra o terminal na raiz do projeto.

Execute o comando:

python -m http.server 8000


Acesse no navegador: http://localhost:8000/index.html

Fluxo de Trabalho e Versionamento Git

O desenvolvimento seguiu as boas práticas do Git Flow e uso de commits semânticos:

Branches: main, dev, e feature branches (feat/html, feat/css, feat/python, feat/json).

Commits: Histórico organizado utilizando padronização semântica (feat:, fix:, docs:, etc.).

Pull Requests: Alterações integradas à branch dev e posteriormente validadas para a branch main.

Integrantes

Informações de identificação localizadas no arquivo integrantes.txt na raiz do repositório:

Nome: [Marcelo Affonso Fonseca]

RM: [559790]

Repositório: [https://github.com/marcelo215/hortifruti/edit/main]
