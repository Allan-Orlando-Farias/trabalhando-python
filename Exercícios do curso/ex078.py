# MAIOR E MENOR VALOR DE UMA LISTA
lista = []
mai = men = 0
for c in range(0, 5):
    lista.append(int(input(f'\033[34mDigite um valor para a posição {c}: ')))
    if c == 0:
        mai = men = lista[c]
    else:
        if lista[c] > mai:
            mai = lista[c]
        if lista[c] < men:
            men = lista[c]
    c += 1
print(f'\033[34mVocê digitou os valores\033[31m {lista}')
print(f'\033[34mO maior valor digitado foi\033[31m {mai}\033[34m nas posições\033[31m ', end='')
for i, v in enumerate(lista):
    if v == mai:
        print(f'{i}...', end='')
print(f'\n\033[34mO menor valor digitado foi\033[31m {men}\033[34m nas posições\033[31m ', end='')
for i, v in enumerate(lista):
    if v == men:
        print(f'{i}...', end='')
print()
