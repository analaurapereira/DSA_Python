'''
Replace de Strings em DataFrames do Pandas
Se for necessário substituir caracteres dentro de uma string o Pandas oferece uma função para isso também.
'''

import pandas as pd

# Primeiro importamos um dataset
dsa_df = pd.read_csv("Módulo10/dataset.csv")
dsa_df['ID_Pedido'].head()
# Substituímos os caracteres CG por AX na coluna 'ID_Cliente'
dsa_df['ID_Cliente'] = dsa_df['ID_Cliente'].str.replace('CG', 'AX')