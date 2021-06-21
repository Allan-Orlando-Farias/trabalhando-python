# MAIS SOBRE MATRIZ EM PYTHON
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'\033[34mDigite um valor para\033[31m [{l}, {c}]\033[34m: '))
print('\033[31m-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'\033[35m[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print('\033[31m-=' * 30)
print(f'\033[34mA soma dos valores pares é\033[31m {spar}')
for l in range(0, 3):
    scol += matriz[l][2]
print(f'\033[34mA soma dos valores da terceira coluna é\033[31m {scol}')
for c in range(0, 3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'\033[34mO maior valor da segunda lina é\033[31m {mai}')
