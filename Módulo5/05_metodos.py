'''
Métodos
Tudo em Python é objeto. E cada objeto tem métodos e atributos.

Atributos são propriedades, características do objeto.
Métodos são funções com ações que podem ser executadas nos objetos.
'''

# Criando uma lista
lista = [100, -2, 12, 65, 0]
# Usando um método do objeto lista
lista.append(100)
# Usando um método do objeto lista
lista.count(100)
# A função help() explica como utilizar cada método de um objeto
help(lista.count)
# A função dir() mostra todos os métodos e atributos de um objeto
dir(lista)

frase = 'Isso é uma string'
# O método de um objeto pode ser chamado dentro de uma função, como print()
print (frase.split())