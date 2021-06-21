# LISTA ORDENADA SEM REPETIÇÕES
lista = []
for c in range(0, 5):
    n = int(input('\033[34mDigite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('\033[35mAdicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'\033[35mAdicionado na posição\033[31m {pos}\033[35m da lista...')
                break
            pos += 1
print('\033[31m=-' * 30)
print(f'\033[34mOs valores digitados em ordem foram\033[36m {lista}')
