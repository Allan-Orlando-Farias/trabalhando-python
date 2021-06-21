# VALORES ÚNICOS EM UMA LISTA
lista = []
while True:
    n = int(input('\033[34mDigite um valor: '))
    if n not in lista:
        lista.append(n)
        print('\033[36mValor adicionado com sucesso...')
    else:
        print('\033[31mValor duplicado! Não vou adicionar...')
    escolha = str(input('\033[35mQuer continuar? [S/N] ').strip().lower())
    if escolha != 's':
        break
print('\033[31m=-' * 30)
print(f'\033[34mVocê digitou os valores\033[31m {lista}')
