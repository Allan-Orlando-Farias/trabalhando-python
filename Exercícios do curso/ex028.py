# JOGO DA ADIVINHAÇÃO v1.0
import random
from time import sleep
print('\033[33m-' * 55)
print('\033[34mVou pensar em um número entre 0 e 5. Tente adivinhar...')
print('\033[33m-' * 55)
computador = random.randint(0, 5)
jogador = int(input('\033[34mEm que número pensei? ').strip())
print('\033[35mPROCESSANDO...')
sleep(2)
if jogador == computador:
    print('\033[36mVOCÊ GANHOU!\033[34m eu pensei no número\033[31m {}\033[34me você no\033[31m {}'.format(computador, jogador))
else:
    print('\033[31mVOCÊ PERDEU!\033[34m eu pensei no número\033[31m {}\033[34me não no\033[31m {}'.format(computador, jogador))
