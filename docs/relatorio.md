# Relatório

## 1. Introdução
Repositórios open-source evoluem por contribuições distribuídas, o que pode afetar atributos de qualidade interna como modularidade, manutenibilidade e legibilidade. Este estudo investiga como essas características se relacionam com aspectos do processo de desenvolvimento em projetos Java populares no GitHub, a partir de métricas de produto obtidas pela ferramenta CK. Entender como características do processo se relacionam com indicadores de qualidade interna em projetos Java do Github. Existe relação entre popularidade, idade, atividade e tamanho dos repositórios e métricas de qualidade de código? Repositorios mais populares tendem a ter melhor qualiadade; H2 — repositórios mais maduros tendem a apresentar melhor qualidade; H3 — repositórios mais ativos tendem a ter melhor qualidade; H4 — repositórios maiores tendem a apresentar piores indicadores de qualidade. Investigar a relação entre características dos repositórios Java no GitHub e métricas de qualidade extraídas pela ferramenta CK, analisando possíveis correlações entre essas variáveis.

Hipóteses (informais):
- H1 (Popularidade): Repositórios mais populares (mais estrelas) tendem a apresentar melhor qualidade (menor acoplamento e maior coesão).
- H2 (Maturidade): Repositórios mais maduros (mais antigos) tendem a apresentar melhor qualidade.
- H3 (Atividade): Repositórios mais ativos (mais releases) tendem a apresentar melhor qualidade.
- H4 (Tamanho): Repositórios maiores (mais LOC e arquivos) tendem a apresentar piores indicadores de qualidade (maior acoplamento e menor coesão), por efeito de escala e complexidade.

## 2. Metodologia
- Passo a passo do experimento: seleção dos Top-1.000 repositórios Java via API GraphQL; processamento em streaming (clona → mede → grava → remove); consolidação e análise (`process_streaming.py`, `analyze_rqs.py`).
- Decisões: foco em repositórios Java; popularidade medida por estrelas; sumarização em nível de repositório; pipeline efêmero para reduzir armazenamento.
- Materiais utilizados: GitHub GraphQL API, Git, `cloc` (LOC/comments) e CK (CBO/DIT/LCOM); scripts em `sprint2/scripts/` e dados em `sprint2/data/`.
- Métodos utilizados: mineração de repositórios, extração automática de métricas, consolidação de dados e análise correlacional (Pearson e Spearman).
- Métricas e suas unidades: stars, releases e arquivos (contagem); idade (dias/anos); LOC e comentários (linhas); CBO (acoplamento), DIT (níveis de herança) e LCOM (índice de coesão).

## 3. Visualização dos Resultados
- Processo: Popularidade (stars), Atividade (releases), Maturidade (age_years), Tamanho (LOC=code, comment, files).
- Produto (CK): CBO (acoplamento), DIT (profundidade de herança), LCOM (falta de coesão). Estatísticas por repo: média/mediana/desvio padrão (quando aplicável).

## 4. Discussão dos resultados
- RQ01. Relação entre popularidade e qualidade (stars vs. CK)
- RQ02. Relação entre maturidade e qualidade (age_years vs. CK)
- RQ03. Relação entre atividade e qualidade (releases vs. CK)
- RQ04. Relação entre tamanho e qualidade (code/comment/files vs. CK)

## 5. Conclusão
Os dados completos estão em `sprint2/data/processed/analysis_summary.csv` e `correlations.csv`. Abaixo, um resumo das correlações mais fortes observadas (Spearman/Pearson), usando `summarize_correlations_stdlib.py`.

Principais correlações (Spearman, |r|):
- code vs lcom_std: r≈0.585 (n≈959)
- comment vs lcom_std: r≈0.554
- code vs cbo_std: r≈0.552
- code vs dit_std: r≈0.498
- releases vs cbo_std: r≈0.452

Principais correlações (Pearson, |r|):
- code vs cbo_std: r≈0.396
- files vs cbo_std: r≈0.355
- comment vs cbo_std: r≈0.327
- releases vs cbo_std: r≈0.250

Medi ana de |Spearman| por métrica de processo (x):
- code: 0.410; comment: 0.374; releases: 0.320; files: 0.310; age_years: 0.098; stars: 0.034

Visualizações (ver `sprint2/data/processed/plots/`):
- code_vs_cbo_median.png, code_vs_dit_median.png, code_vs_lcom_median.png
- stars_vs_cbo_median.png, stars_vs_dit_median.png, stars_vs_lcom_median.png
- releases_vs_cbo_median.png, age_years_vs_cbo_median.png

### Índice de Tabelas
- [Tabela 1. Top-5 Correlações (Spearman)](#tabela1)
- [Tabela 2. Top-5 Correlações (Pearson)](#tabela2)
- [Tabela 3. Mediana de |Spearman| por métrica de processo](#tabela3)

<!-- TABLES:BEGIN -->
#### <a name="tabela1"></a>Tabela 1. Top-5 Correlações (Spearman)

| x | y | r | p | n |
| --- | --- | --- | --- | --- |
| code | lcom_std | 0.5848031500719191 | 4.63713980371053e-89 | 959 |
| comment | lcom_std | 0.5539849660829098 | 3.0753216668322773e-78 | 959 |
| code | cbo_std | 0.5517094426505765 | 1.7485317873596725e-77 | 959 |
| code | dit_std | 0.4977010730068818 | 3.667787505144869e-61 | 959 |
| comment | cbo_std | 0.49375461244112967 | 4.4245385208227285e-60 | 959 |


#### <a name="tabela2"></a>Tabela 2. Top-5 Correlações (Pearson)

| x | y | r | p | n |
| --- | --- | --- | --- | --- |
| code | cbo_std | 0.3963483208559621 | 1.9802175259732372e-37 | 959 |
| files | cbo_std | 0.35462296810042726 | 8.499512181930061e-30 | 959 |
| comment | cbo_std | 0.32735493710625596 | 2.175460375115346e-25 | 959 |
| releases | cbo_std | 0.2504000150112532 | 3.548890311691589e-15 | 959 |
| code | cbo_mean | 0.2425405460498759 | 2.634485842905888e-14 | 959 |


#### <a name="tabela3"></a>Tabela 3. Mediana de |Spearman| por métrica de processo

| x | median_|r| |
| --- | --- |
| code | 0.410 |
| comment | 0.374 |
| releases | 0.320 |
| files | 0.310 |
| age_years | 0.098 |
| stars | 0.034 |
<!-- TABLES:END -->


