import numpy as dsa
arr15 = dsa.arange(1, 10)

# Soma dos elementos do array
dsa.sum(arr15)
# Retorna o produto dos elementos
dsa.prod(arr15)
# Soma acumulada dos elementos
dsa.cumsum(arr15)

# Cria 2 arrays
arr16 = dsa.array([3, 2, 1])
arr17 = dsa.array([1, 2, 3])
# Soma dos arrays
arr18 = dsa.add(arr16, arr17)  

'''
Para multiplicar duas matrizes NumPy, podemos usar a função dot() ou o operador @. Ambos os métodos executam 
a multiplicação matricial. É importante lembrar que, para que a multiplicação de matrizes possa ser 
executada, o número de colunas da primeira matriz deve ser igual ao número de linhas da segunda matriz.

Há várias formas de multiplicar elementos de matrizes NumPy. A função dot() é um método bastante utilizado.
'''

# Cria duas matrizes
arr19 = dsa.array([[1, 2], [3, 4]])
arr20 = dsa.array([[5, 6], [0, 7]])
# Multiplicar as duas matrizes
arr21 = dsa.dot(arr19, arr20)
# Multiplicar as duas matrizes
arr21 = arr19 @ arr20
# Multiplicar as duas matrizes
arr21 = dsa.tensordot(arr19, arr20, axes = ((1),(0)))