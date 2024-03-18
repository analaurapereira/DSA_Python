'''
Split de Strings em DataFrames do Pandas
Com Pandas podemos realizar diversas tarefas de split de strings dividindo uma coluna ou extraindo 
elementos do nosso interesse. 
'''

import pandas as pd

# Primeiro importamos um dataset
dsa_df = pd.read_csv("Módulo10/dataset.csv")
dsa_df['ID_Pedido'].head()
'''
Este é o formato dos dados da coluna "ID_Pedido":

CA-2016-152156
US-2015-108966
Temos o país, o ano e o id do pedido. Vamos dividir essa coluna e extrair o ano para gravar 
em uma nova coluna:
'''

# Split da coluna pelo caracter '-'
dsa_df['ID_Pedido'].str.split('-')
# Observe que o resultado são as listas em Python. Para extrair o ano precisamos especificar o índice 
# da posição que queremos extrair (em nosso caso a posição 2, logo, índice 1 em Python):
dsa_df['ID_Pedido'].str.split('-').str[1].head()
# Fazemos o split da coluna e extraímos o item na posição 2 (índice 1)
dsa_df['Ano'] = dsa_df['ID_Pedido'].str.split('-').str[1]
# Então conferimos a nova coluna criada
dsa_df.head()

########################## Strip de Strings em DataFrames do Pandas #######################
# O Split divide a string. O Strip remove caracteres da string.

dsa_df['Data_Pedido'].head(3)

'''
A coluna 'Data_Pedido' é a data de envio do produto no formato YYYY-MM-DD. Imagine que seja necessário 
deixar o ano apenas com 2 dígitos sem alterar o tipo da variável. Fazemos isso com a função lstrip(), 
ou seja, left strip.
'''
# Vamos remover os dígitos 2 e 0 à esquerda do valor da variável 'Data_Pedido'
dsa_df['Data_Pedido'].str.lstrip('20')

#Como não usamos o inplace = True a mudança é somente na memória e não altera o dataframe. Podemos usar 
# ainda as funções rstrip() e strip() com diferentes variações de strip de strings.
dsa_df['Data_Pedido'].head(3)