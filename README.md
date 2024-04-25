# Aplicação Streamlit: Top 100 Reviews de Livros da Amazon

Este é um aplicativo desenvolvido com o Streamlit que exibe informações sobre os top 100 livros vendidos na Amazon, além de fornecer detalhes específicos sobre cada livro e seus respectivos reviews.

## Estrutura de Diretórios

```
├── LICENSE
├── README.md
├── dataset
│   ├── Top-100 Trending Books.csv
│   └── customer reviews.csv
├── requirements.txt
└── src
    ├── app.py
    └── pages
        └── book_review.py
```

- **dataset**: Contém os arquivos CSV necessários para carregar os dados dos livros e seus reviews.
    - `Top-100 Trending Books.csv`: Contém informações sobre os top 100 livros da Amazon.
    - `customer reviews.csv`: Contém os reviews dos clientes sobre os livros.

- **src**: Contém o código-fonte da aplicação.
    - **app.py**: Arquivo principal da aplicação que define as páginas e a lógica por trás do aplicativo.
    - **pages**: Diretório que contém os scripts para cada página do aplicativo.
        - **book_review.py**: Define a página que exibe os detalhes específicos de um livro, incluindo título, preço, média de nota e reviews dos clientes.

- **requirements.txt**: Lista de dependências Python necessárias para executar o aplicativo.

## Como Iniciar a Aplicação

1. Certifique-se de ter o Python e o pip instalados no seu sistema.
2. Clone este repositório em seu ambiente local.
3. Navegue até o diretório raiz do projeto.
4. Instale as dependências usando o comando:
    ```
    pip install -r requirements.txt
    ```
5. Após a instalação das dependências, execute a aplicação com o seguinte comando:
    ```
    streamlit run src/app.py
    ```

## Funcionalidades

### Página Principal (App)

- Tabela de classificação dos top 100 livros da Amazon.
- Gráfico de contagem de livros por ano de publicação.
- Histograma de faixa de preço dos livros.
- Filtro de preço no menu lateral para filtrar os livros por faixa de preço.

### Página de Detalhes do Livro (Book Review)

- Permite filtrar os detalhes de um livro específico pelo nome.
- Exibe informações detalhadas do livro, incluindo título, preço, média de nota e ano de publicação.
- Lista os reviews dos clientes, exibindo a nota de cada um.

---

Este é um guia básico para executar e entender a aplicação. Se você tiver alguma dúvida ou problema, não hesite em entrar em contato. Aproveite a exploração dos top 100 livros da Amazon!
