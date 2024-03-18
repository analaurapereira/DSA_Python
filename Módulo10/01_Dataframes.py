# Manipulando Dados em DataFrames do Pandas

import pandas as pd

# Cria um dicionário
dados = {'Estado': ['Santa Catarina', 'Rio de Janeiro', 'Tocantins', 'Bahia', 'Minas Gerais'], 
         'Ano': [2004, 2005, 2006, 2007, 2008], 
         'Taxa Desemprego': [1.5, 1.7, 1.6, 2.4, 2.7]}
print(dados)
# Importa a função DataFrame do Pandas
from pandas import DataFrame
# Converte o dicionário em um dataframe
df = DataFrame(dados)
# Visualiza as 5 primeiras linhas
print(df.head())
# Reorganizando as colunas
DataFrame(dados, columns = ['Estado', 'Taxa Desemprego', 'Ano'])
# Criando outro dataframe com os mesmo dados anteriores mas adicionando uma coluna
df2 = DataFrame(dados, 
                columns = ['Estado', 'Taxa Desemprego', 'Taxa Crescimento', 'Ano'], 
                index = ['estado1', 'estado2', 'estado3', 'estado4', 'estado5'])
# Imprimindo apenas uma coluna do Dataframe
df2['Estado']
# Imprimindo apenas duas colunas do Dataframe
df2[ ['Taxa Desemprego', 'Ano'] ]
# Filtrando pelo índice
df2.filter(items = ['estado3'], axis = 0)