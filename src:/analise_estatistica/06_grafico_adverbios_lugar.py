#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Visualização de Frequência de Advérbios de Lugar nos Corpora

Este script gera um gráfico de barras agrupadas de alta resolução para 
comparar a distribuição de advérbios entre CETEM, COMENTA2 e COMJUR.

Autor: Miguel Magalhães
Data de Modificação: Junho de 2026
"""

import os
import pandas as pd
import matplotlib.pyplot as plt

def gerar_grafico_frequencias():
    # 1. Base de Dados Interne
    data = {
        'Palavra': ['aqui', 'aí', 'ali', 'cá', 'lá', 'acolá', 'além'],
        'CETEM':,
        'COMENTA2':,
        'COMJUR':,
    }

    df = pd.DataFrame(data)

    # 2. Ordenação Académica: Ordenar pela soma total de ocorrências da palavra
    df['Total'] = df[['CETEM', 'COMENTA2', 'COMJUR']].sum(axis=1)
    df_sorted = df.sort_values(by='Total', ascending=False).drop(columns=['Total'])

    # 3. Configuração Geométrica do Gráfico
    x = range(len(df_sorted['Palavra']))
    largura = 0.25
    cores = {'CETEM': '#3498db', 'COMENTA2': '#e67e22', 'COMJUR': '#2ecc71'}

    fig, ax = plt.subplots(figsize=(10, 6))

    # Desenhar as barras com pequenos desvios para não se sobreporem
    ax.bar([i - largura for i in x], df_sorted['CETEM'], width=largura, label='CETEM', color=cores['CETEM'])
    ax.bar(x, df_sorted['COMENTA2'], width=largura, label='COMENTA2', color=cores['COMENTA2'])
    ax.bar([i + largura for i in x], df_sorted['COMJUR'], width=largura, label='COMJUR', color=cores['COMJUR'])

    # 4. Elementos Textuais e Estética (Padrão de Publicação)
    ax.set_title("Distribuição de Advérbios de Lugar por Corpus", fontsize=14, fontweight='bold', pad=15)
    ax.set_xlabel("Advérbios", fontsize=12, labelpad=10)
    ax.set_ylabel("Frequência Absoluta (Ocorrências)", fontsize=12, labelpad=10)
    ax.set_xticks(x)
    ax.set_xticklabels(df_sorted['Palavra'], fontsize=11)
    
    # Legenda limpa e única no canto superior direito
    ax.legend(title="Corpora Analisados", title_fontsize=11, fontsize=10, loc='upper right')
    ax.grid(axis='y', linestyle='--', alpha=0.5)

    plt.tight_layout()

    # 5. Exportação Automática para a Pasta de Outputs
    # Cria a pasta caso ela ainda não exista localmente
    os.makedirs('outputs', exist_ok=True)
    caminho_saida = os.path.join('outputs', 'grafico_frequencia_adverbios.png')
    
    # Guarda em 300 DPI (qualidade exigida pelas revistas científicas)
    plt.savefig(caminho_saida, dpi=300)
    print(f"Sucesso! Gráfico guardado em de alta resolução em: '{caminho_saida}'")
    
    # Mostra no ecrã durante a execução local
    plt.show()

if __name__ == "__main__":
    gerar_grafico_frequencias()

