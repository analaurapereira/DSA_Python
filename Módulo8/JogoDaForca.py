# Projeto 2 - Desenvolvimento de Game em Linguagem Python utilizando POO

import random

class Hangman:
    def __init__(self, palavra):

        self.palavra = palavra
        self.letras_erradas = []
        self.letras_escolhidas = []

    def guess(self, letra):

        if letra in self.palavra and letra not in self.letras_escolhidas:
            self.letras_escolhidas.append(letra)

        elif letra not in self.palavra and letra not in self.letras_escolhidas:
            self.letras_erradas.append(letra)

        else:
            return False
        
        return True
    
    def hangman_over(self):

        return self.hangman_won() or len(self.letras_erradas) == 6
    
    def hangman_won(self):
        return all(letra in self.letras_escolhidas for letra in self.palavra)
    
    def hide_palavra(self):

        rtn = ''

        for letra in self.palavra:
            if letra not in self.letras_escolhidas:
                rtn += '_'

            else:
                rtn += letra

        return rtn
    
    def game_status(self):

        print('\nPalavra: ' + self.hide_palavra())
        print('\nLetras erradas: ' + ', '.join(self.letras_erradas))
        print('\nLetras corretas: ' + ', '.join(self.letras_escolhidas))

def rand_palavra():

    with open("Módulo8/palavras.txt", "r", encoding="utf-8") as arquivo:
        palavras = arquivo.readlines()
    return random.choice(palavras).strip()

def main():

    palavra = rand_palavra()
    game = Hangman(palavra)

    while not game.hangman_over():

        game.game_status()
        user_input = input('\nDigite uma letra: ').lower()
        game.guess(user_input)

    game.game_status()

    if game.hangman_won():

        print('\nParabéns, você venceu!!')

    else:
        print('\nVocê perdeu')
        print('A palavra era: ' + palavra)

if __name__ == "__main__":
    main()