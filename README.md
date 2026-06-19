# Discursive Types Analysis
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20764207.svg)](https://doi.org/10.5281/zenodo.20764207)
Este repositório contém o ecossistema de código desenvolvido para a análise quantitativa, extração gramatical e validação estatística da minha tese de Doutoramento intitulada **"O COMENTÁRIO: DA LINGUÍSTICA DO TEXTO AO TEXT MINING"**, defendida na **UNIVERSIDADE NOVA DE LISBOA / FACULDADE DE CIÊNCIAS SOCIAIS E HUMANAS**.

Estes dados focam-se na distribuição linear, coocorrência e variação sintático-discursiva de Tipos Discursivos (TD) e formas pronominais nos corpora *CETEM*, *COMENTA2* e *COMJUR*.

---

## 📁 Estrutura do Repositório

O projeto está organizado metodologicamente seguindo as melhores práticas de Ciência Aberta:

* **`src/analise_gramatical/`**: Scripts focados na estrutura, ordenação e padrões sequenciais linguísticos.
  * `01_analise_sequencias.py`: Mapeamento e visualização da progressão linear de TDs no corpus COMENTA2.
  * `02_frequencia_subsequencias.py`: Deteção e contagem de N-gramas (padrões de transição de comprimento 2 a 4) por ID de documento.
* **`src/analise_estatistica/`**: Scripts dedicados à modelação estatística e testes de hipóteses.
  * `01_anova_pronomes_todos.py`: Comparação inter-corpora da distribuição geral de pronomes (1ª, 2ª e 3ª pessoa).
  * `02_anova_pronomes_1e2_pessoa.py`: Análise estatística isolada focada nos pronomes de 1ª e 2ª pessoa (interlocução).
  * `03_anova_pronomes_sintaxe_3p.py`: Teste estatístico detalhado das funções sintáticas (Sujeito, COD, COB, Apassiva) da 3ª pessoa.
  * `04_correlacao_td_noticias.py`: Matriz de correlação binária e heatmap para o género Notícia.
  * `05_correlacao_td_comentario.py`: Matriz de correlação binária e heatmap para o género Comentário (COMENTA2).
  * `06_grafico_adverbios_lugar.py`: Gráfico de barras agrupadas em alta resolução da distribuição de advérbios de lugar.

---

## 🛠️ Requisitos e Instalação

Para replicar as análises estatísticas e gerar os gráficos do projeto, certifique-se de que tem o Python 3 instalado. Clone o repositório e instale as bibliotecas necessárias:

```bash
pip install -r requirements.txt
```

### Bibliotecas Principais Utilizadas:
* `pandas` & `numpy` (Manipulação de matrizes de dados)
* `scipy` & `statsmodels` (Testes ANOVA e Qui-Quadrado de Independência)
* `matplotlib` & `seaborn` (Visualização de dados com padrão de publicação científica)

---

## 📊 Reprodutibilidade e Dados

Para garantir o cumprimento de políticas de privacidade e direitos de autor dos *corpora* originais, os dados brutos e ficheiros gerados localmente (pastas `data/` e `outputs/`) estão protegidos e são omitidos via `.gitignore`. 

O fluxo de dados baseia-se num ficheiro central unificado (`data/processed/sequencia_corpora.csv`) que alimenta de forma dinâmica os scripts de sequenciação e correlação.

---

## ✍️ Como Citar

Se utilizar este código ou metodologia na sua investigação, por favor cite a tese de doutoramento original ou o repositório arquivado no Zenodo:

* **Tese:** Magalhães, M. (2025). *O Comentário: da linguística do texto ao text mining*. Tese de Doutoramento, Universidade Nova de Lisboa / Faculdade de Ciências Sociais e Humanas.
* **Software (DOI):** https://doi.org/10.5281/zenodo.20764207
