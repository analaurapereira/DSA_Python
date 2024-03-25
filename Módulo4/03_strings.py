# Indexando Strings
# Atribuindo uma string
s = 'Data Science Academy'
print(s)
# Primeiro elemento da string
s[0]

# Retorna todos os elementos da string, começando pela posição 
# (lembre-se que Python começa a indexação pela posição 0),
# até o fim da string.
s[1:]
# Retorna tudo até a posição de índice 3
s[:3]
# Nós também podemos usar a indexação negativa e ler de trás para frente
s[-1]
# Retornar tudo, exceto a última letra
s[:-1]

#podemos usar dois pontos duas vezes em uma linha e, em seguida, um número 
#que especifica a frequência para retornar elementos.
s[::2]
s[::-1]

# Propriedades de Strings
# Alterando um caracter (não é possível alterar um elemento da string)
s[0] = 'x'

# Concatenando strings
s + ' é a melhor maneira de estar preparado para o mercado de trabalho em Ciência de Dados!'
s = s + ' é a melhor maneira de estar preparado para o mercado de trabalho em Ciência de Dados!'

# Podemos usar o símbolo de multiplicação para criar repetição!
letra = 'w'
letra * 3

# Funções Built-in de Strings
# Upper Case 
s.upper()
# Lower case
s.lower()
# Dividir uma string por espaços em branco (padrão)
s.split()
# Dividir uma string por um elemento específico
s.split('y')

# Funções String
# A primeira letra fica maiuscula
s.capitalize()
# Conta quantas vezes aparece
s.count('a')

s.isalnum()
s.islower()
s.isspace()
s.endswith('o')