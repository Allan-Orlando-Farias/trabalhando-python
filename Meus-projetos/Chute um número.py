import random
import time
print('\033[31m-=-' * 10)
print('\033[33m{:^30}'.format('JOGO DA ADIVINHAÇÃO'))
print('\033[31m-=-' * 10)
computador = random.randint(1, 5)
print('\033[34mPensei em um número entre\033[31m 0\033[34m e\033[31m 5\033[34m. Tente adivinhar...')
while True:
    jogador = int(input('\033[34mSeu palpite: '))
    time.sleep(0.5)
    if jogador == computador:
        print('\033[35mParabéns jogador!\033[34m Você pensou no mesmo número que o meu')
        print(f'\033[36mEu pensei no número\033[31m {computador}\033[36m e você no número\033[31m {jogador}')
        break
    elif jogador > computador:
        print('\033[33mVocê chutou alto!')
    elif jogador < computador:
        print('\033[33mVocê chutou baixo!')
