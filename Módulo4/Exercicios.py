# Exercício 1 - Imprima na tela os números de 1 a 10. Use uma lista para armazenar os números.
lista = [1,2,3,4,5,6,7,8,9,10]
print(lista)

# Exercício 2 - Crie uma lista de 5 objetos e imprima na tela
lista = ['chocolate', 'banana', 'abacaxi', 'uva', 'morango']
print(lista)

# Exercício 3 - Crie duas strings e concatene as duas em uma terceira string
frase1 = 'Se beber '
frase2 = 'não case!'
frase_final = frase1 + frase2
print(frase_final)

# Exercício 4 - Crie uma tupla com os seguintes elementos: 1, 2, 2, 3, 4, 4, 4, 5 e depois utilize a 
#função count do objeto tupla para verificar quantas vezes o número 4 aparece na tupla
tup1 = (1, 2, 2, 3, 4, 4, 4, 5)
tup1.count(4)

# Exercício 5 - Crie um dicionário vazio e imprima na tela
dict3 = {}
print(dict3)

# Exercício 6 - Crie um dicionário com 3 chaves e 3 valores e imprima na tela
dict = {'k1':'martelo', 'k2':'serrote', 'k3':'machado'}
print(dict)

# Exercício 7 - Adicione mais um elemento ao dicionário criado no exercício anterior e imprima na tela
dict['k4'] = 'parafuso'
print(dict)

# Exercício 8 - Crie um dicionário com 3 chaves e 3 valores. 
# Um dos valores deve ser uma lista de 2 elementos numéricos. 
# Imprima o dicionário na tela.
dict2 = {'chave1':'Geografia', 'chave2':'Biologia', 'chave3':[70, 90]}
print(dict2)

# Exercício 9 - Crie uma lista de 4 elementos. O primeiro elemento deve ser uma string, 
# o segundo uma tupla de 2 elementos, o terceiro um dcionário com 2 chaves e 2 valores e 
# o quarto elemento um valor do tipo float.
# Imprima a lista.
lst = ['String1', (90, 92), {'k1':'v1', 'k2':'v2'}, 99.98]
print(lst)

# Exercício 10 - Considere a string abaixo. Imprima na tela apenas os caracteres da posição 1 a 18.
frase = 'Cientista de Dados é o profissional mais sexy do século XXI'
frase[0:18]