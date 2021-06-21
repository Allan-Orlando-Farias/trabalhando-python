# TABUADA v2.0
n = int(input('\033[34mDigite um número para ver a sua tabuada: '))
for c in range(1, 11):
    print('\033[31m{}\033[34m x\033[31m {}\033[34m =\033[31m{}'.format(n, c, n * c))
