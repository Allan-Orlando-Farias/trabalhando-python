# SOMA DOS PARES
soma = 0
cont = 0
for c in range(1, 7):
    n = int(input('\033[34mDigite um número: '))
    if n % 2 == 0:
        soma += n
        cont += 1
print('\033[34mVocê informou\033[33m {}\033[34m números e a soma foi\033[33m {}'.format(cont, soma))
