# Definindo uma função - 3 linhas de código
def potencia(num):
    resultado = num ** 2
    return resultado

# Definindo uma função - 2 linhas de código
def potencia(num):
    return num ** 2

# Definindo uma função - 1 linha de código
def potencia(num): return num ** 2

# Definindo uma expressão lambda (função anônima)
potencia = lambda num: num ** 2

# Lembre: operadores de comparação retornam boolean: true or false
Par = lambda x: x%2==0

first = lambda s: s[0]
reverso = lambda s: s[::-1]
addNum = lambda x,y : x+y