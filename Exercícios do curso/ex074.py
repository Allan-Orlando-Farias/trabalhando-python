# MAIOR E MENOR VALORES DE UMA TUPLA
from random import randint

números = (randint(1, 10), randint(1, 10), randint(1, 10),
           randint(1, 10), randint(1, 10))
print('\033[36mOs valores sorteados foram: ', end='')
for n in números:
    print(f'\033[33m{n} ', end='')
print(f'\n\033[34mO maior valor sorteado foi\033[31m {max(números)}')
print(f'\033[34mO menor valor sorteado foi\033[31m {min(números)}')
