#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Matriz de Correlação de Tipos Discursivos (Género: Notícia)

Este script analisa a coocorrência e correlação binária (Coeficiente Phi)
entre os diferentes tipos discursivos presentes no corpus de notícias.

Autor: Miguel Magalhães
Data de Modificação: Junho de 2026
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def calcular_correlacao_noticias(caminho_dados):
    if not os.path.exists(caminho_dados):
        print(f"Erro: O ficheiro '{caminho_dados}' não foi encontrado.")
        return

    # 1. Carregamento e Preparação dos Dados
    df = pd.read_csv(caminho_dados)
    
    # One-Hot Encoding das categorias linguísticas
    df_encoded = pd.get_dummies(df, columns=["TD"], prefix="", prefix_sep="")
    
    # Consolidação por ID de documento (Presença/Ausência binária)
    df_documentos = df_encoded.groupby("ID").max()

    # 2. Cálculo da Matriz de Correlação (Equivalente ao Coeficiente Phi)
    matriz_corr = df_documentos.corr(method='pearson')

    # 3. Construção do Mapa de Calor (Heatmap) Académico
    plt.figure(figsize=(8, 6))
    
    # Máscara opcional para esconder a metade superior se preferir (opcional)
    sns.heatmap(matriz_corr, 
                annot=True, 
                cmap="coolwarm", 
                center=0, 
                fmt=".2f", 
                square=True,
                linewidths=.5, 
                cbar_kws={"shrink": .8, "label": "Coeficiente de Correlação (r)"})
    
    plt.title("Matriz de Correlação de Tipos Discursivos\n(Género: Notícia)", 
              fontsize=13, fontweight='bold', pad=15)
    plt.tight_layout()

    # 4. Exportação do Gráfico de Alta Resolução
    os.makedirs('outputs', exist_ok=True)
    caminho_grafico = os.path.join('outputs', 'heatmap_correlacao_noticia.png')
    plt.savefig(caminho_grafico, dpi=300)
    
    print("Análise de correlação concluída!")
    print(f"Gráfico guardado com sucesso em: '{caminho_grafico}'")
    plt.show()

if __name__ == "__main__":
    # Define o caminho para os dados dentro da estrutura planeada
    caminho_csv = os.path.join('data', 'processed', 'dados_noticia.csv')
    calcular_correlacao_noticias(caminho_csv)
