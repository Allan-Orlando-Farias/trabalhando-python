from math import trunc
conta = 0
print('\033[31m-=' * 15)
print('\033[33m{:^30}'.format('BEM VINDO'))
print('\033[31m-=' * 15)
print('\033[35mEscolha uma das opções abaixo:')
print('''\033[31m[ 1 ]\033[34m Cubo
\033[31m[ 2 ]\033[34m Paralelepípedo
\033[31m[ 3 ]\033[34m Prisma Regular
\033[31m[ 4 ]\033[34m Cilindro
\033[31m[ 5 ]\033[34m Cone (ou pirâmide)
\033[31m[ 6 ]\033[34m Esfera''')
escolha = int(input('\033[35mQual a sua escolha? '))
if escolha == 1:
    lado = float(input('\033[34mQual a medida do lado? '))
    conta = lado ** 3
    print(f'\033[36mO volume do Cubo é\033[31m {trunc(conta)}')

if escolha == 2:
    comprimento = float(input('\033[34mQual a medida do comprimento? '))
    largura = float(input('Qual a medida da largura? '))
    altura = float(input('Qual a medida da altura? '))
    conta = comprimento * largura * altura
    print(f'\033[36mO volume do Paralelepípedo é de\033[31m {trunc(conta)}')

if escolha == 3:
    areab = float(input('\033[34mQual a medida da área da base? '))
    altura = float(input('Qual a medida da altura? '))
    conta = areab * altura
    print(f'\033[36mO volume do Prisma Regular é de\033[31m {trunc(conta)}')

if escolha == 4:
    raioba = float(input('\033[34mQual a medida do raio da base? '))
    altura = float(input('Qual a medida da altura? '))
    conta = raioba * altura
    print(f'\033[36mO volume do cilindro é de\033[31m {trunc(conta)}')

if escolha == 5:
    areaba = float(input('\033[34mQual a medida da área da base? '))
    altura = float(input('Qual a medida da altura? '))
    conta = (areaba * altura) / 3
    print(f'\033[36mO volume do Cone é de\033[31m {trunc(conta)}')

if escolha == 6:
    raio = float(input('\033[34mQual a medida do raio? '))
    conta = 4 / 3 * 3.14 * raio ** 3
    print(f'\033[36mO volume da Esfera é de\033[31m {trunc(conta)}')
