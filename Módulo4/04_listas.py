# Criando uma lista
lista= ["arroz, frango, tomate, leite"]
# Atribuindo cada valor da lista a uma variável.
item1 = lista[0]
item2 = lista[1]
item3 = lista[2]
# Atualizando um item da lista
lista[2] = "chocolate"
# Deletando um item específico da lista
del lista[3]

#Listas de Listas (Listas Aninhadas)
# Criando uma lista de listas
listas = [ [1,2,3], [10,15,14], [10.1,8.7,2.3] ]
a = listas[0]
b = a[0]

# Operador in
# Criando uma lista
lista_teste_op = [100, 2, -5, 3.4]
# Verificando se o valor 10 pertence a lista
print(10 in lista_teste_op)

# Funções Built-in
# Criando uma lista
lista_numeros = [10, 20, 50, -3.4]
# Função len() retorna o comprimento da lista
len(lista_numeros)
# Função max() retorna o valor máximo da lista
max(lista_numeros)
# Função min() retorna o valor mínimo da lista
min(lista_numeros)
# Adicionando um item à lista
lista_numeros.append(9)

new_list = []
old_list = [1,2,5,10]
# Copiando os itens de uma lista para outra
for item in old_list:
    new_list.append(item)

# Reverte a lista
lista_numeros.reverse()
# Ordena a lista
lista_numeros.sort()