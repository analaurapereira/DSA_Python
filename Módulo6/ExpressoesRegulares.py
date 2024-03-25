'''
Neste  Lab  você  vai  aprender  como  usar  Expressões  Regulares  em  Python  ao  mesmo tempo que 
pratica um pouco mais o uso do ChatGPT.
Expressões Regulares são uma sequência de caracteres que definem uma busca padrão em strings.
Em Python, as Expressões Regulares são suportadas pelo pacotere. Ele fornece uma série de funções 
para pesquisar e substituir padrões em strings. Algumas das tarefas mais comuns que podem ser 
realizadas com Expressões Regulares incluem verificar se uma string corresponde a um determinado 
padrão, extrair informações de uma string combase em um padrão específico e substituir 
trechos de uma string com base em um padrão.
Por  exemplo,  você  pode usar  uma  expressão  regular  para  verificar  se  uma  string 
representa um endereço de e-mail válido, ou para encontrar todas as ocorrências de um padrão em uma string

Expressões Regulares
Expressões regulares são padrões usados para combinar ou encontrar ocorrências de sequências 
de caracteres em uma string. Em Python, expressões regulares são geralmente usadas para manipular 
strings e realizar tarefas como validação de entrada de dados, extração de informações de strings e
substituição de texto.
'''

import re #regular expression

texto = "Meu e-mail é alspereira99@gmail.com"
# Expressão regular para contar quantas vezes o caracter arroba aparece no texto
resultado = len(re.findall("@", texto))
# Expressão regular para extrair a palavra que aparece após a palavra "você" em um texto
resultado = re.findall(r'Meu (\w+)', texto)
# Expressão regular para extrair endereços de e-mail de uma string
emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', texto)

text = "O aluno estava incrivelmente perdido, mas encontrou a DSA e rapidamente começou a aprender."
# Extraindo os advérbios da frase
for m in re.finditer(r"\w+mente\b", text):
    print('%02d-%02d: %s' % (m.start(), m.end(), m.group(0)))

################### REGEX com ChatGPT ###########################
    
# Variável do tipo string
musica = '''
Todos os dias quando acordo
Não tenho mais
O tempo que passou
Mas tenho muito tempo
Temos todo o tempo do mundo
Todos os dias
Antes de dormir
Lembro e esqueço
Como foi o dia
Sempre em frente
Não temos tempo a perder
Nosso suor sagrado
É bem mais belo
Que esse sangue amargo
E tão sério
E selvagem! Selvagem!
Selvagem!
Veja o sol
Dessa manhã tão cinza
A tempestade que chega
É da cor dos teus olhos
Castanhos
Então me abraça forte
E diz mais uma vez
Que já estamos
Distantes de tudo
Temos nosso próprio tempo
Temos nosso próprio tempo
Temos nosso próprio tempo
Não tenho medo do escuro
Mas deixe as luzes
Acesas agora
O que foi escondido
É o que se escondeu
E o que foi prometido
Ninguém prometeu
Nem foi tempo perdido
Somos tão jovens
Tão jovens! Tão jovens!
'''

# 1- Crie um REGEX para contar quantas vezes o caracter "a" aparece em todo o texto da música.
resultado1 = len(re.findall("a", musica))
print("O caractere 'a' apareceu", resultado1, "vezes na música.")

# 2- Crie um REGEX em Python para contar quantas vezes a palavra tempo aparece na música.
resultado2 = len(re.findall("tempo", musica))
print("A palavra 'tempo' apareceu", resultado2, "vezes na música.")

# 3- Crie um REGEX em Python para extrair as palavras seguidas por exclamação.
resultado3 = re.findall(r'\b\w+!', musica)
print("Estas são as palavras seguidas por exclamação:", resultado3)

# 4- Crie um REGEX que extrai qualquer palavra cujo antecessor seja a palavra "esse" e 
# o sucessor seja a palavra "amargo" em um texto.
resultado4 = re.findall(r'\besse\s(\w+)\samargo\b', musica)
print("Palavra(s) encontrada(s):", resultado4)

# 5- Crie um REGEX que retorne as palavras com acento, mas somente os caracteres na palavra que 
# são anteriores ao caracter com acento.
resultado5 = re.findall(r'\b[\wÀ-ÿ]+[áéíóúãõç]', musica)
print("As palavras acentuadas são:", resultado5)