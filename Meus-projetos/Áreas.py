from math import trunc
from math import pow
conta = 0
h = 0
print('\033[31m-=' * 15)
print('\033[33m{:^30}'.format('BEM VINDO'))
print('\033[31m-=' * 15)
print('\033[34mEscolha qual desses vc quer descobrir a área: ')
print('''\033[31m[ 1 ]\033[34m Quadrado
\033[31m[ 2 ]\033[34m Retângulo
\033[31m[ 3 ]\033[34m Triângulo
\033[31m[ 4 ]\033[34m Losango
\033[31m[ 5 ]\033[34m Trapézio
\033[31m[ 6 ]\033[34m Polígono regular
\033[31m[ 7 ]\033[34m Círculo
\033[31m[ 8 ]\033[34m Cone
\033[31m[ 9 ]\033[34m Esfera''')
escolha = int(input('\033[36mQual a sua escolha? '))
if escolha == 1:
    largura = float(input('Qual a largura do quadrado? '))
    conta = largura ** 2
    print(f'A área do seu quadrado é de {trunc(conta)}')

if escolha == 2:
    comprimento = float(input('Qual é o comprimento do seu retângulo? '))
    largura = float(input('Qual é a largura do seu retângulo? '))
    conta = comprimento * largura
    print(f'A área do seu retângulo é de {trunc(conta)}')

if escolha == 3:
    triangulo = str(input('Qual é o seu triângulo? '))
    if triangulo == 'normal':
        b = float(input("Digite a base do triangulo: "))
        h = float(input("Digite a altura do triangulo: "))
        print("Area do triangulo:", (b * h) / 2)
        hipotenusa = str(input('Você quer saber a hipotenusa? ').strip().lower()[0])
        if hipotenusa == 's':
            sabe = str(input('Você sabe a medida dos dois catetos?[S/N] ').strip().lower()[0])
            if sabe == 'n':
                cateto = float(input('Qual a medida do cateto? '))
                hipotenusa = float(input('Qual a medida da hipotenusa? '))
                conta = pow((hipotenusa ** 2) - (cateto ** 2), 1/2)
            if sabe == 's':
                catetoo = float(input('Qual a medida do cateto oposto? '))
                catetoa = float(input('Qual a medida do cateto adjacente? '))
                conta = pow((catetoa ** 2) + (catetoo ** 2), 1/2)
            print(f'A hipotenusa mede {conta}')

if escolha == 4:
    diamai = float(input('Qual a medida da diagonal maior? '))
    diame = float(input('Qual a medida da diagonal menor? '))
    conta = (diame * diamai) / 2
    print(f'A área do Losango é de {trunc(conta)}')

if escolha == 5:
    basemai = float(input('Qual a medida da base maior? '))
    basemen = float(input('Qual a medida da base menor? '))
    altura = float(input('Qual a medida da altura? '))
    conta = (basemen + basemai) / 2 * altura
    print(f'A área é de {trunc(conta)}')

if escolha == 6:
    perimetro = float(input('Qual a medida do perímetro? '))
    apotema = float(input('Qual a medida da apótema? '))
    conta = (perimetro / 2) * apotema
    print(f'A área é de {trunc(conta)}')

if escolha == 7:
    raio = float(input('Qual a medida do raio? '))
    conta = 3.14 * raio ** 2
    print(f'A área mede {trunc(conta)}')

if escolha == 8:
    raio = float(input('Qual a medida do raio? '))
    geratriz = float(input('Qual a medida da geratriz? '))
    contabase = 3.14 * raio
    contalateral = 3.14 * raio * geratriz
    conta = 3.14 * raio * (geratriz * raio)
    print(f'A área total é de {trunc(conta)}, a área da base é {contabase} e a área da lateral é de {contalateral}')

if escolha == 9:
    raio = float(input('Qual medida do raio? '))
    conta = 4 * 3.14 * raio ** 2
    print(f'A área é de {trunc(conta)}')
