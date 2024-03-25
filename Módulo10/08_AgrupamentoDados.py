'''
Agrupamento de Dados em DataFrames com Group By

A função Pandas Groupby é uma função versátil e fácil de usar que ajuda a obter uma visão geral dos dados. 
Isso torna mais fácil explorar o conjunto de dados e revelar os relacionamentos entre as variáveis.

O código a seguir agrupará as linhas com base nas combinações Segmento/Regiao/Valor_Venda e nos dará a taxa 
média de vendas de cada grupo.
'''

import pandas as pd

# Primeiro importamos um dataset
dsa_df = pd.read_csv("Módulo10/dataset.csv")
# Aplicamos o group by
dsa_df[['Segmento', 'Regiao', 'Valor_Venda']].groupby(['Segmento', 'Regiao']).mean()

'''
Na instrução acima, primeiro filtramos os dados extraindo 3 colunas: ['Segmento','Regiao','Valor_Venda']. 
Na sequência, agrupamos por duas colunas: ['Segmento','Regiao']. E então calculamos a média para a coluna 
que ficou foram do group by, nesse caso a coluna Sales.

O comportamento do group by com Pandas é o mesmo observado na Linguagem SQL.

Agregação Múltipla com Group By

Vamos explorar mais a função groupby() pois temos diversas opções de sumarização dos dados de forma simples. 
No exemplo abaixo uniremos a função groupby() com a função agg() para realiza agregação múltipla.
'''

# Aplicamos o group by
dsa_df[['Segmento', 'Regiao', 'Valor_Venda']].groupby(['Segmento', 'Regiao']).agg(['mean', 'std', 'count'])

'''
Na instrução acima, primeiro filtramos os dados extraindo 3 colunas: ['Segmento','Regiao','Valor_Venda']. 
Na sequência, agrupamos por duas colunas: ['Segmento','Regiao']. E então agregamos os dados calculando a 
média, desvio padrão e contagem de elementos para a coluna que ficou fora do group by, nesse caso a coluna 
Valor_Venda.

A função agg() recebe como argumento uma lista de funções para agregação.
'''