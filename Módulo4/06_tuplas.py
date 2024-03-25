# Criando uma tupla
tupla1 = ("Geografia", 23, "Elefantes", 9.8, 'Python')
# Tuplas não suportam append()
# Tuplas não suportam delete de um item específico
# Tuplas não suportam atribuição de item

# Slicing, da mesma forma que se faz com listas
tupla1[1:]
# Retorna a posição
tupla1.index('Elefantes')

# Criando uma tupla
t2 = ('A', 'B', 'C')
# Usando a função list() para converter uma tupla para lista
lista_t2 = list(t2)
# Usando a função tuple() para converter uma lista para tupla
t2 = tuple(lista_t2)