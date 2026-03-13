# 📋 Guia de Instalação - Lab 01

> Instruções passo a passo para configurar e executar o laboratório

---

## 🎯 Visão Geral

Este guia cobre:
1. Preparação do ambiente
2. Instalação de dependências
3. Configuração do GitHub token
4. Execução de cada sprint
5. Troubleshooting

---

## 📦 Pré-requisitos

### Sistema Operacional
- Windows 10+, macOS 10.14+, ou Linux (Ubuntu 18.04+)

### Software Necessário
- **Python 3.8+** - [Download](https://www.python.org/downloads/)
- **Git** - [Download](https://git-scm.com/)
- **Editor de Texto** - VS Code, PyCharm, ou similar

### Verificar Instalação

```bash
# Verificar Python
python --version
# Saída esperada: Python 3.8.0 ou superior

# Verificar Git
git --version
# Saída esperada: git version 2.x.x

# Verificar pip
pip --version
# Saída esperada: pip 20.0 ou superior
```

---

## 🚀 Passo 1: Clonar o Repositório

```bash
# Opção 1: Via HTTPS
git clone https://github.com/seu-usuario/lab-experimentacao-atv01.git
cd lab-experimentacao-atv01

# Opção 2: Via SSH (se configurado)
git clone git@github.com:seu-usuario/lab-experimentacao-atv01.git
cd lab-experimentacao-atv01
```

---

## 🔧 Passo 2: Configurar Ambiente Virtual

### Windows

```bash
# Criar ambiente virtual
python -m venv .venv

# Ativar ambiente virtual
.venv\Scripts\activate

# Saída esperada:
# (.venv) C:\Users\seu-usuario\lab-experimentacao-atv01>
```

### macOS / Linux

```bash
# Criar ambiente virtual
python3 -m venv .venv

# Ativar ambiente virtual
source .venv/bin/activate

# Saída esperada:
# (.venv) seu-usuario@computador:~/lab-experimentacao-atv01$
```

---

## 📚 Passo 3: Instalar Dependências

```bash
# Atualizar pip (recomendado)
pip install --upgrade pip

# Instalar dependências do projeto
pip install -r requirements.txt

# Verificar instalação
pip list

# Saída esperada:
# Package         Version
# --------------- -------
# requests        2.28.0
# pandas          1.5.0
# numpy           1.23.0
# matplotlib      3.6.0
# seaborn         0.12.0
# python-dotenv   0.20.0
```

---

## 🔑 Passo 4: Configurar GitHub Token

### Obter Token

1. Acesse https://github.com/settings/tokens
2. Clique em "Generate new token"
3. Selecione escopo `public_repo`
4. Clique em "Generate token"
5. **Copie o token** (não será mostrado novamente)

### Configurar Variável de Ambiente

#### Opção 1: Variável de Ambiente Permanente

**Windows:**
1. Abra "Variáveis de Ambiente" (System Properties)
2. Clique em "New" (Variável de Usuário)
3. Nome: `GITHUB_TOKEN`
4. Valor: `seu_token_aqui`
5. Clique OK e reinicie o terminal

**macOS / Linux:**
```bash
# Adicionar ao ~/.bashrc ou ~/.zshrc
echo 'export GITHUB_TOKEN="seu_token_aqui"' >> ~/.bashrc
source ~/.bashrc
```

#### Opção 2: Arquivo .env (Temporário)

```bash
# Criar arquivo .env na raiz do projeto
echo "GITHUB_TOKEN=seu_token_aqui" > .env

# Verificar
cat .env
# Saída: GITHUB_TOKEN=seu_token_aqui
```

#### Opção 3: Linha de Comando (Temporário)

```bash
# Windows (PowerShell)
$env:GITHUB_TOKEN="seu_token_aqui"

# macOS / Linux (Bash)
export GITHUB_TOKEN="seu_token_aqui"
```

### Verificar Configuração

```bash
# Verificar se token está definido
echo $GITHUB_TOKEN

# Saída esperada:
# seu_token_aqui
```

---

## 🏃 Passo 5: Executar Sprint 1 - Coleta de Dados

```bash
# Ativar ambiente virtual (se não estiver ativo)
source .venv/bin/activate  # macOS/Linux
# ou
.venv\Scripts\activate  # Windows

# Executar coleta
python src/collect_data.py

# Saída esperada:
# Iniciando a coleta de 1000 repositórios...
# Buscando 100 repositórios (cursor: None)...
# ✅ Coletados 100 repositórios até agora... (página com 100 repos)
# Buscando 100 repositórios (cursor: Y3Vyc29yOjEwMA==)...
# ✅ Coletados 200 repositórios até agora... (página com 100 repos)
# ...
# ✅ Coleta finalizada! Total: 1000 repositórios
# ✅ Dados salvos em data/repositories.csv
```

**Tempo estimado:** 5-10 minutos

---

## 📊 Passo 6: Executar Sprint 2 - Análise de Dados

```bash
# Executar análise
python src/analyze_data.py

# Saída esperada:
# ================================================================================
# ANÁLISE DE REPOSITÓRIOS POPULARES DO GITHUB
# ================================================================================
#
# 📊 RQ01: Sistemas populares são maduros/antigos?
#    Mediana de idade: 5.50 anos
#    Média de idade: 5.80 anos
#    Intervalo: 0.10 - 15.50 anos
#
# 📊 RQ02: Sistemas populares recebem muita contribuição externa?
#    Mediana de PRs: 250
#    Média de PRs: 1500
#    Total de PRs: 1500000
#
# ... (mais resultados)
#
# ✅ Análise salva em data/analysis_results.json
```

**Tempo estimado:** 1-2 minutos

---

## 📈 Passo 7: Executar Sprint 3 - Visualizações

```bash
# Executar visualizações
python src/visualize_data.py

# Saída esperada:
# 📊 Gerando visualizações...
# ✅ Gráfico RQ01 salvo
# ✅ Gráfico RQ02 salvo
# ✅ Gráfico RQ03 salvo
# ✅ Gráfico RQ04 salvo
# ✅ Gráfico RQ05 salvo
# ✅ Gráfico RQ06 salvo
# ✅ Gráfico RQ07 salvo
#
# ✅ Todas as visualizações salvas em 'visualizations/'
```

**Tempo estimado:** 1-2 minutos

---

## 📁 Verificar Saídas

```bash
# Verificar se CSV foi criado
ls -la data/repositories.csv

# Verificar se análise foi salva
ls -la data/analysis_results.json

# Verificar visualizações
ls -la visualizations/

# Saída esperada:
# rq01_maturity.png
# rq02_contributions.png
# rq03_releases.png
# rq04_updates.png
# rq05_languages.png
# rq06_issues.png
# rq07_language_analysis.png
```

---

## 🐛 Troubleshooting

### Erro: "ModuleNotFoundError: No module named 'requests'"

```bash
# Solução: Instalar dependências
pip install -r requirements.txt

# Ou instalar módulo específico
pip install requests
```

### Erro: "GITHUB_TOKEN não está definido"

```bash
# Solução 1: Definir variável
export GITHUB_TOKEN="seu_token"

# Solução 2: Criar arquivo .env
echo "GITHUB_TOKEN=seu_token" > .env

# Solução 3: Usar arquivo .env
pip install python-dotenv
```

### Erro: "Query failed to run by returning code of 401"

```bash
# Solução: Token inválido ou expirado
# 1. Gerar novo token em https://github.com/settings/tokens
# 2. Atualizar variável de ambiente
# 3. Tentar novamente
```

### Erro: "Query failed to run by returning code of 403"

```bash
# Solução: Rate limit atingido
# GitHub GraphQL API: 5.000 pontos por hora
# Aguarde 1 hora ou use novo token
```

### Erro: "FileNotFoundError: query.graphql"

```bash
# Solução: Verificar se arquivo existe
ls -la src/query.graphql

# Se não existir, criar arquivo com conteúdo correto
```

### Erro: "Permission denied" no Linux/Mac

```bash
# Solução: Dar permissão de execução
chmod +x src/collect_data.py
chmod +x src/analyze_data.py
chmod +x src/visualize_data.py
```

---

## ✅ Checklist de Instalação

- [ ] Python 3.8+ instalado
- [ ] Git instalado
- [ ] Repositório clonado
- [ ] Ambiente virtual criado
- [ ] Ambiente virtual ativado
- [ ] Dependências instaladas
- [ ] GitHub token obtido
- [ ] GITHUB_TOKEN configurado
- [ ] Sprint 1 executada com sucesso
- [ ] Sprint 2 executada com sucesso
- [ ] Sprint 3 executada com sucesso
- [ ] Arquivos de saída verificados

---

## 🎯 Próximos Passos

Após completar a instalação:

1. **Revisar dados coletados**
   ```bash
   head -10 data/repositories.csv
   ```

2. **Analisar resultados**
   ```bash
   cat data/analysis_results.json | python -m json.tool
   ```

3. **Visualizar gráficos**
   - Abrir arquivos PNG em `visualizations/`

4. **Elaborar relatório**
   - Criar `relatorio/relatorio_final.md`
   - Incluir análise e discussão

---

## 📞 Suporte

Se encontrar problemas não listados:

1. Verifique a documentação das bibliotecas
2. Consulte a [documentação do GitHub GraphQL](https://docs.github.com/en/graphql)
3. Abra uma issue no repositório
4. Procure ajuda em fóruns (Stack Overflow, etc)

---

## 🎓 Conclusão

Parabéns! Você completou a instalação e execução do laboratório. Agora você tem:

✅ 1.000 repositórios coletados
✅ Análise completa das 7 RQs
✅ 7 gráficos de visualização
✅ Dados prontos para relatório

**Próximo passo: Elaborar o relatório final! 📝**
