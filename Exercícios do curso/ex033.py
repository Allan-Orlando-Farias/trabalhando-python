# MAIOR E MENOR VALOR
valor1 = int(input('\033[34mPrimeiro valor: '))
valor2 = int(input('Segundo valor: '))
valor3 = int(input('Terceiro valor: '))
menor = valor1
if valor2 < menor:
    menor = valor2
if valor3 < menor:
    menor = valor3
maior = valor1
if valor2 > maior:
    maior = valor2
if valor3 > maior:
    maior = valor3
print('O menor valor digitado foi\033[31m {}'.format(menor))
print('\033[34mO maior valor digitado foi\033[31m {}'.format(maior))
