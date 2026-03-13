# 📋 Mapa de Instalação - Lab 01 (Análise de Repositórios GitHub)

## 🎯 Resumo Executivo

Você recebeu **6 novos arquivos** que completam o laboratório de análise de repositórios GitHub. Estes arquivos implementam as Sprints 2 e 3, além de documentação e configuração.

---

## 📂 Estrutura de Arquivos

### Arquivos Novos a Adicionar

```
lab-experimentacao-atv01/
│
├── src/
│   ├── collect_data.py           ← JÁ EXISTE (Sprint 1)
│   ├── query.graphql             ← NOVO
│   ├── analyze_data.py           ← NOVO (Sprint 2)
│   └── visualize_data.py         ← NOVO (Sprint 3)
│
├── requirements.txt              ← NOVO
├── README_LAB.md                 ← NOVO (substitui README.md)
├── GUIA_INSTALACAO.md            ← NOVO
│
└── data/
    └── repositories.csv          ← GERADO PELA SPRINT 1
```

---

## 📥 Instruções de Instalação

### Passo 1: Copiar Arquivos

Copie os arquivos fornecidos para as pastas corretas:

```bash
# Copiar arquivos Python para src/
cp query.graphql lab-experimentacao-atv01/src/
cp analyze_data.py lab-experimentacao-atv01/src/
cp visualize_data.py lab-experimentacao-atv01/src/

# Copiar arquivo de dependências
cp requirements.txt lab-experimentacao-atv01/

# Copiar documentação
cp README_LAB.md lab-experimentacao-atv01/README.md
cp GUIA_INSTALACAO.md lab-experimentacao-atv01/
```

### Passo 2: Verificar Estrutura

```bash
# Verificar se arquivos estão no lugar certo
cd lab-experimentacao-atv01

# Verificar src/
ls -la src/
# Esperado: collect_data.py, query.graphql, analyze_data.py, visualize_data.py

# Verificar raiz
ls -la *.md *.txt
# Esperado: README.md, GUIA_INSTALACAO.md, requirements.txt
```

### Passo 3: Instalar Dependências

```bash
# Criar ambiente virtual
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
# ou
.venv\Scripts\activate  # Windows

# Instalar dependências
pip install -r requirements.txt
```

### Passo 4: Configurar GitHub Token

```bash
# Exportar token
export GITHUB_TOKEN="seu_token_aqui"

# Ou criar arquivo .env
echo "GITHUB_TOKEN=seu_token_aqui" > .env
```

### Passo 5: Executar Sprints

```bash
# Sprint 1: Coleta (já feita, mas pode repetir)
python src/collect_data.py

# Sprint 2: Análise (NOVO)
python src/analyze_data.py

# Sprint 3: Visualizações (NOVO)
python src/visualize_data.py
```

---

## 📄 Descrição dos Arquivos

### 1. **query.graphql** (NOVO)

**Localização:** `src/query.graphql`
**Tamanho:** ~1.5 KB
**Conteúdo:**
- Query GraphQL completa para API do GitHub
- Coleta todas as métricas necessárias para as 7 RQs
- Usa paginação para eficiência

**Uso:**
- Utilizado por `collect_data.py`
- Não precisa ser modificado

---

### 2. **analyze_data.py** (NOVO - Sprint 2)

**Localização:** `src/analyze_data.py`
**Tamanho:** ~8 KB
**Conteúdo:**
- Classe `RepositoryAnalyzer` para análise de dados
- Implementa cálculos para todas as 7 RQs
- Gera arquivo JSON com resultados

**Funcionalidades:**
- RQ01: Calcula idade dos repositórios
- RQ02: Analisa pull requests
- RQ03: Analisa releases
- RQ04: Analisa frequência de atualizações
- RQ05: Conta linguagens
- RQ06: Calcula razão de issues fechadas
- RQ07: Análise por linguagem (bônus)

**Uso:**
```bash
python src/analyze_data.py
```

**Saída:**
- `data/analysis_results.json` - Resultados em JSON
- Imprime resumo no console

---

### 3. **visualize_data.py** (NOVO - Sprint 3)

**Localização:** `src/visualize_data.py`
**Tamanho:** ~10 KB
**Conteúdo:**
- Classe `RepositoryVisualizer` para gerar gráficos
- Cria 7 visualizações (uma por RQ)
- Usa matplotlib e seaborn

**Visualizações:**
- `rq01_maturity.png` - Histograma + box plot de idade
- `rq02_contributions.png` - Histograma + box plot de PRs
- `rq03_releases.png` - Histograma + pie chart de releases
- `rq04_updates.png` - Histograma + categorias de atualização
- `rq05_languages.png` - Gráfico de barras horizontal (top 15)
- `rq06_issues.png` - Histograma + box plot de razão
- `rq07_language_analysis.png` - 4 gráficos por linguagem

**Uso:**
```bash
python src/visualize_data.py
```

**Saída:**
- Pasta `visualizations/` com 7 arquivos PNG

---

### 4. **requirements.txt** (NOVO)

**Localização:** `requirements.txt` (raiz)
**Tamanho:** ~200 bytes
**Conteúdo:**
```
requests>=2.28.0
pandas>=1.5.0
numpy>=1.23.0
matplotlib>=3.6.0
seaborn>=0.12.0
python-dotenv>=0.20.0
```

**Uso:**
```bash
pip install -r requirements.txt
```

---

### 5. **README_LAB.md** (NOVO)

**Localização:** `README.md` (substitui o antigo)
**Tamanho:** ~8 KB
**Conteúdo:**
- Visão geral do laboratório
- Arquitetura do projeto
- Guia de execução (5 passos)
- Descrição de saídas
- Métricas coletadas
- Troubleshooting
- Referências

**Uso:**
- Documentação principal do projeto
- Leia primeiro para entender o projeto

---

### 6. **GUIA_INSTALACAO.md** (NOVO)

**Localização:** `GUIA_INSTALACAO.md` (raiz)
**Tamanho:** ~7 KB
**Conteúdo:**
- Pré-requisitos detalhados
- Passo a passo de instalação
- Configuração de GitHub token
- Execução de cada sprint
- Troubleshooting detalhado
- Checklist de verificação

**Uso:**
- Guia passo a passo para iniciantes
- Referência para problemas de instalação

---

## ✅ Checklist de Instalação

- [ ] Baixou os 6 arquivos
- [ ] Copiou para as pastas corretas
- [ ] Verificou estrutura de pastas
- [ ] Criou ambiente virtual
- [ ] Instalou dependências
- [ ] Configurou GitHub token
- [ ] Executou Sprint 2 (analyze_data.py)
- [ ] Executou Sprint 3 (visualize_data.py)
- [ ] Verificou saídas (JSON + PNG)
- [ ] Fez commit dos novos arquivos

---

## 🔍 Verificação

Após instalar, verifique se tudo está correto:

```bash
# 1. Verificar arquivos Python
python -m py_compile src/analyze_data.py
python -m py_compile src/visualize_data.py

# 2. Verificar dependências
pip list | grep -E "pandas|matplotlib|seaborn|requests"

# 3. Verificar estrutura
find . -type f -name "*.py" -o -name "*.graphql" -o -name "*.txt" -o -name "*.md"

# 4. Executar análise de teste
python src/analyze_data.py

# 5. Verificar saídas
ls -la data/analysis_results.json
ls -la visualizations/*.png
```

---

## 📊 Estrutura Final do Repositório

Após instalação, seu repositório ficará assim:

```
lab-experimentacao-atv01/
│
├── README.md                     # Documentação principal (ATUALIZADO)
├── GUIA_INSTALACAO.md            # Guia passo a passo
├── requirements.txt              # Dependências Python
│
├── src/
│   ├── collect_data.py           # Sprint 1: Coleta (já existia)
│   ├── query.graphql             # Query GraphQL (NOVO)
│   ├── analyze_data.py           # Sprint 2: Análise (NOVO)
│   └── visualize_data.py         # Sprint 3: Visualizações (NOVO)
│
├── data/
│   ├── repositories.csv          # 1000 repositórios (gerado)
│   └── analysis_results.json     # Resultados análise (gerado)
│
└── visualizations/
    ├── rq01_maturity.png         # Gráfico RQ01 (gerado)
    ├── rq02_contributions.png    # Gráfico RQ02 (gerado)
    ├── rq03_releases.png         # Gráfico RQ03 (gerado)
    ├── rq04_updates.png          # Gráfico RQ04 (gerado)
    ├── rq05_languages.png        # Gráfico RQ05 (gerado)
    ├── rq06_issues.png           # Gráfico RQ06 (gerado)
    └── rq07_language_analysis.png # Gráfico RQ07 (gerado)
```

---

## 🚀 Próximos Passos

Após instalar os novos arquivos:

1. **Leia o README.md**
   - Entenda a estrutura do projeto
   - Veja as questões de pesquisa

2. **Siga o GUIA_INSTALACAO.md**
   - Instale dependências
   - Configure GitHub token
   - Execute as sprints

3. **Analise os Resultados**
   - Abra `data/analysis_results.json`
   - Visualize os gráficos em `visualizations/`

4. **Elabore o Relatório**
   - Crie `relatorio/relatorio_final.md`
   - Inclua análise e discussão das 7 RQs

---

## 💡 Dicas

### Para Entender o Código
- Comece por `analyze_data.py` - mais simples
- Depois estude `visualize_data.py` - mais complexo
- Use comentários no código como guia

### Para Customizar
- Modifique `analyze_data.py` para adicionar métricas
- Edite `visualize_data.py` para novos gráficos
- Atualize `query.graphql` para coletar mais dados

### Para Otimizar
- Use cache para evitar requisições duplicadas
- Paralelizar requisições GraphQL
- Adicionar logging detalhado

---

## ❓ FAQ

**P: Preciso substituir o README.md?**
R: Sim, o novo é mais completo. Mas você pode manter ambos.

**P: Posso editar os arquivos Python?**
R: Sim! Adapte conforme sua necessidade.

**P: Onde coloco os arquivos?**
R: Siga a estrutura indicada acima.

**P: Preciso fazer algo especial no código?**
R: Não! Os arquivos estão prontos para usar.

**P: Posso usar em produção?**
R: Não, é apenas para análise acadêmica.

---

## 📞 Suporte

Se tiver dúvidas:

1. Verifique o arquivo relevante (README ou GUIA)
2. Procure na seção "Troubleshooting"
3. Consulte a documentação das bibliotecas
4. Teste manualmente seguindo os exemplos

---

## ✨ Conclusão

Você agora tem:
- ✅ Código de análise completo
- ✅ Código de visualização completo
- ✅ Documentação detalhada
- ✅ Guia de instalação
- ✅ Projeto pronto para entregar

**Parabéns! Seu laboratório está 100% completo! 🎉**
