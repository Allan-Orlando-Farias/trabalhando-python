# MAIOR E MENOR DA SEQUÊNCIA
maior = menor = 0
for c in range(1, 6):
    peso = float(input(f'\033[34mPeso da \033[33m{c}ª \033[34m pessoa: '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('\033[34mO maior peso lido foi de\033[31m {}\033[34mKg'.format(maior))
print('\033[34mO menor peso lido foi de\033[31m {}\033[34mKg'.format(menor))
