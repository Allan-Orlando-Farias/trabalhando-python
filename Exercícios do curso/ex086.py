# MATRIZ EM PYTHON
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'\033[34mDigite um valor para a linha\033[31m {l + 1}\033[34m e a coluna\033[31m {c + 1}\033[34m: '))
print('\033[31m-=\033[35m' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
