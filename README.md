# Laboratório 01 - Análise de Repositórios GitHub

Este projeto tem como objetivo coletar e analisar características de repositórios populares no GitHub, conforme as diretrizes do Laboratório 01 da disciplina de Experimentação de Software.

## Sprint 1: Coleta de 100 Repositórios via GraphQL

Nesta sprint, o foco é a coleta inicial de dados de 100 repositórios utilizando a API GraphQL do GitHub, sem o uso de bibliotecas de terceiros para a API.

### 1. Preparação do Ambiente Python

Para começar, você precisará configurar um ambiente virtual Python e instalar as dependências necessárias. Siga os passos abaixo:

1.  **Navegue até o diretório do projeto:**
    ```bash
    cd /home/ubuntu/lab01_github_analysis
    ```

2.  **Crie um ambiente virtual:**
    ```bash
    python3 -m venv .venv
    ```

3.  **Ative o ambiente virtual:**
    ```bash
    source .venv/bin/activate
    ```

4.  **Instale as dependências:**
    ```bash
    pip3 install requests
    ```

### 2. Geração do Token de Acesso GitHub

Para acessar a API do GitHub, você precisará de um Personal Access Token (PAT). Siga as instruções no material de apoio ou acesse [https://github.com/settings/tokens](https://github.com/settings/tokens) para gerar um token com as permissões necessárias (pelo menos `public_repo`).

**Importante:** Mantenha seu token seguro e nunca o exponha em seu código-fonte diretamente. Usaremos variáveis de ambiente ou um arquivo de configuração separado para isso.

### Próximos Passos

Nos próximos passos, iremos:

-   Elaborar a query GraphQL para coletar os dados necessários.
-   Desenvolver o script Python para executar a query e processar os dados.
-   Fornecer instruções detalhadas para a execução do script.

### 3. Execução do Script de Coleta de Dados

1.  **Defina seu Personal Access Token (PAT) como uma variável de ambiente:**
    ```bash
    export GITHUB_TOKEN="SEU_TOKEN_AQUI"
    ```
    Substitua `SEU_TOKEN_AQUI` pelo seu token gerado no GitHub. Para sessões futuras, você pode adicionar esta linha ao seu `~/.bashrc` ou `~/.zshrc`.

2.  **Execute o script Python para coletar os dados:**
    ```bash
    python3 src/collect_data.py
    ```

O script irá coletar os dados dos 100 repositórios mais populares (com mais de 1000 estrelas) e salvará as informações no arquivo `data/repositories.csv`.

### Estrutura do Projeto

```
lab01_github_analysis/
├── README.md
├── src/
│   ├── collect_data.py
│   └── query.graphql
└── data/
    └── repositories.csv (será gerado após a execução do script)
```
