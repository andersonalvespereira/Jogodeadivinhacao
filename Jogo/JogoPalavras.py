import random

with open('Animal.txt', 'r') as f:
    animais = f.readlines()

tentativas = 0
maxtentativas = 12

indice_animais = random.randint(0, len(animais)-1)
animais_sorteado = animais[indice_animais].replace('\n', '')
animais = ['_'] * len(animais_sorteado)
while True:

    if tentativas==maxtentativas:
        print('Você perdeu, atingiu o maximo de {0} tentativas!'.format(maxtentativas))
        break
    print('Você tem {0} tentativas!'.format(maxtentativas - tentativas))
    letra = input('Digite um letra: ').upper()
    tentativas = tentativas +1
    for i in range(len(animais_sorteado)):
        if letra == animais_sorteado [i]:
            animais[i] = letra
    if '' .join(animais) == animais_sorteado:
        print('Jogo finalizado. Parabéns você acertou!!!')
        print('A palavra é {0}'.format(animais_sorteado))
        print('Você acertou em {0} tentativas'.format(tentativas))
        break
    else:
        print(' '.join(animais))