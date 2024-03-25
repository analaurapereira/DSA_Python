import sqlite3
import pandas as pd

# Conecta no banco de dados
con = sqlite3.connect('Módulo12/cap12_dsa.db')
# Abre um cursor para percorrer os dados no banco de dados
cursor = con.cursor()
# Cria uma instrução SQL
query = 'SELECT * FROM tb_vendas_dsa'
# Executa a query no banco de dados
cursor.execute(query)
# Retorna os dados da execução da query
dados = cursor.fetchall()
# Carrega os dados como dataframe do Pandas
df = pd.DataFrame(dados, columns = ['ID_Pedido', 
                                    'ID_Cliente', 
                                    'Nome_Produto',
                                    'Valor_Unitario',
                                    'Unidades_Vendidas',
                                    'Custo'])

print(df.head())
# Fecha o cursor e encerra a conexão
cursor.close()
con.close()

# Calcula a média de unidades vendidas
media_unidades_vendidas = df['Unidades_Vendidas'].mean()
# Calcula a média de unidades vendidas por produto
media_unidades_vendidas_por_produto = df.groupby('Nome_Produto')['Unidades_Vendidas'].mean()
# Visualiza os 10 primeiros resultados
print(media_unidades_vendidas_por_produto.head(10))
#A query abaixo retorna a média de unidades vendidas por produto se o valor unitario for maior do que 199 
# e somente se a média de unidades vendidas for maior do que 10.

# Alternativa A
df[df['Valor_Unitario'] > 199].groupby('Nome_Produto').filter(lambda x: x['Unidades_Vendidas'].mean() > 10)
# Alternativa B
df[df['Valor_Unitario'] > 199].groupby('Nome_Produto') \
                              .filter(lambda x: x['Unidades_Vendidas'].mean() > 10) \
                              .groupby('Nome_Produto')['Unidades_Vendidas'].mean()