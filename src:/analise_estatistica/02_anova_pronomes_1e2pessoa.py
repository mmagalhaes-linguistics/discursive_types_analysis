#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Análise Estatística Exclusiva de Pronomes de 1ª e 2ª Pessoa

Este script compara a distribuição das formas pronominais de 1ª e 2ª pessoa
entre os corpora CETEM, COMENTA2 e COMJUR, isolando a variação da 3ª pessoa.

Autor: Miguel Magalhães
Data de Modificação: Junho de 2026
"""

import pandas as pd
from scipy import stats

def analisar_pronomes_1e2():
    print("--- Análise Estatística: 1ª e 2ª Pessoa Gramatical --- \n")

    # 1. Base de Dados Filtrada (Apenas 1ª e 2ª pessoa)
    dados = {
        'Pessoa': ['1ª pessoa', '2ª pessoa'],
        'CETEM':,
        'COMENTA2':,
        'COMJUR': [46, 0]
    }
    df = pd.DataFrame(dados)

    # 2. Teste de Qui-Quadrado de Independência
    tabela_contingencia = df.set_index('Pessoa')[['CETEM', 'COMENTA2', 'COMJUR']]
    chi2, p_val, dof, expected = stats.chi2_contingency(tabela_contingencia)
    
    print("Resultados do Teste de Qui-Quadrado:")
    print(f"Estatística Chi2: {chi2:.4f}")
    print(f"Valor de p (p-value): {p_val:.4e}")
    print(f"Graus de Liberdade: {dof}")
    
    if p_val < 0.05:
        print("\nResultado: Estatisticamente significativo (p < 0.05).")
        print("A proporção entre a 1ª e a 2ª pessoa varia significativamente consoante o corpus.")
    else:
        print("\nResultado: Não significativo (p >= 0.05).")
        print("A relação entre a 1ª e a 2ª pessoa é estável e independente do corpus.")

if __name__ == "__main__":
    analisar_pronomes_1e2()
