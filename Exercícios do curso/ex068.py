# JOGO DO PAR OU ÍMPAR
from random import randint
v = 0
print('\033[31m=-' * 15)
print('\033[35m{:^30}'.format('VAMOS JOGAR PAR OU ÍMPAR'))
print('\033[31m=-' * 15)
while True:
    jogador = int(input('\033[34mDiga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('\033[34mPar ou Ímpar?\033[33m [P/I]').strip().upper()[0])
    print(f'\033[34mVocê jogou\033[31m {jogador}\033[34m e o computador\033[31m {computador}\033[34m. Total de\033[31m {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print('\033[34mVocê\033[33m VENCEU!')
            v += 1
        else:
            print('\033[34mVocê\033[31mPERDEU')
    if tipo == 'I':
        if total % 2 == 1:
            print('\033[34mVocê\033[33m VENCEU!')
            v += 1
        else:
            print('\033[34mVocê\033[31m PERDEU!')
            break
    print('\033[34mVamos jogar novamente...')
    print('\033[31m=-' * 15)
print(f'\033[31mGAME OVER!\033[34m Você venceu\033[31m {v}\033[34m vezes')
