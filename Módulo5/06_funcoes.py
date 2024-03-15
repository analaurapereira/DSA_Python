# Definindo uma função
def primeiraFunc():
    print('Hello World')

# Definindo uma função
def primeiraFunc():
    nome = 'Bob'
    print('Hello %s' %(nome))

# Definindo uma função com parâmetro
def segundaFunc(nome):
    print('Hello %s' %(nome))
segundaFunc('Aluno')

# Função para imprimir números
def imprimeNumeros():
    
    # Loop
    for i in range(0, 5):
        print("Número " + str(i))
imprimeNumeros()

# Funções com número variável de argumentos
def printVarInfo( arg1, *vartuple ):
    
   # Imprimindo o valor do primeiro argumento
    print ("O parâmetro passado foi: ", arg1)
   
   # Imprimindo o valor do segundo argumento 
    for item in vartuple:
        print ("O parâmetro passado foi: ", item)
    return;
# Fazendo chamada à função usando apenas 1 argumento
printVarInfo(10)


# Escopo de Variável - Local e Global
# Variável Global
var_global = 10  # Esta é uma variável global
# Função
def multiplica_numeros(num1, num2):
    var_global = num1 * num2  # Esta é uma variável local
    print(var_global)
multiplica_numeros(5, 25)

# Variável Global
var_global = 10  # Esta é uma variável global
# Função
def multiplica_numeros(num1, num2):
    var_local = num1 * num2   # Esta é uma variável local
    print(var_local)

# Usando a função int para converter o valor digitado
idade = int(input("Digite sua idade: "))
if idade > 13:
    print("Você pode acessar Redes Sociais sem supervisão!")  
else:
    print("Seus pais não deveriam você acessar Redes Sociais sem supervisão!")  


# Criando Funções Usando Outras Funções
import math
# Verificando se um número é primo
def numPrimo(num):
    if (num % 2) == 0 and num > 2: 
        return "Este número não é primo"
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if (num % i) == 0:
            return "Este número não é primo"
    return "Este número é primo"

# Fazendo Split dos Dados
# Fazendo split dos dados
def split_string_palavras(text):
    return text.split(" ")
texto = "Esta função será bastante útil para separar grandes volumes de dados."
# Isso divide a string em uma lista de palavras
print(split_string_palavras(texto))
# Podemos atribuir o output de uma função para uma variável
token = split_string_palavras(texto)
# Fazendo split dos dados
def split_string_letras(text):
    texto = text.upper()
    for letra in texto:
        print(letra)
split_string_letras(texto)