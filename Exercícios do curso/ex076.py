# LISTAS DE PREÇOS COM TUPLAS
listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)
print('\033[31m-' * 40)
print(f'\033[33m{"LISTAGEM DE PREÇOS":^40}')
print('\033[31m-' * 40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'\033[34m{listagem[pos]:.<30}', end='')
    else:
        print(f'\033[33mR${listagem[pos]:>7.2f}')
print('\033[31m-' * 40)