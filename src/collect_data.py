import requests
import os
import csv
import json

# Carrega o token de acesso pessoal do GitHub de uma variável de ambiente
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')

if not GITHUB_TOKEN:
    print("Erro: A variável de ambiente 'GITHUB_TOKEN' não está definida.")
    print("Por favor, defina-a com seu Personal Access Token do GitHub.")
    exit()

# URL da API GraphQL do GitHub
GRAPHQL_URL = 'https://api.github.com/graphql'

# Cabeçalhos para a requisição GraphQL
HEADERS = {
    'Authorization': f'Bearer {GITHUB_TOKEN}',
    'Content-Type': 'application/json'
}

def run_query(query, variables):
    """Executa uma query GraphQL e retorna a resposta JSON."""
    request = requests.post(GRAPHQL_URL, headers=HEADERS, json={'query': query, 'variables': variables})
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception(f"Query failed to run by returning code of {request.status_code}. {query}")

def get_repository_data(num_repos=1000):
    """Coleta dados de repositórios do GitHub usando a API GraphQL."""
    # Ajuste do caminho para ler o arquivo query.graphql
    query_path = os.path.join(os.path.dirname(__file__), 'query.graphql')
    with open(query_path, 'r') as f:
        query = f.read()

    all_repositories = []
    end_cursor = None
    has_next_page = True

    print(f"Iniciando a coleta de {num_repos} repositórios...")

    while len(all_repositories) < num_repos and has_next_page:
        variables = {
            "queryString": "stars:>1000 sort:stars-desc", # Critério de busca: repositórios com mais de 1000 estrelas, ordenados por estrelas (decrescente)
            "first": min(10, num_repos - len(all_repositories)), # Busca no máximo por vez (limite da API)
            "after": end_cursor
        }
        
        try:
            result = run_query(query, variables)
            if 'errors' in result:
                print(f"Erros na query: {result['errors']}")
                break

            search_data = result['data']['search']
            repositories = search_data['nodes']
            all_repositories.extend(repositories)

            page_info = search_data['pageInfo']
            end_cursor = page_info['endCursor']
            has_next_page = page_info['hasNextPage']
            print(f"Coletados {len(all_repositories)} repositórios até agora...")

        except Exception as e:
            print(f"Ocorreu um erro durante a coleta: {e}")
            break

    return all_repositories[:num_repos]

def save_to_csv(data, filename):
    """Salva os dados coletados em um arquivo CSV."""
    if not data:
        print("Nenhum dado para salvar.")
        return

    # Garante que o diretório de destino exista
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    # Define os nomes das colunas com base nas métricas solicitadas no enunciado
    fieldnames = [
        'name', 'owner_login', 'stargazerCount', 'forkCount', 'createdAt', 'updatedAt',
        'primaryLanguage', 'pullRequests_totalCount', 'releases_totalCount',
        'issues_closed_totalCount', 'issues_totalCount', 'diskUsage', 'defaultBranch_name',
        'defaultBranch_commit_history_totalCount', 'license_spdxId', 'license_name', 'topics'
    ]

    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for repo in data:
            # Extrai os tópicos e formata como string separada por vírgulas
            topics = ", ".join([t['topic']['name'] for t in repo['repositoryTopics']['nodes']]) if repo.get('repositoryTopics') and repo['repositoryTopics'].get('nodes') else ''

            writer.writerow({
                'name': repo.get('name'),
                'owner_login': repo['owner']['login'] if repo.get('owner') else None,
                'stargazerCount': repo.get('stargazerCount'),
                'forkCount': repo.get('forkCount'),
                'createdAt': repo.get('createdAt'),
                'updatedAt': repo.get('updatedAt'),
                'primaryLanguage': repo['primaryLanguage']['name'] if repo.get('primaryLanguage') else None,
                'pullRequests_totalCount': repo['pullRequests']['totalCount'] if repo.get('pullRequests') else None,
                'releases_totalCount': repo['releases']['totalCount'] if repo.get('releases') else None,
                'issues_closed_totalCount': repo['issues']['totalCount'] if repo.get('issues') else None,
                'issues_totalCount': repo['totalIssues']['totalCount'] if repo.get('totalIssues') else None,
                'diskUsage': repo.get('diskUsage'),
                'defaultBranch_name': repo['defaultBranchRef']['name'] if repo.get('defaultBranchRef') else None,
                'defaultBranch_commit_history_totalCount': repo['defaultBranchRef']['target']['history']['totalCount'] if repo.get('defaultBranchRef') and repo['defaultBranchRef'].get('target') and repo['defaultBranchRef']['target'].get('history') else None,
                'license_spdxId': repo['licenseInfo']['spdxId'] if repo.get('licenseInfo') else None,
                'license_name': repo['licenseInfo']['name'] if repo.get('licenseInfo') else None,
                'topics': topics
            })
    print(f"Dados salvos em {filename}")

if __name__ == '__main__':
    # Define o caminho do arquivo CSV de saída
    output_csv = os.path.join(os.path.dirname(__file__), '..', 'data', 'repositories.csv')
    repositories = get_repository_data(num_repos=1000)
    if repositories:
        save_to_csv(repositories, output_csv)
    else:
        print("Não foi possível coletar os repositórios.")
