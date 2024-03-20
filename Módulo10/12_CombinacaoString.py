'''
Combinação de Strings em DataFrames do Pandas
A função cat() pode ser usada para concatenar strings em um dataframe do Pandas.
'''

import pandas as pd

# Primeiro importamos um dataset
dsa_df = pd.read_csv("Módulo10/dataset.csv")
dsa_df['ID_Pedido'].head()

# Concatenando strings
dsa_df['Pedido_Segmento'] = dsa_df['ID_Pedido'].str.cat(dsa_df['Segmento'], sep = '-')