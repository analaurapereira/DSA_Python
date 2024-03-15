'''
Função Enumerate
A função enumerate() em Python é uma função que permite iterar sobre uma estrutura de dados 
(como uma lista, tupla ou outro objeto iterável). A função enumerate() retorna um objeto enumerado,
que pode ser usado em loops para percorrer a estrutura de dados e acessar o contador e o valor de 
cada elemento.
'''

# Criando uma lista
seq = ['a','b','c']
list(enumerate(seq))

# Imprimindo os valores de uma lista com a função enumerate() e seus respectivos índices
for indice, valor in enumerate(seq):
    print (indice, valor)

for indice, valor in enumerate(seq):
    if indice >= 2:
        break
    else:
        print (valor)

lista = ['Marketing', 'Tecnologia', 'Business']
for i, item in enumerate(lista):
    print(i, item)