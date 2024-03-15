# Isso é um dicionário
estudantes = {"Pedro":24, "Ana":22, "Ronaldo":26, "Janaina":25}
len(estudantes)
# primeiro valor é a chave
estudantes.keys()
# segundo valor é o valor
estudantes.values()
estudantes.items()

estudantes2 = {"Camila":27, "Adriana":28, "Roberta":26}
# concatena as listas
estudantes.update(estudantes2)

# Dicionário de listas
dict3 = {'chave1':1230, 'chave2':[22,453,73.4], 'chave3':['picanha', 'fraldinha', 'alcatra']}
# Acessando um item da lista, dentro do dicionário
dict3['chave3'][0].upper()
# Operações com itens da lista, dentro do dicionário
var1 = dict3['chave2'][0] - 2
# Duas operações no mesmo comando, para atualizar um item dentro da lista
dict3['chave2'][0] -= 2

# Criando Dicionários Aninhados
# Criando dicionários aninhados
dict_aninhado = {'key1':{'key2_aninhada':{'key3_aninhada':'Dict aninhado em Python'}}}
dict_aninhado['key1']['key2_aninhada']['key3_aninhada']