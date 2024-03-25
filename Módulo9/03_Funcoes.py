import numpy as dsa
# A função array() cria um array NumPy
arr2 = dsa.array([1, 2, 3, 4, 5])

# Usando métodos do array NumPy
arr2.cumsum() # Soma acumulada

arr2.cumprod() # Produto acumulado

# A função arange cria um array NumPy contendo uma progressão aritmética a partir de um intervalo - start, stop, step
arr3 = dsa.arange(0, 50, 5)

# Formato do array
dsa.shape(arr3)

# Cria um array preenchido com zeros
arr4 = dsa.zeros(10)

# Retorna 1 nas posições em diagonal e 0 no restante
arr5 = dsa.eye(3)

# Os valores passados como parâmetro, formam uma diagonal
arr6 = dsa.diag(dsa.array([1, 2, 3, 4]))

# Array de valores booleanos
arr7 = dsa.array([True, False, False, True])

# Array de strings
arr8 = dsa.array(['Linguagem Python', 'Linguagem R', 'Linguagem Julia'])

'''
A função linspace() do NumPy é usada para criar uma sequência de números igualmente espaçados dentro de 
um intervalo especificado. Essa função é amplamente utilizada em programação científica e matemática para
gerar arrays de números para diversos fins, como gráficos, cálculos e simulações.

O método linspace (linearly spaced vector) retorna um número de valores igualmente distribuídos no intervalo
especificado.
'''

print(dsa.linspace(0, 10))
print(dsa.linspace(0, 10, 15))

'''
A função logspace() do NumPy é usada para criar uma sequência de números igualmente espaçados em escala 
logarítmica dentro de um intervalo especificado. Essa função é amplamente utilizada em programação 
científica e matemática para gerar arrays de números para diversos fins, como gráficos, cálculos e 
simulações.
'''
print(dsa.logspace(0, 5, 10))