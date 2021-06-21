# NÚMEROS PRIMOS
num = int(input('\033[34mDigite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[34mO número\033[33m {}\033[34m foi divisível\033[33m {}\033[34m vezes'.format(num, tot))
if tot == 2:
    print('\033[34mE por isso ele é\033[33m PRIMO!')
else:
    print('\033[34mE por isso ele\033[31m NÃO\033[34m é\033[33m PRIMO')
