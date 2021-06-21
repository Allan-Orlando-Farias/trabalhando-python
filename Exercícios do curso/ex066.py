# VÁRIOS NÚMEROS COM FLAG
cont = soma = 0
while True:
    n = int(input('\033[34mDigite um valor\033[33m (999 para parar): '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'\033[34mA soma dos\033[31m {cont}\033[34m valores foi\033[33m {soma}\033[34m!')
