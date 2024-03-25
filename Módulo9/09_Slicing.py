import numpy as dsa
# Cria um array
arr22 = dsa.diag(dsa.arange(3))
arr22[1] # Retorna a linha de indice 1
arr22[:,2] # Retorna a coluna de indice 2

arr23 = dsa.arange(10)
# [start:end:step]
arr23[2:9:3] 

# Cria 2 arrays
a = dsa.array([1, 2, 3, 4])
b = dsa.array([4, 2, 2, 4])
# Comparação item a item
a == b
# Comparação global
dsa.array_equal(arr22, arr23)
# Menor valor
arr23.min()
# Maior valor 
arr23.max()
# Somando um valor a cada elemento do array
dsa.array([1, 2, 3]) + 1.5

# Cria um array
arr24 = dsa.array([1.2, 1.5, 1.6, 2.5, 3.5, 4.5])
# Usando o método around
arr25 = dsa.around(arr24)

# Criando um array
arr26 = dsa.array([[1, 2, 3, 4], [5, 6, 7, 8]])
'''
O método flatten() com NumPy é usado para criar uma cópia unidimensional (ou "achatada") de um array 
multidimensional. Isso significa que o método cria um novo array unidimensional, que contém todos os 
elementos do array multidimensional original, mas que está organizado em uma única linha. A ordem dos 
elementos no novo array unidimensional segue a ordem dos elementos no array multidimensional original.
'''
# "Achatando" a matriz
arr27 = arr26.flatten()

# Criando um array
arr28 = dsa.array([1, 2, 3])
# Repetindo os elementos de um array
dsa.repeat(arr28, 3) # array([1, 1, 1, 2, 2, 2, 3, 3, 3])
# Repetindo os elementos de um array
dsa.tile(arr28, 3) # array([1, 2, 3, 1, 2, 3, 1, 2, 3])

# Criando um array
arr29 = dsa.array([5, 6])
# Criando cópia do array
arr30 = dsa.copy(arr29)