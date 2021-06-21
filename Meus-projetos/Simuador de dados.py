from random import randint
while True:
    jogada = str(input('Você quer jogar um dado? ').strip().lower()[0])
    if jogada == 'n':
        break
    elif jogada != 's':
        jogada = str(input('Você quer jogar um dado? ').strip().lower()[0])
    elif jogada == 's':
        print(f'O dado jogou o número {randint(1, 6)}')
        continue
