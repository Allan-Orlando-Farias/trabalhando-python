# MAIOR E MENOR VALORES
cont = tot = soma = maior = menor = 0
while True:
    n = float(input('\033[34mDigite um número: '))
    continuar = str(input('\033[34mQuer continuar?\033[33m [S/N] ').strip().upper())
    cont += 1
    soma += n
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    if continuar != 'S':
        break
tot = soma / cont
print('\033[34mVocê digitou\033[31m {}\033[34m números e a média foi\033[31m {:.2f}'.format(cont, tot))
print('\033[34mO maior valor foi\033[31m {}\033[34m e o menor foi\033[31m {}'.format(maior, menor))
