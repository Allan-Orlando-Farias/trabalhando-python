# GAME: PEDRA, PAPEL E TESOURA
from random import randint
from time import sleep
itens = ['Pedra', 'Papel', 'Tesoura']
computador = randint(0, 2)
print('\033[36mJOGO: PEDRA, PAPEL E TESOURA')
print('''\033[34mSuas opções:
\033[31m[ 0 ]\033[33m PEDRA
\033[31m[ 1 ]\033[33m PAPEL
\033[31m[ 2 ]\033[33m TESOURA''')
jogador = int(input('\033[34mQual é a sua jogada? '))
print('\033[35mJO')
sleep(1)
print('\033[35mKEN')
sleep(1)
print('\033[35mPO!!!')
print('\033[31m-=' * 15)
print('\033[34mComputador jogou\033[36m {}'.format(itens[computador]))
print('\033[34mJogador jogou\033[36m {}'.format(itens[jogador]))
print('\033[31m-=' * 15)
if computador == 0:
    if jogador == 0:
        print('\033[33mEMPATE!')
    elif jogador == 1:
        print('\033[36mJOGADOR VENCE!')
    elif jogador == 2:
        print('\033[35mCOMPUTADOR VENCE!')
    else:
        print('\033[31mJOGADA INVÁLIDA!')
elif computador == 1:
    if jogador == 0:
        print('\033[35mCOMPUTADOR VENCE!')
    elif jogador == 1:
        print('\033[33mEMPATE!')
    elif jogador == 2:
        print('\033[36mJOGADOR VENCE!')
    else:
        print('\033[31mJOGADA INVÁLIDA!')
elif computador == 2:
    if jogador == 0:
        print('\033[36mJOGADOR VENCE!')
    elif jogador == 1:
        print('\033[35mCOMPUTADOR VENCE!')
    elif jogador == 2:
        print('\033[33mEMPATE!')
    else:
        print('\033[31mJOGADA INVÁLIDA!')
