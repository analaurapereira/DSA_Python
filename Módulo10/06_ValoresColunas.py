'''
Verificando a Ocorrência de Diversos Valores em Uma Coluna

Em nosso conjunto de dados de exemplo temos a coluna Quantidade que representa a quantidade de itens 
vendidos em cada uma das vendas. Imagine que precisamos saber em quais vendas foram vendidos 5, 7, 9 
ou 11 itens.

Como aplicaríamos esse tipo de filtro ao nosso dataframe?

Fácil. O Pandas oferece o método isin() para checar diversos valores em uma coluna. Quem conhece Linguagem 
SQL já deve ter percebido que o método é o mesmo que a cláusula IN em SQL. 
'''

import pandas as pd
from pandas import DataFrame

# Primeiro importamos um dataset
dsa_df = pd.read_csv("Módulo10/dataset.csv")
dsa_df.shape
# Então aplicamos o filtro
dsa_df[dsa_df['Quantidade'].isin([5,7,9,11])]
'''
Na instrução acima estamos filtrando o dataframe chamado df, retornando todas as linhas onde a coluna 
Quantidade for igual aos valores 5, 7, 9 ou 11. Passamos uma lista de valores como argumento para o método 
isin().

Vamos deixar um pouquinho mais divertido. Se você executou a instrução acima, percebeu que foram retornadas 
2.128 linhas. E se quisermos retornar somente 10 linhas? É só fatiar o resultado assim:
'''

# Shape
dsa_df[dsa_df['Quantidade'].isin([5,7,9,11])].shape

dsa_df[dsa_df['Quantidade'].isin([5,7,9,11])][:10]