#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Análise de Progressão Sequencial de Tipos Discursivos (TD)

Este script mapeia a distribuição linear e a alternância dos tipos 
discursivos ao longo do corpus COMENTA2.

Autor: Miguel Magalhães
Data de Modificação: Junho de 2026
"""

import os
import pandas as pd
import matplotlib.pyplot as plt

def analisar_sequencia_td(caminho_dados):
    if not os.path.exists(caminho_dados):
        print(f"Erro: O ficheiro de dados '{caminho_dados}' não foi encontrado.")
        return

    # 1. Carregamento dos Dados
    df = pd.read_csv(caminho_dados)
    
    # Adiciona a posição linear (índice da sequência)
    df['posicao'] = range(len(df))

    # 2. Configuração do Mapeamento Linguístico
    td_labels = ['DI', 'DT', 'RI', 'N', 'DI Cit', 'DT Cit', 'RI Cit', 'N Cit']
    td_mapping = {label: i+1 for i, label in enumerate(td_labels)}
    
    df['td_num'] = df['tipo_discursivo'].map(td_mapping)

    # 3. Construção da Visualização Avançada
    fig, ax = plt.subplots(figsize=(14, 6))
    
    # Utiliza cores distintas para cada tipo, facilitando a análise de padrões
    scatter = ax.scatter(df['posicao'], df['td_num'], c=df['td_num'], 
                         cmap='tab10', s=35, alpha=0.8, edgecolors='none')

    # 4. Ajustes Estéticos para Publicação Científica
    ax.set_title("Distribuição Linear dos Tipos Discursivos (Corpus COMENTA2)", 
                 fontsize=14, fontweight='bold', pad=15)
    ax.set_xlabel("Progressão Linear ao Longo do Corpus (Ocorrências)", fontsize=12, labelpad=10)
    ax.set_ylabel("Categorias de Tipos Discursivos", fontsize=12, labelpad=10)
    
    # Fixar os limites e nomes do eixo Y de forma limpa
    ax.set_yticks(list(td_mapping.values()))
    ax.set_yticklabels(list(td_mapping.keys()), fontsize=11)
    
    ax.grid(True, linestyle=':', alpha=0.6)
    ax.set_xlim(-5, len(df) + 5)

    plt.tight_layout()

    # 5. Exportação Automática do Gráfico
    os.makedirs('outputs', exist_ok=True)
    caminho_grafico = os.path.join('outputs', 'sequencia_tipos_discursivos.png')
    plt.savefig(caminho_grafico, dpi=300)
    
    print(f"Análise concluída com sucesso!")
    print(f"Gráfico de alta resolução guardado em: '{caminho_grafico}'")
    plt.show()

if __name__ == "__main__":
    # Define o caminho padrão baseado na estrutura que planeámos
    caminho_csv = os.path.join('data', 'processed', 'sequencia_corpora.csv')
    analisar_sequencia_td(caminho_csv)
