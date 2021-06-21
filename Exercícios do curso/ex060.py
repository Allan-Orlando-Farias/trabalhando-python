# CÁLCULO DO FATORIAL
print('\033[34mDigite um número para')
n = int(input('calcular seu Fatorial: '))
c = n
f = 1
print('\033[36mCalculando\033[31m {}!\033[33m = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))
