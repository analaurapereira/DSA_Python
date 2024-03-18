import pandas as pd
dados = {'Estado': ['Santa Catarina', 'Rio de Janeiro', 'Tocantins', 'Bahia', 'Minas Gerais'], 
         'Ano': [2004, 2005, 2006, 2007, 2008], 
         'Taxa Desemprego': [1.5, 1.7, 1.6, 2.4, 2.7]}
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

df2['estado2':'estado4'] # Do estado 2 ao 4
df2[ df2['Taxa Desemprego'] < 2 ] # Colchetes porque quer apenas um pedaço
df2['Taxa Crescimento'] # Apenas uma coluna, um colchete
df2[['Estado', 'Taxa Crescimento']] # Duas ou mais colunas, dois colchetes
df2[['Estado', 'Taxa Crescimento', 'Ano']]