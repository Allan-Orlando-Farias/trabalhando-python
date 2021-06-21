# TRATANDO VÁRIOS VALORES v1.0
n = soma = cont = 0
n = int(input('\033[34mDigite um número \033[33m[999 para parar]: '))
while n != 999:
    soma += n
    cont += 1
    n = int(input('\033[34mDigite um número\033[33m [999 para parar]: '))
print('\033[34mVocê digitou\033[31m {}\033[34m números e a soma entre eles foi\033[31m {}'.format(cont, soma))
