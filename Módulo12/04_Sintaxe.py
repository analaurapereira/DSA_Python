# Sintaxe SQL x Sintaxe Pandas
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


# Sintaxe SQL
query5 = """SELECT Nome_Produto, AVG(Unidades_Vendidas) 
            FROM tb_vendas_dsa 
            WHERE Valor_Unitario > 199 
            GROUP BY Nome_Produto 
            HAVING AVG(Unidades_Vendidas) > 10"""

# Sintaxe Pandas
df[df['Valor_Unitario'] > 199].groupby('Nome_Produto') \
                              .filter(lambda x: x['Unidades_Vendidas'].mean() > 10) \
                              .groupby('Nome_Produto')['Unidades_Vendidas'].mean()