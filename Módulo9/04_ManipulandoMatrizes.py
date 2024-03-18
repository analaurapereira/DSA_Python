import numpy as dsa
# Criando uma matriz
arr9 = dsa.array( [ [1,2,3] , [4,5,6] ] )  # [1 2 3 ]
                                           # [4 5 6 ]

print(arr9.shape) # (2,3)
# Criando uma matriz 2x3 apenas com números "1"
arr10 = dsa.ones((2,3))

# Lista de listas
lista = [[13,81,22], [0, 34, 59], [21, 48, 94]]
# A função matrix cria uma matriz a partir de uma lista de listas
arr11 = dsa.matrix(lista)
# Indexação da matriz
arr11[2,1] # 48
# Indexação da matriz
arr11[0:2,2]
# Indexação da matriz
arr11[1,]
# Alterando um elemento da matriz
arr11[1,0] = 100

x = dsa.array([1, 2])  # NumPy decide o tipo dos dado
y = dsa.array([1.0, 2.0])  # NumPy decide o tipo dos dado
z = dsa.array([1, 2], dtype = dsa.float64)  # Forçamos um tipo de dado em particular    

arr12 = dsa.array([[24, 76, 92, 14], [47, 35, 89, 2]], dtype = float)

'''
O itemsize de um array numpy é um atributo que retorna o tamanho em bytes de cada elemento do array. 
Em outras palavras, o itemsize representa o número de bytes necessários para armazenar cada valor do array 
numpy.
'''

arr12.itemsize # Tamanho por elemento
arr12.nbytes # Tomanho total
arr12.ndim # Número de dimensões