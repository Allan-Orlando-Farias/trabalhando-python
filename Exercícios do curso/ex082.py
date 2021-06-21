# DIVIDINDO VALORES EM VÁRIAS LISTAS
lista = []
pares = []
ímpares = []
while True:
    valor = int(input('\033[34mDigite um número: '))
    lista.append(valor)
    escolha = str(input('\033[35mQuer continuar?\033[33m [S/N] ').lower())
    if valor % 2 == 0:
        pares.append(valor)
    else:
        ímpares.append(valor)
    if escolha != 's':
        break
print('\033[31m-=-' * 15)
print(f'\033[34mA lista completa é\033[31m {lista}')
print(f'\033[34mA lista de pares é\033[31m {pares}')
print(f'\033[34mA lista de ímpares é\033[31m {ímpares}')
