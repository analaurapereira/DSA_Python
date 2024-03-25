'''
A Linguagem SQL (Structured Query Language) é fundamental para profissionais de dados por várias razões:

Padrão Universal: SQL é uma linguagem padrão e amplamente aceita para gerenciamento e consulta de bancos de 
dados relacionais. Independentemente do sistema gerenciador de banco de dados (SGBD) utilizado, SQL é a 
linguagem comum para realizar consultas e manipulações de dados.

Flexibilidade: SQL permite criar consultas complexas e personalizadas, combinando dados de várias tabelas, 
filtrando informações e realizando operações de agregação e ordenação. Isso permite que os profissionais 
de dados extraiam informações valiosas a partir dos dados armazenados.

Manipulação de Dados: Além das consultas, SQL permite a inserção, atualização e exclusão de dados, bem como 
a definição de esquemas e gerenciamento de objetos de banco de dados, como tabelas, índices e visões.
Controle de Acesso e Segurança: SQL também oferece recursos para gerenciar o acesso e a segurança dos dados, 
permitindo aos profissionais de dados controlar quem pode acessar, modificar ou excluir informações no banco 
de dados.

Alta Demanda no Mercado: Profissionais de dados com habilidades em SQL estão em alta demanda, já que a 
linguagem é amplamente usada em várias áreas e setores. O conhecimento em SQL é uma habilidade essencial 
para cargos como Analista de Dados, Cientista de Dados, Engenheiro de Dados e Administrador de Banco de 
Dados.

Integração com Outras Ferramentas e Tecnologias: SQL se integra facilmente com outras ferramentas e 
linguagens de programação, como Python, R, Java, entre outras. Isso permite que os profissionais de 
dados aproveitem o poder da Linguagem SQL em conjunto com outras tecnologias para analisar, visualizar 
e processar dados.
'''
import sqlite3
import pandas as pd

# Conecta no banco de dados
con = sqlite3.connect('Módulo12/cap12_dsa.db')
# Abre um cursor para percorrer os dados no banco de dados
cursor = con.cursor()
# Query SQL para extrair os nomes das colunas no banco de dados
sql_query = """SELECT name FROM sqlite_master WHERE type = 'table';"""
# Visualiza o resultado
print(cursor.fetchall())
# Cria uma instrução SQL
query1 = 'SELECT * FROM tb_vendas_dsa'
# Executa a query no banco de dados
cursor.execute(query1)
# List comprehension para visualizar os nomes das colunas
nomes_colunas = [description[0] for description in cursor.description]
# Visualiza o resultado
print(nomes_colunas)
# Retorna os dados da execução da query
dados = cursor.fetchall()
print(dados)
# Fecha o cursor e encerra a conexão
cursor.close()
con.close()