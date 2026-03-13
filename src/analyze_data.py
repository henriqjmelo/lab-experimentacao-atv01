import pandas as pd
import numpy as np
from datetime import datetime
import json

class RepositoryAnalyzer:
    """Classe para analisar dados de repositórios do GitHub"""
    
    def __init__(self, csv_path):
        """Inicializa o analisador com dados do CSV"""
        self.df = pd.read_csv(csv_path)
        self.prepare_data()
        
    def prepare_data(self):
        """Prepara os dados para análise"""
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
        
        # Calcular idade do repositório (em dias)
        self.df['age_days'] = (now - self.df['createdAt']).dt.days
        self.df['age_years'] = self.df['age_days'] / 365.25
        
        # Calcular dias desde última atualização
        self.df['days_since_update'] = (now - self.df['updatedAt']).dt.days
        
        # Calcular commits por ano (frequência de desenvolvimento)
        self.df['defaultBranch_commit_history_totalCount'] = self.df['defaultBranch_commit_history_totalCount'].fillna(0)
        self.df['commits_per_year'] = np.where(
            self.df['age_years'] > 0,
            self.df['defaultBranch_commit_history_totalCount'] / self.df['age_years'],
            self.df['defaultBranch_commit_history_totalCount']
        )
        
        # Calcular razão de issues fechadas
        self.df['closed_issues_ratio'] = np.where(
            self.df['issues_totalCount'] > 0,
            self.df['issues_closed_totalCount'] / self.df['issues_totalCount'],
            0
        )
        
        # Preencher NaN com 0 para contagens
        for col in ['pullRequests_totalCount', 'releases_totalCount', 'issues_closed_totalCount', 'issues_totalCount']:
            self.df[col] = self.df[col].fillna(0)
    
    def rq01_repository_maturity(self):
        """RQ 01: Sistemas populares são maduros/antigos?"""
        stats = {
            'median_age_years': float(self.df['age_years'].median()),
            'mean_age_years': float(self.df['age_years'].mean()),
            'min_age_years': float(self.df['age_years'].min()),
            'max_age_years': float(self.df['age_years'].max()),
            'std_age_years': float(self.df['age_years'].std()),
            'q1_age_years': float(self.df['age_years'].quantile(0.25)),
            'q3_age_years': float(self.df['age_years'].quantile(0.75)),
        }
        return stats
    
    def rq02_external_contributions(self):
        """RQ 02: Sistemas populares recebem muita contribuição externa?"""
        stats = {
            'median_prs': float(self.df['pullRequests_totalCount'].median()),
            'mean_prs': float(self.df['pullRequests_totalCount'].mean()),
            'min_prs': float(self.df['pullRequests_totalCount'].min()),
            'max_prs': float(self.df['pullRequests_totalCount'].max()),
            'std_prs': float(self.df['pullRequests_totalCount'].std()),
            'q1_prs': float(self.df['pullRequests_totalCount'].quantile(0.25)),
            'q3_prs': float(self.df['pullRequests_totalCount'].quantile(0.75)),
            'total_prs': float(self.df['pullRequests_totalCount'].sum()),
        }
        return stats
    
    def rq03_release_frequency(self):
        """RQ 03: Sistemas populares lançam releases com frequência?"""
        stats = {
            'median_releases': float(self.df['releases_totalCount'].median()),
            'mean_releases': float(self.df['releases_totalCount'].mean()),
            'min_releases': float(self.df['releases_totalCount'].min()),
            'max_releases': float(self.df['releases_totalCount'].max()),
            'std_releases': float(self.df['releases_totalCount'].std()),
            'q1_releases': float(self.df['releases_totalCount'].quantile(0.25)),
            'q3_releases': float(self.df['releases_totalCount'].quantile(0.75)),
            'repos_with_releases': int((self.df['releases_totalCount'] > 0).sum()),
            'repos_without_releases': int((self.df['releases_totalCount'] == 0).sum()),
        }
        return stats
    
    def rq04_update_frequency(self):
        """RQ 04: Sistemas populares são atualizados com frequência?"""
        stats = {
            'median_days_since_update': float(self.df['days_since_update'].median()),
            'mean_days_since_update': float(self.df['days_since_update'].mean()),
            'min_days_since_update': float(self.df['days_since_update'].min()),
            'max_days_since_update': float(self.df['days_since_update'].max()),
            'std_days_since_update': float(self.df['days_since_update'].std()),
            'q1_days_since_update': float(self.df['days_since_update'].quantile(0.25)),
            'q3_days_since_update': float(self.df['days_since_update'].quantile(0.75)),
            'repos_updated_last_week': int((self.df['days_since_update'] <= 7).sum()),
            'repos_updated_last_month': int((self.df['days_since_update'] <= 30).sum()),
            'repos_updated_last_year': int((self.df['days_since_update'] <= 365).sum()),
            'median_commits_per_year': float(self.df['commits_per_year'].median()),
            'mean_commits_per_year': float(self.df['commits_per_year'].mean()),
            'min_commits_per_year': float(self.df['commits_per_year'].min()),
            'max_commits_per_year': float(self.df['commits_per_year'].max()),
            'std_commits_per_year': float(self.df['commits_per_year'].std()),
            'q1_commits_per_year': float(self.df['commits_per_year'].quantile(0.25)),
            'q3_commits_per_year': float(self.df['commits_per_year'].quantile(0.75)),
            'total_commits': float(self.df['defaultBranch_commit_history_totalCount'].sum()),
        }
        return stats
    
    def rq05_primary_languages(self):
        """RQ 05: Sistemas populares são escritos nas linguagens mais populares?"""
        # Remover valores NaN
        languages = self.df['primaryLanguage'].dropna()
        language_counts = languages.value_counts()
        
        stats = {
            'total_languages': int(len(language_counts)),
            'repos_without_language': int(self.df['primaryLanguage'].isna().sum()),
            'top_languages': language_counts.head(10).to_dict(),
            'language_distribution': language_counts.to_dict(),
        }
        return stats
    
    def rq06_closed_issues_ratio(self):
        """RQ 06: Sistemas populares possuem um alto percentual de issues fechadas?"""
        # Apenas repositórios com issues
        repos_with_issues = self.df[self.df['issues_totalCount'] > 0]
        
        stats = {
            'median_closed_ratio': float(repos_with_issues['closed_issues_ratio'].median()),
            'mean_closed_ratio': float(repos_with_issues['closed_issues_ratio'].mean()),
            'min_closed_ratio': float(repos_with_issues['closed_issues_ratio'].min()),
            'max_closed_ratio': float(repos_with_issues['closed_issues_ratio'].max()),
            'std_closed_ratio': float(repos_with_issues['closed_issues_ratio'].std()),
            'q1_closed_ratio': float(repos_with_issues['closed_issues_ratio'].quantile(0.25)),
            'q3_closed_ratio': float(repos_with_issues['closed_issues_ratio'].quantile(0.75)),
            'repos_with_issues': int(len(repos_with_issues)),
            'repos_without_issues': int((self.df['issues_totalCount'] == 0).sum()),
        }
        return stats
    
    def rq07_language_analysis(self):
        """RQ 07 (BÔNUS): Análise por linguagem das RQs 02, 03 e 04"""
        # Remover repositórios sem linguagem definida
        df_with_lang = self.df[self.df['primaryLanguage'].notna()].copy()
        
        language_analysis = {}
        
        for lang in df_with_lang['primaryLanguage'].unique():
            lang_data = df_with_lang[df_with_lang['primaryLanguage'] == lang]
            
            language_analysis[lang] = {
                'count': int(len(lang_data)),
                'median_prs': float(lang_data['pullRequests_totalCount'].median()),
                'mean_prs': float(lang_data['pullRequests_totalCount'].mean()),
                'median_releases': float(lang_data['releases_totalCount'].median()),
                'mean_releases': float(lang_data['releases_totalCount'].mean()),
                'median_days_since_update': float(lang_data['days_since_update'].median()),
                'mean_days_since_update': float(lang_data['days_since_update'].mean()),
                'median_commits_per_year': float(lang_data['commits_per_year'].median()),
                'mean_commits_per_year': float(lang_data['commits_per_year'].mean()),
                'total_prs': float(lang_data['pullRequests_totalCount'].sum()),
                'total_releases': float(lang_data['releases_totalCount'].sum()),
                'total_commits': float(lang_data['defaultBranch_commit_history_totalCount'].sum()),
            }
        
        # Ordenar por número de repositórios
        sorted_analysis = dict(sorted(
            language_analysis.items(),
            key=lambda x: x[1]['count'],
            reverse=True
        ))
        
        return sorted_analysis
    
    def generate_all_analysis(self):
        """Gera análise completa de todas as RQs"""
        analysis = {
            'RQ01_maturity': self.rq01_repository_maturity(),
            'RQ02_contributions': self.rq02_external_contributions(),
            'RQ03_releases': self.rq03_release_frequency(),
            'RQ04_updates': self.rq04_update_frequency(),
            'RQ05_languages': self.rq05_primary_languages(),
            'RQ06_issues': self.rq06_closed_issues_ratio(),
            'RQ07_language_analysis': self.rq07_language_analysis(),
        }
        return analysis
    
    def save_analysis_json(self, output_path):
        """Salva análise em arquivo JSON"""
        analysis = self.generate_all_analysis()
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(analysis, f, indent=2, ensure_ascii=False)
        
        print(f"✅ Análise salva em {output_path}")
    
    def print_summary(self):
        """Imprime resumo da análise"""
        analysis = self.generate_all_analysis()
        
        print("\n" + "="*80)
        print("ANÁLISE DE REPOSITÓRIOS POPULARES DO GITHUB")
        print("="*80)
        
        print("\n📊 RQ01: Sistemas populares são maduros/antigos?")
        print(f"   Mediana de idade: {analysis['RQ01_maturity']['median_age_years']:.2f} anos")
        print(f"   Média de idade: {analysis['RQ01_maturity']['mean_age_years']:.2f} anos")
        print(f"   Intervalo: {analysis['RQ01_maturity']['min_age_years']:.2f} - {analysis['RQ01_maturity']['max_age_years']:.2f} anos")
        
        print("\n📊 RQ02: Sistemas populares recebem muita contribuição externa?")
        print(f"   Mediana de PRs: {analysis['RQ02_contributions']['median_prs']:.0f}")
        print(f"   Média de PRs: {analysis['RQ02_contributions']['mean_prs']:.0f}")
        print(f"   Total de PRs: {analysis['RQ02_contributions']['total_prs']:.0f}")
        
        print("\n📊 RQ03: Sistemas populares lançam releases com frequência?")
        print(f"   Mediana de releases: {analysis['RQ03_releases']['median_releases']:.0f}")
        print(f"   Média de releases: {analysis['RQ03_releases']['mean_releases']:.0f}")
        print(f"   Repos com releases: {analysis['RQ03_releases']['repos_with_releases']}")
        print(f"   Repos sem releases: {analysis['RQ03_releases']['repos_without_releases']}")
        
        print("\n📊 RQ04: Sistemas populares são atualizados com frequência?")
        print(f"   Mediana de dias desde última atualização: {analysis['RQ04_updates']['median_days_since_update']:.0f} dias")
        print(f"   Média de dias desde última atualização: {analysis['RQ04_updates']['mean_days_since_update']:.0f} dias")
        print(f"   Mediana de commits/ano: {analysis['RQ04_updates']['median_commits_per_year']:.2f}")
        print(f"   Média de commits/ano: {analysis['RQ04_updates']['mean_commits_per_year']:.2f}")
        print(f"   Total de commits: {analysis['RQ04_updates']['total_commits']:.0f}")
        print(f"   Atualizados na última semana: {analysis['RQ04_updates']['repos_updated_last_week']}")
        print(f"   Atualizados no último mês: {analysis['RQ04_updates']['repos_updated_last_month']}")
        
        print("\n📊 RQ05: Sistemas populares são escritos nas linguagens mais populares?")
        print(f"   Total de linguagens: {analysis['RQ05_languages']['total_languages']}")
        print(f"   Repos sem linguagem definida: {analysis['RQ05_languages']['repos_without_language']}")
        print("   Top 10 linguagens:")
        for lang, count in list(analysis['RQ05_languages']['top_languages'].items())[:10]:
            print(f"      {lang}: {count}")
        
        print("\n📊 RQ06: Sistemas populares possuem um alto percentual de issues fechadas?")
        print(f"   Mediana de razão de issues fechadas: {analysis['RQ06_issues']['median_closed_ratio']:.2%}")
        print(f"   Média de razão de issues fechadas: {analysis['RQ06_issues']['mean_closed_ratio']:.2%}")
        print(f"   Repos com issues: {analysis['RQ06_issues']['repos_with_issues']}")
        
        print("\n📊 RQ07 (BÔNUS): Análise por linguagem")
        print("   Top 5 linguagens por número de repositórios:")
        for i, (lang, data) in enumerate(list(analysis['RQ07_language_analysis'].items())[:5], 1):
            print(f"   {i}. {lang}:")
            print(f"      Repositórios: {data['count']}")
            print(f"      Mediana PRs: {data['median_prs']:.0f}")
            print(f"      Mediana releases: {data['median_releases']:.0f}")
            print(f"      Mediana commits/ano: {data['median_commits_per_year']:.2f}")
            print(f"      Mediana dias desde update: {data['median_days_since_update']:.0f}")
        
        print("\n" + "="*80)

if __name__ == '__main__':
    import os
    
    # Caminho do CSV
    csv_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'repositories.csv')
    output_json = os.path.join(os.path.dirname(__file__), '..', 'data', 'analysis_results.json')
    
    # Criar analisador
    analyzer = RepositoryAnalyzer(csv_path)
    
    # Imprimir resumo
    analyzer.print_summary()
    
    # Salvar análise em JSON
    analyzer.save_analysis_json(output_json)