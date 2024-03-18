# Usando NumPy e Pandas Para Manipulação de Dados

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

# Resumo estatístico do Dataframe
df2.describe()
# Importando o NumPy
import numpy as np

# Usando o NumPy para alimentar uma das colunas do dataframe
df2['Taxa Crescimento'] = np.arange(5.)