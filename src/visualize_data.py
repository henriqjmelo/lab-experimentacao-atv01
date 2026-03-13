import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from datetime import datetime
import os

class RepositoryVisualizer:
    """Classe para gerar visualizações dos dados de repositórios"""
    
    def __init__(self, csv_path, output_dir='visualizations'):
        """Inicializa o visualizador"""
        self.df = pd.read_csv(csv_path)
        self.output_dir = output_dir
        self.prepare_data()
        self.setup_style()
        
        # Criar diretório de saída
        os.makedirs(self.output_dir, exist_ok=True)
    
    def prepare_data(self):
        """Prepara os dados para visualização"""
        # Converter datas
        self.df['createdAt'] = pd.to_datetime(self.df['createdAt'])
        self.df['updatedAt'] = pd.to_datetime(self.df['updatedAt'])
        
        # Remover timezone para comparação (usar UTC)
        if self.df['createdAt'].dt.tz is not None:
            self.df['createdAt'] = self.df['createdAt'].dt.tz_localize(None)
        if self.df['updatedAt'].dt.tz is not None:
            self.df['updatedAt'] = self.df['updatedAt'].dt.tz_localize(None)
        
        # Usar pd.Timestamp.now() sem timezone
        now = pd.Timestamp.now()
        
        # Calcular idade do repositório
        self.df['age_years'] = (now - self.df['createdAt']).dt.days / 365.25
        self.df['days_since_update'] = (now - self.df['updatedAt']).dt.days
        
        # Calcular razão de issues fechadas
        self.df['closed_issues_ratio'] = np.where(
            self.df['issues_totalCount'] > 0,
            self.df['issues_closed_totalCount'] / self.df['issues_totalCount'],
            0
        )
        
        # Preencher NaN
        for col in ['pullRequests_totalCount', 'releases_totalCount', 'issues_closed_totalCount', 'issues_totalCount']:
            self.df[col] = self.df[col].fillna(0)
    
    def setup_style(self):
        """Configura estilo dos gráficos"""
        sns.set_style("whitegrid")
        plt.rcParams['figure.figsize'] = (12, 6)
        plt.rcParams['font.size'] = 10
    
    def plot_rq01_maturity(self):
        """Visualiza idade dos repositórios (RQ01)"""
        fig, axes = plt.subplots(1, 2, figsize=(14, 5))
        
        # Histograma
        axes[0].hist(self.df['age_years'], bins=50, color='steelblue', edgecolor='black', alpha=0.7)
        axes[0].axvline(self.df['age_years'].median(), color='red', linestyle='--', linewidth=2, label=f'Mediana: {self.df["age_years"].median():.1f} anos')
        axes[0].set_xlabel('Idade (anos)')
        axes[0].set_ylabel('Número de Repositórios')
        axes[0].set_title('RQ01: Distribuição de Idade dos Repositórios')
        axes[0].legend()
        axes[0].grid(True, alpha=0.3)
        
        # Box plot
        axes[1].boxplot(self.df['age_years'], vert=True)
        axes[1].set_ylabel('Idade (anos)')
        axes[1].set_title('RQ01: Box Plot - Idade dos Repositórios')
        axes[1].grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig(os.path.join(self.output_dir, 'rq01_maturity.png'), dpi=300, bbox_inches='tight')
        print("✅ Gráfico RQ01 salvo")
        plt.close()
    
    def plot_rq02_contributions(self):
        """Visualiza contribuições externas (RQ02)"""
        fig, axes = plt.subplots(1, 2, figsize=(14, 5))
        
        # Histograma com escala logarítmica
        axes[0].hist(self.df['pullRequests_totalCount'] + 1, bins=50, color='forestgreen', edgecolor='black', alpha=0.7)
        axes[0].set_xlabel('Total de Pull Requests (escala linear)')
        axes[0].set_ylabel('Número de Repositórios')
        axes[0].set_title('RQ02: Distribuição de Pull Requests')
        axes[0].axvline(self.df['pullRequests_totalCount'].median(), color='red', linestyle='--', linewidth=2, label=f'Mediana: {self.df["pullRequests_totalCount"].median():.0f}')
        axes[0].legend()
        axes[0].grid(True, alpha=0.3)
        
        # Box plot
        axes[1].boxplot(self.df['pullRequests_totalCount'], vert=True)
        axes[1].set_ylabel('Total de Pull Requests')
        axes[1].set_title('RQ02: Box Plot - Pull Requests')
        axes[1].grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig(os.path.join(self.output_dir, 'rq02_contributions.png'), dpi=300, bbox_inches='tight')
        print("✅ Gráfico RQ02 salvo")
        plt.close()
    
    def plot_rq03_releases(self):
        """Visualiza frequência de releases (RQ03)"""
        fig, axes = plt.subplots(1, 2, figsize=(14, 5))
        
        # Histograma
        axes[0].hist(self.df['releases_totalCount'], bins=50, color='coral', edgecolor='black', alpha=0.7)
        axes[0].set_xlabel('Total de Releases')
        axes[0].set_ylabel('Número de Repositórios')
        axes[0].set_title('RQ03: Distribuição de Releases')
        axes[0].axvline(self.df['releases_totalCount'].median(), color='red', linestyle='--', linewidth=2, label=f'Mediana: {self.df["releases_totalCount"].median():.0f}')
        axes[0].legend()
        axes[0].grid(True, alpha=0.3)
        
        # Pie chart: com vs sem releases
        with_releases = (self.df['releases_totalCount'] > 0).sum()
        without_releases = (self.df['releases_totalCount'] == 0).sum()
        axes[1].pie([with_releases, without_releases], labels=['Com Releases', 'Sem Releases'], autopct='%1.1f%%', colors=['lightgreen', 'lightcoral'])
        axes[1].set_title('RQ03: Repositórios com/sem Releases')
        
        plt.tight_layout()
        plt.savefig(os.path.join(self.output_dir, 'rq03_releases.png'), dpi=300, bbox_inches='tight')
        print("✅ Gráfico RQ03 salvo")
        plt.close()
    
    def plot_rq04_updates(self):
        """Visualiza frequência de atualizações (RQ04)"""
        fig, axes = plt.subplots(1, 2, figsize=(14, 5))
        
        # Histograma
        axes[0].hist(self.df['days_since_update'], bins=50, color='mediumpurple', edgecolor='black', alpha=0.7)
        axes[0].set_xlabel('Dias desde última atualização')
        axes[0].set_ylabel('Número de Repositórios')
        axes[0].set_title('RQ04: Distribuição de Dias desde Última Atualização')
        axes[0].axvline(self.df['days_since_update'].median(), color='red', linestyle='--', linewidth=2, label=f'Mediana: {self.df["days_since_update"].median():.0f} dias')
        axes[0].legend()
        axes[0].grid(True, alpha=0.3)
        
        # Categorias de atualização
        categories = ['Última semana', 'Último mês', 'Último ano', 'Mais de 1 ano']
        counts = [
            (self.df['days_since_update'] <= 7).sum(),
            ((self.df['days_since_update'] > 7) & (self.df['days_since_update'] <= 30)).sum(),
            ((self.df['days_since_update'] > 30) & (self.df['days_since_update'] <= 365)).sum(),
            (self.df['days_since_update'] > 365).sum(),
        ]
        axes[1].bar(categories, counts, color=['green', 'yellow', 'orange', 'red'], edgecolor='black', alpha=0.7)
        axes[1].set_ylabel('Número de Repositórios')
        axes[1].set_title('RQ04: Categorias de Atualização')
        axes[1].grid(True, alpha=0.3, axis='y')
        
        plt.tight_layout()
        plt.savefig(os.path.join(self.output_dir, 'rq04_updates.png'), dpi=300, bbox_inches='tight')
        print("✅ Gráfico RQ04 salvo")
        plt.close()
    
    def plot_rq05_languages(self):
        """Visualiza linguagens primárias (RQ05)"""
        # Top 15 linguagens
        languages = self.df['primaryLanguage'].dropna().value_counts().head(15)
        
        fig, ax = plt.subplots(figsize=(12, 8))
        languages.plot(kind='barh', ax=ax, color='teal', edgecolor='black', alpha=0.7)
        ax.set_xlabel('Número de Repositórios')
        ax.set_title('RQ05: Top 15 Linguagens Primárias')
        ax.grid(True, alpha=0.3, axis='x')
        
        plt.tight_layout()
        plt.savefig(os.path.join(self.output_dir, 'rq05_languages.png'), dpi=300, bbox_inches='tight')
        print("✅ Gráfico RQ05 salvo")
        plt.close()
    
    def plot_rq06_issues(self):
        """Visualiza razão de issues fechadas (RQ06)"""
        # Apenas repos com issues
        repos_with_issues = self.df[self.df['issues_totalCount'] > 0]
        
        fig, axes = plt.subplots(1, 2, figsize=(14, 5))
        
        # Histograma
        axes[0].hist(repos_with_issues['closed_issues_ratio'], bins=50, color='skyblue', edgecolor='black', alpha=0.7)
        axes[0].set_xlabel('Razão de Issues Fechadas')
        axes[0].set_ylabel('Número de Repositórios')
        axes[0].set_title('RQ06: Distribuição de Razão de Issues Fechadas')
        axes[0].axvline(repos_with_issues['closed_issues_ratio'].median(), color='red', linestyle='--', linewidth=2, label=f'Mediana: {repos_with_issues["closed_issues_ratio"].median():.2%}')
        axes[0].legend()
        axes[0].grid(True, alpha=0.3)
        
        # Box plot
        axes[1].boxplot(repos_with_issues['closed_issues_ratio'], vert=True)
        axes[1].set_ylabel('Razão de Issues Fechadas')
        axes[1].set_title('RQ06: Box Plot - Razão de Issues Fechadas')
        axes[1].grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig(os.path.join(self.output_dir, 'rq06_issues.png'), dpi=300, bbox_inches='tight')
        print("✅ Gráfico RQ06 salvo")
        plt.close()
    
    def plot_rq07_language_analysis(self):
        """Visualiza análise por linguagem (RQ07 - BÔNUS)"""
        # Top 10 linguagens
        df_with_lang = self.df[self.df['primaryLanguage'].notna()]
        top_langs = df_with_lang['primaryLanguage'].value_counts().head(10).index
        
        df_top = df_with_lang[df_with_lang['primaryLanguage'].isin(top_langs)]
        
        fig, axes = plt.subplots(2, 2, figsize=(16, 12))
        
        # PRs por linguagem
        prs_by_lang = df_top.groupby('primaryLanguage')['pullRequests_totalCount'].median().sort_values(ascending=True)
        axes[0, 0].barh(prs_by_lang.index, prs_by_lang.values, color='steelblue', edgecolor='black', alpha=0.7)
        axes[0, 0].set_xlabel('Mediana de Pull Requests')
        axes[0, 0].set_title('RQ07: Mediana de PRs por Linguagem')
        axes[0, 0].grid(True, alpha=0.3, axis='x')
        
        # Releases por linguagem
        releases_by_lang = df_top.groupby('primaryLanguage')['releases_totalCount'].median().sort_values(ascending=True)
        axes[0, 1].barh(releases_by_lang.index, releases_by_lang.values, color='forestgreen', edgecolor='black', alpha=0.7)
        axes[0, 1].set_xlabel('Mediana de Releases')
        axes[0, 1].set_title('RQ07: Mediana de Releases por Linguagem')
        axes[0, 1].grid(True, alpha=0.3, axis='x')
        
        # Dias desde update por linguagem
        update_by_lang = df_top.groupby('primaryLanguage')['days_since_update'].median().sort_values(ascending=True)
        axes[1, 0].barh(update_by_lang.index, update_by_lang.values, color='coral', edgecolor='black', alpha=0.7)
        axes[1, 0].set_xlabel('Mediana de Dias desde Última Atualização')
        axes[1, 0].set_title('RQ07: Mediana de Dias desde Update por Linguagem')
        axes[1, 0].grid(True, alpha=0.3, axis='x')
        
        # Número de repos por linguagem
        count_by_lang = df_top['primaryLanguage'].value_counts().sort_values(ascending=True)
        axes[1, 1].barh(count_by_lang.index, count_by_lang.values, color='mediumpurple', edgecolor='black', alpha=0.7)
        axes[1, 1].set_xlabel('Número de Repositórios')
        axes[1, 1].set_title('RQ07: Número de Repositórios por Linguagem')
        axes[1, 1].grid(True, alpha=0.3, axis='x')
        
        plt.tight_layout()
        plt.savefig(os.path.join(self.output_dir, 'rq07_language_analysis.png'), dpi=300, bbox_inches='tight')
        print("✅ Gráfico RQ07 salvo")
        plt.close()
    
    def generate_all_visualizations(self):
        """Gera todas as visualizações"""
        print("\n📊 Gerando visualizações...")
        self.plot_rq01_maturity()
        self.plot_rq02_contributions()
        self.plot_rq03_releases()
        self.plot_rq04_updates()
        self.plot_rq05_languages()
        self.plot_rq06_issues()
        self.plot_rq07_language_analysis()
        print(f"\n✅ Todas as visualizações salvas em '{self.output_dir}/'")

if __name__ == '__main__':
    # Caminho do CSV
    csv_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'repositories.csv')
    output_dir = os.path.join(os.path.dirname(__file__), '..', 'visualizations')
    
    # Criar visualizador
    visualizer = RepositoryVisualizer(csv_path, output_dir)
    
    # Gerar todas as visualizações
    visualizer.generate_all_visualizations()