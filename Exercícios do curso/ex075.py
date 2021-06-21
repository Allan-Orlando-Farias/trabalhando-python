# ANÁLISE DE DADOS EM UMA TUPLA
num = (int(input('\033[35mDigite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))
print(f'\033[36mVocê digitou os valores\033[31m {num}')
print(f'\033[34mO valor\033[31m 9\033[34m apareceu\033[33m {num.count(9)}\033[34m vezes')
if 3 in num:
    print(f'\033[34mO valor\033[31m 3\033[34m apareceu na\033[33m {num.index(3)+ 1}ª\033[34m posição')
else:
    print('\033[34mO valor\033[31m 3 NÃO\033[34m foi digitado')
print('\033[34mOs valores pares digitados foram\033[33m ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
