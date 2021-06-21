# SEPARANDO DÍGITOS DE UM NÚMERO
num = int(input('\033[34mInforme um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('\033[31mAnalisando o número\033[33m {}'.format(num))
print('\033[34Unidade:\033[31m {}'.format(u))
print('\033[34Dezena:\033[31m {}'.format(d))
print('\033[34Centena:\033[31m {}'.format(c))
print('\033[34Milhar:\033[31m {}'.format(m))
