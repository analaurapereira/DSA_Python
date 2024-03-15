# Projeto 1 - Desenvolvimento de Game em Linguagem Python - Versão 2

import random

def palavra(resposta, ad):

    r = " "

    for i in resposta:
        if i in ad:
            r = r + i

        else:
            r = r + " _ "

    return r

palavras = []

with open("Módulo7/palavras.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)


resposta = random.choice(palavras).upper()

tentativa = random.randint(6, 11)
ad = []
aux = 0

while tentativa > 0 and aux < len(resposta):

    print('\n----------------- Bem-vindo(a) ao jogo da forca -------------------------')

    p = palavra(resposta, ad)

    print(f'\n {p} \n')
    print(f'Tentativas restantes: {tentativa}\n')

    l = input("Letra: ").upper()

    if l in ad:
        print("Letra já escolhida. Tente novamente")

    else: 
        ad.append(l)

        if l in resposta:
            for i in resposta:
                if i == l:
                    aux = aux + 1
                    

        else:
            print("Letra incorreta. Tente novamente")
     
        tentativa = tentativa - 1


if tentativa == 0 and aux != len(resposta):
    print(f'Você perdeu. A palavra era {resposta}')

else:
    print(f'Você acertou a palavra {resposta}')