print('\033[31m-=' * 30)
print('\033[33m{:^60}'.format('Converssor de Temperatura'))
print('\033[31m-=' * 30)
print('''\033[34mQual a medida que está sendo utilizada?
\033[31m[ 1 ]\033[33m CELSIUS
\033[31m[ 2 ]\033[33m FAHRENHEIT
\033[31m[ 3 ]\033[33m KELVIN''')
medida = int(input('\033[34mQual a sua escolha? '))
graus = float(input('\033[34mQuantos graus? '))
print('')
print('''\033[36mOpções de Medidas:
\033[31m[ 1 ]\033[34m converter para\033[33m CELSIUS
\033[31m[ 2 ]\033[34m converter para\033[33m FAHRENHEIT
\033[31m[ 3 ]\033[34m converter para\033[33m KELVIN''')
opção = int(input('\033[34mQual a sua escolha? '))
if medida == 1:
    if opção == 1:
        print('\033[31m{}C°\033[34m convertido para\033[33m C°\033[34m é\033[31m {:.2f}'.format(graus, graus))

    elif opção == 2:
        conversão = (graus * 9 / 5) + 32
        print('\033[31m{}C°\033[34m convertido para\033[33m F°\033[34m é\033[31m {:.2f}'.format(graus, conversão))

    elif opção == 3:
        conversão = graus + 273.15
        print('\033[31m{}C°\033[34m convertido para\033[33m K°\033[34m é\033[31m {:.2f}'.format(graus, conversão))

elif medida == 2:
    if opção == 1:
        conversão = (graus - 32) * 5 / 9
        print('\033[31m{}F°\033[34m convertido para\033[33m C°\033[34m é\033[31m {:.2f}'.format(graus, conversão))

    elif opção == 2:
        print('\033[31m{}F°\033[34m convertido para\033[33m F°\033[34m é\033[31m {:.2f}'.format(graus, graus))

    elif opção == 3:
        conversão = (graus - 32) * 5 / 9 + 273.15
        print('\033[31m{}F°\033[34m convertido para\033[33m K°\033[34m é\033[31m {:.2f}'.format(graus, conversão))

elif medida == 3:
    if opção == 1:
        conversão = (graus - 273.15) * 9 / 5 + 32
        print('\033[31m{}K°\033[34m convertido para\033[33m C°\033[34m é\033[31m {:.2f}'.format(graus, conversão))

    elif opção == 2:
        conversão = (graus - 273.15) * 9 / 5 + 32
        print('\033[31m{}K°\033[34m convertido para\033[33m F°\033[34m é\033[31m {:.2f}'.format(graus, conversão))

    elif opção == 3:
        print('\033[31m{}K°\033[34m convertido para\033[33m K°\033[34m é\033[31m {:.2f}'.format(graus, graus))

else:
    print('\033[31mOPÇÃO INVÁLIDA!')
