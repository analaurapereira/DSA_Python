'''
Com o Pandas criamos dataframes, que são essencialmente tabelas. Como tal, podemos fazer consultas, 
ou simplesmente queries. E para isso usamos o método query(). Veja o exemplo abaixo:
'''

import pandas as pd
from pandas import DataFrame

# Primeiro importamos um dataset
dsa_df = pd.read_csv("Módulo10/dataset.csv")
# Checamos os valores mínimo e máximo da coluna Valor_Venda
dsa_df.Valor_Venda.describe()
# Geramos um novo dataframe apenas com o intervalo de vendas entre 229 e 10000
df2 = dsa_df.query('229 < Valor_Venda < 10000')
# Então confirmamos os valores mínimo e máximo
df2.Valor_Venda.describe()

# Geramos um novo dataframe apenas com os valores de venda acima da média
df3 = df2.query('Valor_Venda > 766')