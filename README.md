# 📚 Biblioteca de livros

Esta API implementada em Python com FastAPI extrai informações de livros do site [Books to Scrape](https://books.toscrape.com/), armazena os dados no arquivo "books.csv" e fornece rotas para consulta.


## 📦 Requisitos

- Python 3.8+
- pip


## 📄 Requirements.txt
- Todas as bibliotecas utilizadas no projeto estão informados nesse arquivo.


## 🔧 Instalação e configuração
#### 1. Clone o repositório ou copie os arquivos.
#### 2. Crie um ambiente virtual e ative.

- python -m venv venv
- source venv/bin/activate  # Linux/macOS
- venv\Scripts\activate     # Windows

#### 3. Instalação de dependências, bibliotecas utilizadas no projeto.
- pip install -r requirements.txt


## 🔧 Inicie o servidor
- uvicorn main:app --reload


## 🗂️ Estrutura do Projeto

```
biblioteca/
├── app/
│   ├── main.py
│   ├── scraper.py
│   ├── models.py
│   └── utils.py
├── data/
│   └── books.csv
├── requirements.txt
└── README.md
```


## 🧠 scraper.py: Extração dos livros
- Realiza a extração de dados (web scraping) do site "https://books.toscrape.com/". Coleta informações sobre os livros disponíveis na página, como título, preço, disponibilidade, avaliação, categoria, URL da imagem e detalhes específicos de cada livro. Verifica uma ou mais páginas do site (dependendo do parâmetro pages), extrai os dados de cada livro listado, acessa a página de detalhes de cada um para obter informações adicionais, e então salva tudo em um arquivo CSV chamado "books.csv". Faz a coleta e organização das informações de livros de forma automatizada.


## 📦 models.py Modelos da API
- Modelo com a definição dos campos, atributos do livro que serão extraidos do site [Books to Scrape](https://books.toscrape.com/).


## 🛠 utils.py: Funções auxiliares
- Os métodos do arquivo utils.py são funções auxiliares que ajudam a manipular e consultar uma base de dados de livros armazenada em um arquivo CSV.

#### 1. load_books(): 
- Carrega todos os livros do arquivo CSV e retorna um DataFrame do pandas com esses dados.

#### 2. get_book_by_id(book_id): 
- Busca um livro específico pelo seu ID. Se encontrar, retorna um dicionário com as informações desse livro; se não, retorna None.

#### 3. search_books(title=None, category=None): 
- Permite procurar livros pelo título ou pela categoria. Você pode usar um ou ambos os filtros. Ele retorna uma lista de dicionários com os livros que correspondem aos critérios.

#### 4. get_categories(): 
- Lista todas as categorias de livros disponíveis, sem repetições, em ordem alfabética.



## 🚀 main.py: Rotas da API
- Os métodos do arquivo main.py são responsáveis por criar e gerenciar a API da sua biblioteca.

📁 Extrair Dados
#### /api/v1/extrair/{pages}
- Esse método extrai e salva livros de acordo com o número de páginas informado. Você pode solicitar entre 1 a 5 páginas ou exatamente 50 páginas para extrair todos os dados. Ele chama uma função que faz a extração, carrega os livros e retorna a quantidade de livros extraídos.


✅ Health Check
#### /api/v1/health
- Essa rota verifica se a API está funcionando bem. Ela tenta carregar os livros e retorna um status "ok" junto com a quantidade de livros disponíveis. É como um teste de saúde do sistema.


📚 Listar Todos os Livros
#### /api/v/books
- Aqui você consegue listar todos os livros disponíveis na sua biblioteca. Ela retorna uma lista com os detalhes de cada livro.


🔍 Buscar Livro por ID
#### /api/v1/books/{id}
- Essa rota busca um livro específico pelo seu ID. Se encontrar, retorna os detalhes do livro; se não, informa que o livro não foi encontrado.


🔎 Buscar por Título e/ou Categoria
#### /api/v1/books/search
- Essa busca permite procurar livros pelo título ou pela categoria. Você pode passar um ou ambos os parâmetros para filtrar os resultados.


📂 Listar Categorias
#### /api/v1/categories
- Essa rota retorna todas as categorias de livros disponíveis na sua biblioteca.

## ✅ Para executar as funcionalidades disponiveis
- http://127.0.0.1:8000/docs

