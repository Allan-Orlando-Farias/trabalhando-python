# TABUADA v3.0
while True:
    n = int(input('\033[34mQuer ver a tabuada de qual valor? '))
    print('\033[31m-' * 30)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'\033[31m{n}\033[33m x\033[31m {c}\033[33m =\033[31m {n * c}')
    print('\033[31m-' * 30)
print('\033[35mPROGRAMA TABUADA ENCERRADO.\033[34m Volte sempre!')
