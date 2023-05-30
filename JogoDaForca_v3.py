# Hangman Game (Jogo da Forca) 
# Programação Orientada a Objetos

import random

board = ['''

>>>>>>>>>> Hangman do Dev <<<<<<<<<<
>>>>>>> Descubra a Linguagem <<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


class Hangman:

    # Método Construtor
    def __init__(self, palavra):
        self.palavra = palavra
        self.letras_erradas = []
        self.letras_escolhidas = []

    # Método para adivinhar a letra
    def advinhar(self, letra):
        if letra in self.palavra and letra not in self.letras_escolhidas:
            self.letras_escolhidas.append(letra)
        elif letra not in self.palavra and letra not in self.letras_erradas:
            self.letras_erradas.append(letra)
        else:
            return False
        return True

    # Método para verificar se o jogo terminou
    def hangman_acabou(self):
        return self.hangman_venceu() or (len(self.letras_erradas) == 6)

    # Método para verificar se o jogador venceu
    def hangman_venceu(self):
        if '_' not in self.esconder_palavra():
            return True
        return False

    # Método para não mostrar a letra no board
    def esconder_palavra(self):
        rtn = ''
        for letra in self.palavra:
            if letra not in self.letras_escolhidas:
                rtn += '_'
            else:
                rtn += letra
        return rtn

    # Método para checar o status do game e imprimir o board na tela
    def mostrar_status_jogo(self):
        print(board[len(self.letras_erradas)])
        print('\nPalavra: ' + self.esconder_palavra())
        print('\nLetras erradas: ')
        for letra in self.letras_erradas:
            print(letra)
        print()
        print('Letras corretas: ')
        for letras in self.letras_escolhidas:
            print(letras)
        print()


# Método para escolher aleatoriamente uma palavra dentro de uma lista pré estabelecida
def palavra_aleatoria():
    palavras = ['python', 'java', 'golang', 'javascript', 'ruby']
    palavra = random.choice(palavras)
    return palavra

#
def main():
    game = Hangman(palavra_aleatoria())
    while not game.hangman_acabou():
        game.mostrar_status_jogo()
        usuario_input = input('\nDigite uma letra: ')
        game.advinhar(usuario_input)
    game.mostrar_status_jogo()
    if game.hangman_venceu():
        print('\nParabéns! Você venceu!')
    else:
        print('\nGame over! Você perdeu!')
        print('A palavra era ' + game.palavra)
    print('\nFoi bom jogar com você! Volte sempre, Dev!')


if __name__ == '__main__':
    main()
