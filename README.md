# JogoDaForca
 
Para desenvolver o jogo da forca em Python, nas duas versões, foram seguidos os passos abaixo:

1- Definição da lista de palavras possíveis

2- Escolha de uma palavra aleatória da lista

3- Criação de uma lista vazia para armazenar as letras adivinhadas

4- Definição do número máximo de tentativas permitidas

5- Criação da seguinte estrutura de repetição e condicional: 
5.1- Enquanto o número de tentativas não atingir o limite máximo:
a. Exibir a palavra como uma série de underscores, com as letras adivinhadas preenchidas nos espaços corretos
b. Pedir ao jogador que adivinhe uma letra
c. Verificar se a letra adivinhada está na palavra
d. Se a letra adivinhada está na palavra, adicionar a letra à lista de letras adivinhadas e atualizar a exibição da palavra
e. Se a letra adivinhada não está na palavra, reduzir o número de tentativas restantes e exibir a mensagem "Letra incorreta. Tentativas restantes: [n de tentativas restantes]"
f. Verificar se todas as letras da palavra foram adivinhadas
g. Se todas as letras foram adivinhadas, exibir a mensagem "Você venceu!"
h. Se o número de tentativas restantes chegar a zero, exibir a mensagem "Você perdeu. A palavra era [palavra escolhida]" e encerrar o jogo.
