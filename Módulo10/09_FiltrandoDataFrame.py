'''
Filtrando DataFrame do Pandas com Base em Strings
O Pandas oferece diversas funções para manipulação de strings. Começaremos com o filtros de strings com base 
nas letras iniciais e finais.
'''

import pandas as pd

# Primeiro importamos um dataset
dsa_df = pd.read_csv("Módulo10/dataset.csv")

# Filtramos o dataframe pela coluna Segmento com valores que iniciam com as letras 'Con'
dsa_df[dsa_df.Segmento.str.startswith('Con')].head()
dsa_df.Segmento.value_counts()
# Filtramos o dataframe pela coluna Segmento com valores que terminam com as letras 'mer'
dsa_df[dsa_df.Segmento.str.endswith('mer')].head()

#As funções startswith() e endswith() são muito úteis quando for necessário filtrar strings por caracteres 
# que apareçam no começo e/ou final.