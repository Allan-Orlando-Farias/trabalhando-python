# LISTA COMPOSTA E ANÁLISE DE DADOS
lista = []
principal = []
maior = menor = 0
while True:
    lista.append(str(input('\033[34mNome: ')))
    lista.append(int(input('Peso: ')))
    continuar = str(input('\033[35mQuer continuar?\033[34m [S/N] ').lower()[0])
    if len(principal) == 0:
        maior = menor = lista[1]
    else:
        if lista[1] > maior:
            maior = lista[1]
        if lista[1] < menor:
            menor = lista[1]
    principal.append(lista[:])
    lista.clear()
    if continuar != 's':
        break
print(f'\033[34mAo todo, você cadastrou\033[31m {principal}\033[34m pessoas')
print(f'\033[34mO maior peso foi de\033[31m {maior}Kg\033[34m. Peso de\033[31m ', end='')
for p in principal:
    if p[1] == maior:
        print(f'[{p[0]}]', end='')
print()
print(f'\033[34mO menor peso foi de\033[31m {menor}Kg\033[34m. Peso de\033[31m ', end='')
for p in principal:
    if p[1] == menor:
        print(f'[{p[0]}]', end='')
