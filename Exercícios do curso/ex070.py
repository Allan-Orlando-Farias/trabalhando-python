# ESTATÍSTICAS EM PRODUTOS
print('\033[31m-' * 30)
print('\033[35m{:^30}'.format('LOJA SUPER BARATÃO'))
print('\033[31m-' * 30)
tot = caro = menor = cont = 0
barato = str
while True:
    nome = str(input('\033[34mNome do Produto: '))
    preço = float(input('\033[34mPreço:\033[33m R$'))
    continuar = str(input('\033[34mQuer continuar?\033[33m [S/N] ').strip().lower())
    cont += 1
    tot += preço
    if preço > 1000:
        caro += 1
    if cont == 1:
        barato = nome
        menor = preço
    else:
        if preço < menor:
            menor = preço
            barato = nome
    if continuar not in 's':
        break
print('\033[31m-' * 30)
print(f'\033[34mO total da compra foi\033[31m R${tot}')
print(f'\033[34mTemos\033[31m {caro}\033[34m produtos custando mais de \033[31m R$1000.00')
print(f'\033[34mO produto mais barato foi\033[33m {barato}\033[34m que custa\033[31m {menor}')
