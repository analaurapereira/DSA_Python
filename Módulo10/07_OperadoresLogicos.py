'''
Operadores Lógicos Para Manipulação de Dados com Pandas

Os operadores lógicos são excelentes para filtrar dataframes e retornar exatamente os dados que precisamos 
para nosso trabalho. Para conhecer mais sobre as regras dos operadores lógicos, acesse aqui:

https://pt.wikipedia.org/wiki/Operador_l%C3%B3gico

Primeiro usaremos o operador lógico AND para checar duas condições. Serão retornados os registros quando 
as duas condições forem verdadeiras.
'''

import pandas as pd

# Primeiro importamos um dataset
dsa_df = pd.read_csv("Módulo10/dataset.csv")

# Filtrando as vendas que ocorreram para o segmento de Home Office e na região South
dsa_df[ (dsa_df.Segmento == 'Home Office') & (dsa_df.Regiao == 'South') ].head()
# Filtrando as vendas que ocorreram para o segmento de Home Office ou região South
dsa_df[(dsa_df.Segmento == 'Home Office') | (dsa_df.Regiao == 'South')].tail()
# Filtrando as vendas que não ocorreram para o segmento de Home Office e nem na região South
dsa_df[(dsa_df.Segmento != 'Home Office') & (dsa_df.Regiao != 'South')].sample(5)