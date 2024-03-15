'''
Função Reduce
A função reduce() em Python é uma função da biblioteca functools que aplica uma determinada função binária 
a pares consecutivos de elementos em uma estrutura de dados iterável (como uma lista, tupla ou outro objeto
 iterável), reduzindo-a a um único valor.
'''

# Importando a função reduce do módulo functools
from functools import reduce
from IPython.display import Image
Image('arquivos/reduce.png')

# Criando uma lista
lista = [47, 11 , 42, 13]
# Função 
def soma(a,b):
    x = a + b
    return x
# Usando reduce com uma função e uma lista. A função vai retornar o valor máximo
reduce(soma, lista)
# Usando a função reduce() com lambda
reduce(lambda x,y: x+y, lista)

# Podemos atribuir a expressão lambda a uma variável
max_find2 = lambda a,b: a if (a > b) else b
# Reduzindo a lista até o valor máximo, através da função criada com a expressão lambda
reduce(max_find2, lista)