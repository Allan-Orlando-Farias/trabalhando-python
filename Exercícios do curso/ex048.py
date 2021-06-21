# SOMA ÍMPARES MÚLTIPLOS DE TRÊS
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        cont += 1
print('\033[34mA soma de todos os\033[31m {} valores solicitados é\033[31m {}'.format(cont, soma))
