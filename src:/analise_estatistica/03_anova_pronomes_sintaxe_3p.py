#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Análise Estatística dos Pronomes de 3ª Pessoa por Função Sintática

Este script analisa a distribuição das funções sintáticas (Sujeito, COD, COB, 
Apassiva) dos pronomes de 3ª pessoa nos corpora CETEM, COMENTA2 e COMJUR.
Executa o ANOVA original e introduz o Teste de Qui-Quadrado de Independência.

Autor: Miguel Magalhães
Data de Modificação: Junho de 2026
"""

import pandas as pd
from scipy import stats

def analisar_sintaxe_pronomes():
    print("--- Análise Estatística: Funções Sintáticas (3ª Pessoa) --- \n")

    # 1. Base de Dados Baseada na Tese
    dados = {
        'Funcao_Sintatica': ['Pronomes Sujeito', 'COD', 'COB', 'Apassiva'],
        'CETEM':,
        'COMENTA2':,
        'COMJUR': [2, 0, 2, 0]
    }
    df = pd.DataFrame(dados)

    # 2. Teste ANOVA Original (Preservação Metodológica)
    anova_result = stats.f_oneway(df['CETEM'], df['COMENTA2'], df['COMJUR'])
    print(f"1. [MÉTODO ORIGINAL] Valor-p do ANOVA: {anova_result.pvalue:.4f}")
    print("-" * 60)

    # 3. [CORREÇÃO CIENTÍFICA] Teste de Qui-Quadrado de Independência
    # Define a matriz de contigência cruzando funções sintáticas com os corpora
    tabela_contingencia = df.set_index('Funcao_Sintatica')[['CETEM', 'COMENTA2', 'COMJUR']]
    
    chi2, p_val, dof, expected = stats.chi2_contingency(tabela_contingencia)
    
    print("\n2. [MÉTODO RECOMENDADO] Teste de Qui-Quadrado de Independência:")
    print(f"Estatística Chi2: {chi2:.4f}")
    print(f"Valor de p (p-value): {p_val:.4e}")
    print(f"Graus de Liberdade: {dof}")
    
    # Interpretação estatística padrão (alfa = 0.05)
    if p_val < 0.05:
        print("\nResultado: Estatisticamente significativo (p < 0.05).")
        print("A escolha da função sintática do pronome de 3ª pessoa está associada de forma significativa ao tipo de corpus.")
    else:
        print("\nResultado: Não significativo (p >= 0.05).")
        print("Não há evidência de que a distribuição das funções sintáticas varie entre os corpora.")

if __name__ == "__main__":
    analisar_sintaxe_pronomes()
