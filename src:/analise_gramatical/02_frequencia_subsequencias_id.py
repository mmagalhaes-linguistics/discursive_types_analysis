#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Análise de Subsequências e N-gramas de Tipos Discursivos

Este script deteta e contabiliza padrões sequenciais (comprimento 2 a 4) 
de Tipos Discursivos para IDs específicos a partir do dataset centralizado.

Autor: Miguel Magalhães
Data de Modificação: Junho de 2026
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

def obter_subsequencias(lista_td, comp_min=2, comp_max=4):
    """Extrai subsequências contínuas de elementos de texto."""
    subsequencias = []
    for comprimento in range(comp_min, comp_max + 1):
        subsequencias += [
            ' ➔ '.join(lista_td[i:i+comprimento])
            for i in range(len(lista_td) - comprimento + 1)
        ]
    return subsequencias

def analisar_subsequencias_por_id(caminho_dados, id_alvo):
    if not os.path.exists(caminho_dados):
        print(f"Erro: O ficheiro '{caminho_dados}' não foi encontrado.")
        return

    # 1. Carregamento e Filtragem Dinâmica pelo ID selecionado
    df = pd.read_csv(caminho_dados)
    
    # Adaptar nomes de colunas do seu CSV unificado
    df_filtrado = df[df['id'] == id_alvo]
    
    if df_filtrado.empty:
        print(f"Aviso: O ID {id_alvo} não foi encontrado no ficheiro de dados.")
        return

    lista_td = df_filtrado['tipo_discursivo'].astype(str).tolist()

    # 2. Extração e Contagem de Padrões Sequenciais
    subsequencias_detetadas = obter_subsequencias(lista_td, comp_min=2, comp_max=4)
    frequencia_padroes = Counter(subsequencias_detetadas)

    # 3. Estruturação dos Resultados (Top 15 mais frequentes)
    df_freq = pd.DataFrame(frequencia_padroes.items(), columns=['Padrão Sequencial', 'Frequência'])
    df_freq = df_freq.sort_values(by='Frequência', ascending=False).head(15)

    # 4. Construção do Gráfico Horizontal Académico
    plt.figure(figsize=(11, 6))
    plt.barh(df_freq['Padrão Sequencial'], df_freq['Frequência'], color='#34495e', edgecolor='none', height=0.6)
    
    plt.xlabel('Frequência Absoluta (Ocorrências)', fontsize=11, labelpad=10)
    plt.ylabel('Padrões de Transição (N-gramas)', fontsize=11, labelpad=10)
    plt.title(f'Top 15 Subsequências de Tipos Discursivos\n(Documento ID: {id_alvo})', fontsize=13, fontweight='bold', pad=15)
    
    plt.gca().invert_yaxis()  # Garante que o mais frequente fica no topo
    plt.grid(axis='x', linestyle=':', alpha=0.6)
    plt.tight_layout()

    # 5. Exportação Automática
    os.makedirs('outputs', exist_ok=True)
    caminho_grafico = os.path.join('outputs', f'subsequencias_id_{id_alvo}.png')
    plt.savefig(caminho_grafico, dpi=300)
    
    print(f"Análise do ID {id_alvo} concluída!")
    print(f"Gráfico de padrões guardado em: '{caminho_grafico}'")
    plt.show()

if __name__ == "__main__":
    # Caminho para o ficheiro de dados sequenciais unificado
    caminho_csv = os.path.join('data', 'processed', 'sequencia_corpora.csv')
    
    # Pode alterar o número do ID aqui para analisar qualquer outro texto da sua tese
    id_para_analise = 130 
    analisar_subsequencias_por_id(caminho_csv, id_alvo=id_para_analise)
