#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Análise Estatística de Pronomes Pessoais inter-Corpora

Este script realiza uma análise comparativa da distribuição de pronomes
pessoais (1ª, 2ª e 3ª pessoa) entre os corpora CETEM, COMENTA2 e COMJUR.
Inclui o teste ANOVA original e o teste de Qui-Quadrado de Independência.

Autor: Miguel Magalhães
Data de Modificação: Junho de 2026
"""

import pandas as pd
from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import ols

def analisar_pronomes():
    print("--- Análise Estatística: Pronomes Pessoais --- \n")

    # 1. Base de Dados
    dados = {
        'Pessoa': ['1ª pessoa', '2ª pessoa', '3ª pessoa'],
        'CETEM':,
        'COMENTA2':,
        'COMJUR': [46, 0, 356]
    }
    df = pd.DataFrame(dados)

    # 2. Execução do ANOVA Original (Abordagem por Modelos Lineares)
    df_melt = pd.melt(df, id_vars=['Pessoa'], value_vars=['CETEM', 'COMENTA2', 'COMJUR'],
                      var_name='Corpus', value_name='Frequencia')
    
    modelo = ols('Frequencia ~ Corpus', data=df_melt).fit()
    tabela_anova = sm.stats.anova_lm(modelo, typ=2)
    
    print("1. [MÉTODO ORIGINAL] Tabela ANOVA (Comparação de Médias brutas):")
    print(tabela_anova)
    print("-" * 60)

    # 3. [CORREÇÃO METODOLÓGICA] Teste de Qui-Quadrado de Independência
    # Ideal para tabelas de contingência de frequências absolutas em linguística
    tabela_contingencia = df.set_index('Pessoa')[['CETEM', 'COMENTA2', 'COMJUR']]
    
    chi2, p_val, dof, expected = stats.chi2_contingency(tabela_contingencia)
    
    print("\n2. [MÉTODO RECOMENDADO] Teste de Qui-Quadrado de Independência:")
    print(f"Estatística Chi2: {chi2:.4f}")
    print(f"Valor de p (p-value): {p_val:.4e}")
    print(f"Graus de Liberdade: {dof}")
    
    if p_val < 0.05:
        print("\nResultado: Altamente significativo (p < 0.05).")
        print("A distribuição dos pronomes pessoais depende significativamente do corpus analisado.")
    else:
        print("\nResultado: Não significativo (p >= 0.05).")
        print("Não há evidência de associação entre a escolha do pronome e o corpus.")

if __name__ == "__main__":
    analisar_pronomes()
