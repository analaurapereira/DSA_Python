'''
Função Zip
A função zip() em Python é uma função que agrupa elementos de múltiplas estruturas de dados iteráveis 
(como listas, tuplas ou outros objetos iteráveis) juntos em pares. A função zip() retorna um objeto zip,
 que pode ser convertido em outra estrutura de dados, como uma lista ou dicionário, se necessário.
'''

# Criando duas listas
x = [1,2,3]
y = [4,5,6]
# Unindo as listas. Em Python3 retorna um iterator
zip(x, y)
# Perceba que zip retorna tuplas. Neste caso, uma lista de tuplas
list(zip(x,y))
# Atenção quando as sequências tiverem número diferente de elementos(ele vai até quando a menor lista 
# terminar)
list(zip('ABCD', 'xy'))

# Criando 2 dicionários
d1 = {'a':1,'b':2}
d2 = {'c':4,'d':5}
# Zip vai unir as chaves
list(zip(d1,d2))
# Zip pode unir os valores (itens)
list(zip(d1, d2.values()))

# Criando uma função para trocar valores entre 2 dicionários
def trocaValores(d1, d2):
    
    dicTemp = {}
    
    for d1key, d2val in zip(d1, d2.values()):
        dicTemp[d1key] = d2val
    
    return dicTemp
trocaValores(d1, d2)