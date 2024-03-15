'''
Manipulando Arquivos TXT
TXT é a extensão de arquivo para arquivos de texto puro. Um arquivo TXT é um arquivo de texto simples 
sem formatação, como negrito, itálico ou fontes diferentes. Ele pode ser aberto e editado com muitos 
aplicativos diferentes, incluindo editores de texto, processadores de texto e IDEs. Arquivos TXT são 
amplamente utilizados para armazenar dados de texto simples, como listas, notas e documentos de texto. 
Eles são universais e podem ser lidos em praticamente qualquer dispositivo ou sistema operacional.
'''

texto = "Cientista de Dados pode ser uma excelente alternativa de carreira.\n"
texto = texto + "Esses profissionais precisam saber como programar em Python.\n"
texto += "E, claro, devem ser proficientes em Data Science."
print(texto)

# Importando o módulo os
import os
# Criando um arquivo 
arquivo = open(os.path.join('arquivos/cientista.txt'),'w')
# Gravando os dados no arquivo
for palavra in texto.split():
    arquivo.write(palavra + ' ')
# Fechando o arquivo
arquivo.close()
# Lendo o arquivo
arquivo = open('arquivos/cientista.txt','r')
conteudo = arquivo.read()
arquivo.close()
print(conteudo)

################################## Usando a Expressão with ###############################
# O método close() é executado automaticamente.

with open('arquivos/cientista.txt','r') as arquivo:
    conteudo = arquivo.read()

with open('arquivos/cientista.txt','w') as arquivo:
    arquivo.write(texto[:19])
    arquivo.write('\n')
    arquivo.write(texto[28:66])

'''
Manipulando Arquivos CSV
CSV (Comma-Separated Values) é um formato de arquivo que armazena dados tabulares em formato de texto plano. 
Cada linha do arquivo CSV representa uma linha da tabela e as colunas são separadas por vírgulas. 
É amplamente utilizado para exportar e importar dados em diferentes aplicações, como planilhas e banco 
de dados. CSV é uma opção simples e universal para compartilhar dados, pois pode ser aberto e editado 
com muitos aplicativos diferentes, incluindo programas de planilha e editores de texto.
'''

# Importando o módulo csv
import csv

with open('arquivos/numeros.csv','w') as arquivo:
    
    # Cria o objeto de gravação
    writer = csv.writer(arquivo)
    
    # Grava no arquivo linha a linha
    writer.writerow(('nota1', 'nota2', 'nota3'))
    writer.writerow((63,87,92)) 
    writer.writerow((61,79,76))
    writer.writerow((72,64,91))

with open('arquivos/numeros.csv','w') as arquivo:
    
    # Cria o objeto de gravação
    writer = csv.writer(arquivo)
    
    # Grava no arquivo linha a linha
    writer.writerow(('nota1', 'nota2', 'nota3'))
    writer.writerow((63,87,92)) 
    writer.writerow((61,79,76))
    writer.writerow((72,64,91))

# Gerando uma lista com dados do arquivo csv
with open('arquivos/numeros.csv','r') as arquivo:
    leitor = csv.reader(arquivo)
    dados = list(leitor)

# Impriminfo a partir da segunda linha
for linha in dados[1:]:
    print(linha)

'''
Manipulando Arquivos JSON (Java Script Object Notation )
JSON (JavaScript Object Notation) é um formato de dados de texto simples e leve que é utilizado para 
transmitir informações em aplicações web. É baseado em uma estrutura de objetos JavaScript e usa pares 
de chave-valor para representar dados. JSON é facilmente lido e escrito por máquinas e é amplamente 
utilizado como formato de intercâmbio de dados em aplicações web modernas.
'''

# Criando um dicionário
dict_guido = {'nome': 'Guido van Rossum',
              'linguagem': 'Python',
              'similar': ['c','Modula-3','lisp'],
              'users': 1000000}

for k,v in dict_guido.items():
    print (k,v)

# Importando o módulo JSON
import json
# Convertendo o dicionário para um objeto json
json.dumps(dict_guido)
# Criando um arquivo Json
with open('arquivos/dados.json','w') as arquivo:
    arquivo.write(json.dumps(dict_guido))
# Leitura de arquivos Json
with open('arquivos/dados.json','r') as arquivo:
    texto = arquivo.read()
    dados = json.loads(texto)

################################## Extração de Arquivo da Web ##################################
    
# Imprimindo um arquivo JSON copiado da internet
from urllib.request import urlopen

response = urlopen("http://vimeo.com/api/v2/video/57733101.json").read().decode('utf8')
dados = json.loads(response)[0]

print ('Título: ', dados['title'])
print ('URL: ', dados['url'])
print ('Duração: ', dados['duration'])
print ('Número de Visualizações: ', dados['stats_number_of_plays'])

# Nomes dos arquivos
arquivo_fonte = 'arquivos/dados.json'
arquivo_destino = 'arquivos/dados.txt'
# Método 1
with open(arquivo_fonte,'r') as infile:
    text = infile.read()
    with open(arquivo_destino,'w') as outfile:
        outfile.write(text)  

# Método 2
open(arquivo_destino,'w').write(open(arquivo_fonte,'r').read()) 

# Leitura do arquivo txt
with open('arquivos/dados.txt','r') as arquivo:
    texto = arquivo.read()
    dados = json.loads(texto)