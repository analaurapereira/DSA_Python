# Condicional If (Se)
if 5 > 2:
    print("A sentença é verdadeira!")

# Condicional If...Else
if 5 < 2:
    print("A sentença é verdadeira!")
else:
    print("A sentença é falsa!")

# Condicional If...Else com variável
dia = "Terça"
if dia == "Segunda":
    print("Hoje fará sol!")
else:
    print("Hoje vai chover!")

# Podemos usar o operador elif para validar mais de uma condição
if dia == "Segunda":
    print("Hoje fará sol!")
elif dia == "Terça":
    print("Hoje vai chover!")
else:
    print("Sem previsão do tempo para o dia selecionado")

# Condicionais Aninhados
Nome = "Bob"
idade = 18

if idade > 13:
    if Nome == "Bob":
        print("Ok Bob, você está autorizado a entrar!")
    else:
        print("Desculpe, mas você não pode entrar!")

idade = 13
Nome = "Bob"
if idade >= 13 and Nome == "Bob":
    print("Ok Bob, você está autorizado a entrar!")

idade = 12
Nome = "Bob"
if (idade >= 13) or (Nome == "Bob"):
    print("Ok Bob, você está autorizado a entrar!")

'''
Os operadores lógicos funcionam assim:

Operador and - Retorna True se ambas as declarações forem verdadeiras.
Operador or - Retorna True se uma das declarações for verdadeira.
Operador not - Inverte o resultado, retorna False se o resultado for True.
'''