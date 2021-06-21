# JOGO DA ADIVINHAÇÃO v2.0
from random import randint
print('\033[34mSou seu computador...')
print('''Acabei de pensar em um número entre\033[33m 0\033[34m e\033[33m 10\033[34m.
Será que você consegue adivinhar qual foi?''')
palpite = int(input('\033[35mQual é seu palpite? '))
computador = randint(0, 10)
tentativas = 1
while palpite != computador:
    if palpite < computador:
        print('\033[35mMais...\033[36m Tente mais uma vez.')
        palpite = int(input('\033[34mQual é seu palpite? '))
        tentativas += 1
    elif palpite > computador:
        print('\033[35mMenos...\033[36m Tente mais uma vez.')
        palpite = int(input('\033[34mQual é seu palpite? '))
        tentativas += 1
    else:
        break
print('\033[34mAcertou com\033[33m {}\033[34m tentativas.\033[36m Parabéns!'.format(tentativas))
