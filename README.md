# Lab 01: Análise de Repositórios Populares do GitHub

> Estudo das características de sistemas populares open-source através de análise de 1.000 repositórios com maior número de estrelas no GitHub.

## 📋 Visão Geral

Este laboratório implementa um pipeline completo de coleta, análise e visualização de dados de repositórios GitHub para responder a 7 questões de pesquisa sobre características de sistemas populares.

### Questões de Pesquisa (RQs)

- **RQ01**: Sistemas populares são maduros/antigos?
- **RQ02**: Sistemas populares recebem muita contribuição externa?
- **RQ03**: Sistemas populares lançam releases com frequência?
- **RQ04**: Sistemas populares são atualizados com frequência?
- **RQ05**: Sistemas populares são escritos nas linguagens mais populares?
- **RQ06**: Sistemas populares possuem um alto percentual de issues fechadas?
- **RQ07** (BÔNUS): Sistemas escritos em linguagens mais populares recebem mais contribuição externa, lançam mais releases e são atualizados com mais frequência?

---

## 🏗️ Arquitetura do Projeto

```
lab-experimentacao-atv01/
│
├── src/
│   ├── collect_data.py          # Sprint 1: Coleta de dados (100 repos)
│   ├── query.graphql             # Query GraphQL para API
│   ├── analyze_data.py           # Sprint 2: Análise de dados
│   └── visualize_data.py         # Sprint 3: Visualizações
│
├── data/
│   ├── repositories.csv          # Dados coletados (1000 repos)
│   └── analysis_results.json     # Resultados da análise
│
├── visualizations/
│   ├── rq01_maturity.png
│   ├── rq02_contributions.png
│   ├── rq03_releases.png
│   ├── rq04_updates.png
│   ├── rq05_languages.png
│   ├── rq06_issues.png
│   └── rq07_language_analysis.png
│
└── relatorio/
    └── relatorio_final.md        # Relatório com análise e discussão
```

---

## 📦 Pré-requisitos

### Obrigatório
- Python 3.8+
- pip (gerenciador de pacotes Python)
- GitHub Personal Access Token (PAT)

### Dependências Python
```bash
requests>=2.28.0
pandas>=1.5.0
numpy>=1.23.0
matplotlib>=3.6.0
seaborn>=0.12.0
```

---

## 🚀 Guia de Execução

### Passo 1: Configurar Ambiente

```bash
# Clonar repositório
git clone https://github.com/seu-usuario/lab-experimentacao-atv01.git
cd lab-experimentacao-atv01

# Criar ambiente virtual (recomendado)
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# ou
.venv\Scripts\activate  # Windows

# Instalar dependências
pip install -r requirements.txt
```

### Passo 2: Configurar GitHub Token

```bash
# Exportar token como variável de ambiente
export GITHUB_TOKEN="seu_token_aqui"

# Ou criar arquivo .env
echo "GITHUB_TOKEN=seu_token_aqui" > .env
```

### Passo 3: Coletar Dados (Sprint 1)

```bash
# Coletar 1000 repositórios
python src/collect_data.py

# Saída esperada:
# Iniciando a coleta de 1000 repositórios...
# Buscando 100 repositórios (cursor: None)...
# ✅ Coletados 100 repositórios até agora...
# ...
# ✅ Coleta finalizada! Total: 1000 repositórios
# ✅ Dados salvos em data/repositories.csv
```

### Passo 4: Analisar Dados (Sprint 2)

```bash
# Executar análise
python src/analyze_data.py

# Saída esperada:
# ================================================================================
# ANÁLISE DE REPOSITÓRIOS POPULARES DO GITHUB
# ================================================================================
#
# 📊 RQ01: Sistemas populares são maduros/antigos?
#    Mediana de idade: X.XX anos
#    ...
#
# ✅ Análise salva em data/analysis_results.json
```

### Passo 5: Gerar Visualizações (Sprint 3)

```bash
# Gerar gráficos
python src/visualize_data.py

# Saída esperada:
# 📊 Gerando visualizações...
# ✅ Gráfico RQ01 salvo
# ✅ Gráfico RQ02 salvo
# ...
# ✅ Todas as visualizações salvas em 'visualizations/'
```

---

## 📊 Saídas do Projeto

### Arquivo CSV (`data/repositories.csv`)

Contém 1.000 repositórios com as seguintes colunas:

| Coluna | Descrição |
|--------|-----------|
| name | Nome do repositório |
| owner_login | Login do proprietário |
| stargazerCount | Número de estrelas |
| forkCount | Número de forks |
| createdAt | Data de criação |
| updatedAt | Data de última atualização |
| primaryLanguage | Linguagem primária |
| pullRequests_totalCount | Total de PRs |
| releases_totalCount | Total de releases |
| issues_closed_totalCount | Total de issues fechadas |
| issues_totalCount | Total de issues |
| diskUsage | Tamanho do repositório |
| license_spdxId | ID SPDX da licença |
| license_name | Nome da licença |
| topics | Tópicos do repositório |

### Arquivo JSON (`data/analysis_results.json`)

Contém resultados da análise com estatísticas para cada RQ:

```json
{
  "RQ01_maturity": {
    "median_age_years": 5.5,
    "mean_age_years": 5.8,
    ...
  },
  "RQ02_contributions": {
    "median_prs": 250,
    ...
  },
  ...
}
```

### Visualizações (`visualizations/`)

7 arquivos PNG com gráficos para cada RQ:

- `rq01_maturity.png` - Distribuição de idade
- `rq02_contributions.png` - Distribuição de PRs
- `rq03_releases.png` - Distribuição de releases
- `rq04_updates.png` - Frequência de atualizações
- `rq05_languages.png` - Linguagens mais populares
- `rq06_issues.png` - Razão de issues fechadas
- `rq07_language_analysis.png` - Análise por linguagem

---

## 📈 Métricas Coletadas

### Para cada repositório:

| Métrica | Descrição | RQ |
|---------|-----------|-----|
| Idade | Dias desde criação | RQ01 |
| Pull Requests | Total de PRs aceitas | RQ02 |
| Releases | Total de releases | RQ03 |
| Dias desde atualização | Dias desde última atualização | RQ04 |
| Linguagem primária | Linguagem principal | RQ05 |
| Razão issues fechadas | Issues fechadas / Total | RQ06 |
| Análise por linguagem | Métricas agrupadas por linguagem | RQ07 |

---

## 🔧 Troubleshooting

### Erro: "GITHUB_TOKEN não está definido"

```bash
# Solução: Definir token
export GITHUB_TOKEN="seu_token"
```

### Erro: "Módulo não encontrado"

```bash
# Solução: Instalar dependências
pip install -r requirements.txt
```

### Erro: "Query failed"

```bash
# Solução: Verificar token e limite de requisições
# GitHub GraphQL API: 5.000 pontos por hora
# Cada query: ~10 pontos
```

### Arquivo CSV vazio

```bash
# Solução: Verificar se coleta completou
# Verificar logs para erros
# Tentar novamente com token novo
```

---

## 📝 Estrutura do Relatório Final

O relatório deve conter:

1. **Introdução**
   - Contexto e motivação
   - Hipóteses informais

2. **Metodologia**
   - Fonte de dados (GitHub API)
   - Critérios de seleção (stars > 1000)
   - Métricas coletadas
   - Ferramentas utilizadas

3. **Resultados**
   - Estatísticas para cada RQ
   - Tabelas com valores medianos
   - Gráficos e visualizações

4. **Discussão**
   - Comparação entre hipóteses e resultados
   - Insights obtidos
   - Limitações do estudo

5. **Conclusão**
   - Resumo dos achados
   - Trabalhos futuros

---

## 💡 Dicas

### Para Melhorar a Análise

1. **Adicionar mais métricas**
   - Watchers, forks, issues abertas
   - Tempo médio de resolução de issues
   - Frequência de commits

2. **Expandir análise por linguagem**
   - Comparar com linguagens menos populares
   - Analisar tendências ao longo do tempo

3. **Visualizações adicionais**
   - Scatter plots: idade vs PRs
   - Correlação entre métricas
   - Heatmaps de linguagens

### Para Otimizar Coleta

1. **Usar cache**
   - Salvar resultados intermediários
   - Evitar requisições duplicadas

2. **Paralelizar requisições**
   - Usar threads ou asyncio
   - Respeitar rate limits

3. **Tratar erros**
   - Retry automático
   - Logging detalhado

---

## 📚 Referências

- [GitHub GraphQL API](https://docs.github.com/en/graphql)
- [GitHub REST API](https://docs.github.com/en/rest)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)
- [Seaborn Documentation](https://seaborn.pydata.org/)

---

## 📞 Suporte

Se encontrar problemas:

1. Verifique o arquivo de log
2. Consulte o troubleshooting acima
3. Verifique a documentação das bibliotecas
4. Abra uma issue no repositório

---

## ✅ Checklist

- [ ] Ambiente configurado
- [ ] GitHub token definido
- [ ] Dependências instaladas
- [ ] Dados coletados (1000 repos)
- [ ] Análise executada
- [ ] Visualizações geradas
- [ ] Relatório elaborado
- [ ] Projeto entregue

---

## 📄 Licença

MIT License - veja LICENSE para detalhes

---

## 🎓 Conclusão

Após completar este laboratório, você terá:

✅ Experiência com coleta de dados via API GraphQL
✅ Prática em análise exploratória de dados
✅ Habilidades em visualização de dados
✅ Compreensão de características de projetos open-source populares
✅ Capacidade de responder questões de pesquisa com dados

**Bom trabalho! 🚀**
