# Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt

# Carrega o dataset
df_dsa = pd.read_csv('Módulo13/dataset.csv')

# Amostra dos dados - inicio
df_dsa.head()
# Amostra dos dados - final
df_dsa.tail()

######### Análise Exploratória #########
# Colunas do conjunto de dados
df_dsa.columns
# Resumo estatístico da coluna com o valor de venda
df_dsa['Valor_Venda'].describe()
# Verificando se há registros duplicados
df_dsa[df_dsa.duplicated()]
# Verificando de há valores ausentes
df_dsa.isnull().sum()

# Pergunta de Negócio 1:
# Qual Cidade com Maior Valor de Venda de Produtos da Categoria 'Office Supplies'?
p1 = df_dsa[df_dsa['Categoria']=='Office Supplies']
p1_total = p1.groupby('Cidade')['Valor_Venda'].sum()
resposta = p1_total.idxmax()

# Pergunta de Negócio 2:
# Qual o Total de Vendas Por Data do Pedido?
# Demonstre o resultado através de um gráfico de barras.

p2 = df_dsa.groupby('Data_Pedido')['Valor_Venda'].sum()
plt.figure(figsize=(20, 10))
p2.plot(x = 'Data_Pedido', y = 'Valor_Venda', color = 'blue')
plt.title('Total de Vendas Por Data do Pedido')
plt.show()

# Pergunta de Negócio 3:
# Qual o Total de Vendas por Estado?
# Demonstre o resultado através de um gráfico de barras.
p3 = df_dsa.groupby('Estado')['Valor_Venda'].sum().reset_index()
plt.figure(figsize=(20,10))
sns.barplot(data = p3, x = 'Estado', y = 'Valor_Venda').set(title= 'Total de Vendas por Estado')
plt.xticks(rotation = 80) # Rotaciona a legenda
plt.show()

# Quais São as 10 Cidades com Maior Total de Vendas?
# Demonstre o resultado através de um gráfico de barras.
p4 = df_dsa.groupby('Cidade')['Valor_Venda'].sum().reset_index().sort_values(by = 'Valor_Venda', ascending = False).head(10)
plt.figure(figsize=(20,10))
sns.barplot(data = p4, x  ='Cidade', y ='Valor_Venda').set(title = '10 Cidades com Maior Total de Vendas')
plt.show()

# Pergunta de Negócio 5:
# Qual Segmento Teve o Maior Total de Vendas?
# Demonstre o resultado através de um gráfico de pizza.
p5 = df_dsa.groupby('Segmento')['Valor_Venda'].sum().reset_index().sort_values(by = 'Valor_Venda', ascending= False)
