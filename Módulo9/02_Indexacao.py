import numpy as dsa

# Array criado a partir de uma lista Python
arr1 = dsa.array([10, 21, 32, 43, 48, 15, 76, 57, 89])

# Imprimindo um elemento específico no array
arr1[4] 

# Indexação
arr1[1:4] 

# Cria uma lista de índices
indices = [1, 2, 5, 6]

# Imprimindo os elementos dos índices
arr1[indices] 

# Cria uma máscara booleana para os elementos pares
mask = (arr1 % 2 == 0)

# Alterando um elemento do array
arr1[0] = 100

# Não é possível incluir elemento de outro tipo
try:
    arr1[0] = 'Novo elemento'
except:
    print("Operação não permitida!")