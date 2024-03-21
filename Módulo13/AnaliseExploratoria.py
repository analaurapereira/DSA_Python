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
# Função para converter os dados em valor absoluto
def autopct_format(values): 
    def my_format(pct): 
        total = sum(values) 
        val = int(round(pct * total / 100.0))
        return ' $ {v:d}'.format(v = val)
    return my_format

plt.figure(figsize=(20,10))
plt.pie(p5 = ['Valor_Venda'],  labels = p5['Segmento'], autopct=autopct_format(p5['Valor_Venda']))
plt.annotate(text = 'Total de Vendas: ' + '$ ' + str(int(sum(p5['Valor_Venda']))), xy = (-0.25, 0))
plt.title('Total de Vendas Por Segmento')
plt.show()

# Pergunta de Negócio 6 :
# Qual o Total de Vendas Por Segmento e Por Ano?

df_dsa['Data_Pedido'] = pd.to_datetime(df_dsa['Data_Pedido'], dayfirst = True)
df_dsa['Ano'] = df_dsa['Data_Pedido'].dt.year
p6 = df_dsa.groupby(['Ano', 'Segmento'])['Valor_Venda'].sum()

# Pergunta de Negócio 7 :
# Os gestores da empresa estão considerando conceder diferentes faixas de descontos e gostariam de fazer 
# uma simulação com base na regra abaixo:
# Se o Valor_Venda for maior que 1000 recebe 15% de desconto.
# Se o Valor_Venda for menor que 1000 recebe 10% de desconto.

df_dsa['Desconto'] = np.where(df_dsa['Valor_Venda'] > 1000, 0.15, 0.10)
df_dsa['Desconto'].value_counts()

# Pergunta de Negócio 8 :
# Considere Que a Empresa Decida Conceder o Desconto de 15% do Item Anterior. Qual Seria a Média do Valor 
# de Venda Antes e Depois do Desconto?

df_dsa['Valor_Venda_Desconto'] = df_dsa['Valor_Venda'] - (df_dsa['Valor_Venda'] * df_dsa['Desconto'])
p8_vendas_antes_desconto = df_dsa.loc[df_dsa['Desconto'] == 0.15, 'Valor_Venda']
p8_vendas_depois_desconto = df_dsa.loc[df_dsa['Desconto'] == 0.15, 'Valor_Venda_Desconto']
media_vendas_antes_desconto = p8_vendas_antes_desconto.mean()
media_vendas_depois_desconto = p8_vendas_depois_desconto.mean()

# Pergunta de Negócio 9 :
# Qual o Média de Vendas Por Segmento, Por Ano e Por Mês?

df_dsa['Mes'] = df_dsa['Data_Pedido'].dt.month
p9 = df_dsa.groupby(['Ano', 'Mes', 'Segmento'])['Valor_Venda'].agg([np.sum, np.mean, np.median])
anos = p9.index.get_level_values(0)
meses = p9.index.get_level_values(1)
segmentos = p9.index.get_level_values(2)

plt.figure(figsize = (20, 10))
sns.set_theme()
fig1 = sns.relplot(kind = 'line',
                   data = p9, 
                   y = 'mean', 
                   x = meses,
                   hue = segmentos, 
                   col = anos,
                   col_wrap = 4)
plt.show()

# Pergunta de Negócio 10 :
# Qual o Total de Vendas Por Categoria e SubCategoria, Considerando Somente as Top 12 SubCategorias?

p10 = df_dsa.groupby(['Categoria',
                        'SubCategoria']).sum(numeric_only = True).sort_values('Valor_Venda',
                                                                                ascending = False).head(12)
p10 = p10[['Valor_Venda']].astype(int).sort_values(by = 'Categoria').reset_index()
p10_cat = p10.groupby('Categoria').sum(numeric_only = True).reset_index()

cores_categorias = ['#5d00de',
                    '#0ee84f',
                    '#e80e27']

cores_subcategorias = ['#aa8cd4',
                       '#aa8cd5',
                       '#aa8cd6',
                       '#aa8cd7',
                       '#26c957',
                       '#26c958',
                       '#26c959',
                       '#26c960',
                       '#e65e65',
                       '#e65e66',
                       '#e65e67',
                       '#e65e68']

fig, ax = plt.subplots(figsize = (18,12))


p1 = ax.pie(p10_cat['Valor_Venda'], 
            radius = 1,
            labels = p10_cat['Categoria'],
            wedgeprops = dict(edgecolor = 'white'),
            colors = cores_categorias)

p2 = ax.pie(p10['Valor_Venda'],
            radius = 0.9,
            labels = p10['SubCategoria'],
            autopct = autopct_format(p10['Valor_Venda']),
            colors = cores_subcategorias, 
            labeldistance = 0.7,
            wedgeprops = dict(edgecolor = 'white'), 
            pctdistance = 0.53,
            rotatelabels = True)

fig = plt.gcf()
plt.annotate(text = 'Total de Vendas: ' + '$ ' + str(int(sum(p10['Valor_Venda']))), xy = (-0.2, 0))
plt.title('Total de Vendas Por Categoria e Top 12 SubCategorias')
plt.show()