# LISTAS COM PARES E ÍMPARES
pares = []
ímpares = []
for c in range(1, 8):
    n = int(input(f'\033[34mDigite o\033[35m {c}o\033[34m. valor: '))
    if n % 2 == 0:
        pares.append(n)
    else:
        ímpares.append(n)
print('\033[31m-=' * 30)
print('\033[34mOs valores pares digitados foram:\033[31m {}'.format(sorted(pares)))
print('\033[34mOs valores ímpares digitados foram:\033[31m {}'.format(sorted(ímpares)))
