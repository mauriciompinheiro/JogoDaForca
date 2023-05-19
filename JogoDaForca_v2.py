import random
from os import system, name


def homem_na_forca(chances):
    estagios = [
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        """,
        """
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        """
    ]
    return estagios[chances]


def game():
    print("Bem vindo ao jogo da forca!")
    print("Adivinhe a palavra abaixo:\n")

    palavras = ['banana', 'abacate', 'uva', 'morango', 'laranja']
    palavra = random.choice(palavras)
    lista_letras_palavras = [letra for letra in palavra]
    tabuleiro = ["_"] * len(palavra)
    chances = 6
    letras_tentativas = []

    while chances > 0:
        print(homem_na_forca(chances))
        print("Palavra: ", tabuleiro)
        print("\n")

        tentativa = input("\nDigite uma letra: ")

        if tentativa in letras_tentativas:
            print("Você já tentou essa letra. Escolha outra!")
            continue

        letras_tentativas.append(tentativa)

        if tentativa in lista_letras_palavras:
            print("Você acertou a letra!")
            for indice in range(len(lista_letras_palavras)):
                if lista_letras_palavras[indice] == tentativa:
                    tabuleiro[indice] = tentativa
            if "_" not in tabuleiro:
                print("\nVocê venceu! A palavra era: {}".format(palavra))
                break
        else:
            print("Ops. Essa letra não está na palavra!")
            chances -= 1

    if "_" in tabuleiro:
        print("\nVocê perdeu! A palavra era: {}.".format(palavra))


game()
