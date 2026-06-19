#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Matriz de Correlação de Tipos Discursivos (Género: Comentário)

Este script analisa a coocorrência e correlação binária dos tipos discursivos
dentro do corpus COMENTA2, utilizando o ficheiro de dados sequencial unificado.

Autor: Miguel Magalhães
Data de Modificação: Junho de 2026
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def calcular_correlacao_comentarios(caminho_dados):
    if not os.path.exists(caminho_dados):
        print(f"Erro: O ficheiro '{caminho_dados}' não foi encontrado.")
        print("Certifique-se de que o ficheiro 'sequencia_corpora.csv' está na pasta 'data/processed/'.")
        return

    # 1. Carregamento dos Dados a partir do CSV Centralizado
    df = pd.read_csv(caminho_dados)
    
    # Mapeamento dos nomes das colunas conforme configurámos no CSV
    coluna_id = 'id'
    coluna_td = 'tipo_discursivo'

    # 2. Processamento Metodológico: One-Hot Encoding e Agrupamento por ID
    # Transforma as etiquetas de texto em colunas binárias (0 ou 1)
    df_encoded = pd.get_dummies(df, columns=[coluna_td], prefix='', prefix_sep='')
    
    # Agrupa por ID de documento para consolidar quais os TD que coocorrem no mesmo texto
    if coluna_id in df_encoded.columns:
        # Mantém apenas colunas numéricas para o cálculo da correlação
        df_agrupado = df_encoded.groupby(coluna_id).max().select_dtypes(include=['number'])
    else:
        print(f"Aviso: Coluna '{coluna_id}' não encontrada. A calcular por ocorrência isolada.")
        df_agrupado = pd.get_dummies(df[coluna_td])

    # 3. Cálculo da Correlação (Equivalente ao Coeficiente Phi para dados binários)
    correlacao_td = df_agrupado.corr(method='pearson')

    # 4. Construção do Heatmap para Publicação Académica
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlacao_td, annot=True, cmap='coolwarm', vmin=-1, vmax=1, square=True, linewidths=.5)
    plt.title('Matriz de Correlação dos Tipos Discursivos\n(Género: Comentário - COMENTA2)', fontsize=13, fontweight='bold', pad=15)
    plt.tight_layout()

    # 5. Exportação Automática de Resultados
    os.makedirs('outputs', exist_ok=True)
    
    # Guardar Gráfico em alta resolução (300 DPI) para o artigo/tese
    caminho_grafico = os.path.join('outputs', 'heatmap_correlacao_comentario.png')
    plt.savefig(caminho_grafico, dpi=300)
    
    # Guardar Matriz numérica em Excel para anexos ou consultas rápidas
    caminho_excel = os.path.join('outputs', 'matriz_correlacao_comentario.xlsx')
    correlacao_td.to_excel(caminho_excel)

    print("Análise concluída com sucesso!")
    print(f"Gráfico de alta resolução guardado em: '{caminho_grafico}'")
    print(f"Matriz Excel de correlação guardada em: '{caminho_excel}'")
    plt.show()

if __name__ == "__main__":
    # Caminho relativo unificado apontando para o CSV correto
    caminho_entrada = os.path.join('data', 'processed', 'sequencia_corpora.csv')
    calcular_correlacao_comentarios(caminho_entrada)
