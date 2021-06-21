# EXTRAINDO DADOS DE UMA LISTA
lista = []
cont = 1
cinco = ""
while True:
    valor = int(input('\033[34mDigite um valor: '))
    escolha = str(input('\033[35mQuer continuar?\033[36m [S/N] ').lower())
    lista.append(valor)
    if escolha != 's':
        break
    cont += 1
if 5 in lista:
    cinco = 'faz'
else:
    cinco = 'não faz'
lista.sort(reverse=True)
print(f'\033[34mVocê digitou\033[31m {cont}\033[34m elementos.')
print(f'\033[34mOs valores em ordem decrescente são\033[31m {lista}')
print(f'\033[34mO valor\033[31m 5\033[34m {cinco} parte da lista!')
