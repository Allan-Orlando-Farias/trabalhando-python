print('\033[31m-=' * 30)
print('\033[33m{:^60}'.format('CONVERSOR DE MEDIDAS'))
print('\033[31m-=' * 30)
print('''\033[34mQual a medida sendo usada?
\033[31m[ 1 ]\033[33m QUILÔMETRO
\033[31m[ 2 ]\033[33m METRO
\033[31m[ 3 ]\033[33m CENTÍMETRO
\033[31m[ 4 ]\033[33m MILÍMETRO
\033[31m[ 5 ]\033[33m MICRÔMETRO
\033[31m[ 6 ]\033[33m NANÔMETRO
\033[31m[ 7 ]\033[33m MILHA
\033[31m[ 8 ]\033[33m JARDA
\033[31m[ 9 ]\033[33m PÉ
\033[31m[ 10 ]\033[33m POLEGADA
\033[31m[ 11 ]\033[33m MILHA NÁUTICA''')
escolha = int(input('\033[34mQual a sua escolha? '))
medida = float(input('Qual a medida? '))
opção = int(input('Qual a sua escolha? '))
if escolha == 1:
    if opção == 1:
        print('\033[33m{}Km\033[34m convertido para Quilômetros é\033[31m {:.2f}'.format(medida, medida))

    elif opção == 2:
        conversão = medida * 1000
        print('\033[33m{}Km\033[34m convertido para Metros é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 3:
        conversão = medida * 100000
        print('\033[33m{}Km\033[34m convertido para Centímetros é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 4:
        conversão = medida * 1000000
        print('\033[33m{}Km\033[34m convertido para Milímetros é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 5:
        conversão = medida * 1000000000
        print('\033[33m{}Km\033[34m convertido para Micrômetros é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 6:
        conversão = medida * 1000000000000
        print('\033[33m{}Km\033[34m convertido para Nanômetros é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 7:
        conversão = medida / 1.609
        print('\033[33m{}Km\033[34m convertido para Milhas é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 8:
        conversão = medida * 1094
        print('\033[33m{}Km\033[34m convertido para Jardas é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 9:
        conversão = medida * 3281
        print('\033[33m{}Km\033[34m convertido para Pés é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 10:
        conversão = medida * 39370
        print('\033[33m{}Km\033[34m convertido para Polegadas é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 11:
        conversão = medida / 1.852
        print('\033[33m{}Km\033[34m convertido para Milha Náutica é\033[31m {:.2f}'.format(medida, conversão))


elif escolha == 2:
    if opção == 1:
        conversão = medida / 1000
        print('\033[33m{}M\033[34m convertido para Quilômetros é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 2:
        print('\033[33m{}M\033[34m convertido para Metros é\033[31m {:.2f}'.format(medida, medida))

    elif opção == 3:
        conversão = medida * 100
        print('\033[33m{}M\033[34m convertido para Centímetros é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 4:
        conversão = medida * 1000
        print('\033[33m{}M\033[34m convertido para Milímetros é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 5:
        conversão = medida * 1e+6
        print('\033[33m{}M\033[34m convertido para Micrômetros é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 6:
        conversão = medida * 1e+9
        print('\033[33m{}M\033[34m convertido para Nanômetros é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 7:
        conversão = medida / 1609
        print('\033[33m{}M\033[34m convertido para Milhas é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 8:
        conversão = medida * 1.094
        print('\033[33m{}M\033[34m convertido para Jardas é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 9:
        conversão = medida * 3.281
        print('\033[33m{}M\033[34m convertido para Pés é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 10:
        conversão = medida * 39.37
        print('\033[33m{}M\033[34m convertido para Polegadas é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 11:
        conversão = medida / 1852
        print('\033[33m{}M\033[34m convertido para Milha Náutica é\033[31m {:.2f}'.format(medida, conversão))


elif escolha == 3:
    if opção == 1:
        conversão = medida / 100000
        print('\033[33m{}Cm\033[34m convertido para Quilômetros é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 2:
        conversão = medida / 100
        print('\033[33m{}Cm\033[34m convertido para Metros é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 3:
        print('\033[33m{}Cm\033[34m convertido para Centímetros é\033[31m {:.2f}'.format(medida, medida))

    elif opção == 4:
        conversão = medida * 10
        print('\033[33m{}Cm\033[34m convertido para Milímetros é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 5:
        conversão = medida * 10000
        print('\033[33m{}Cm\033[34m convertido para Micrômetros é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 6:
        conversão = medida * 1e+7
        print('\033[33m{}Cm\033[34m convertido para Nanômetros é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 7:
        conversão = medida / 160934
        print('\033[33m{}Cm\033[34m convertido para Milhas é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 8:
        conversão = medida / 91.44
        print('\033[33m{}Cm\033[34m convertido para Jardas é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 9:
        conversão = medida / 30.48
        print('\033[33m{}Cm\033[34m convertido para Pés é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 10:
        conversão = medida / 2.54
        print('\033[33m{}Cm\033[34m convertido para Polegadas é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 11:
        conversão = medida / 185200
        print('\033[33m{}Cm\033[34m convertido para Milha Náutica é\033[31m {:.2f}'.format(medida, conversão))


elif escolha == 4:
    if opção == 1:
        conversão = medida / 1e+6
        print('\033[33m{}mm\033[34m convertido para Quilômetros é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 2:
        conversão = medida / 1000
        print('\033[33m{}mm\033[34m convertido para Metros é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 3:
        conversão = medida / 10
        print('\033[33m{}mm\033[34m convertido para Centímetros é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 4:
        print('\033[33m{}mm\033[34m convertido para Milímetros é\033[31m {:.2f}'.format(medida, medida))

    elif opção == 5:
        conversão = medida * 1000
        print('\033[33m{}mm\033[34m convertido para Micrômetros é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 6:
        conversão = medida * 1e+6
        print('\033[33m{}mm\033[34m convertido para Nanômetros é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 7:
        conversão = medida / 1.609e+6
        print('\033[33m{}mm\033[34m convertido para Milhas é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 8:
        conversão = medida / 914
        print('\033[33m{}mm\033[34m convertido para Jardas é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 9:
        conversão = medida / 305
        print('\033[33m{}mm\033[34m convertido para Pés é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 10:
        conversão = medida / 25.4
        print('\033[33m{}mm\033[34m convertido para Polegadas é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 11:
        conversão = medida / 1.852e+6
        print('\033[33m{}mm\033[34m convertido para Milha Náutica é\033[31m {:.2f}'.format(medida, conversão))


elif escolha == 5:
    if opção == 1:
        conversão = medida / 1e+9
        print('\033[33m{}μm\033[34m convertido para Quilômetros é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 2:
        conversão = medida / 1e+6
        print('\033[33m{}μm\033[34m convertido para Metros é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 3:
        conversão = medida / 10000
        print('\033[33m{}μm\033[34m convertido para Centímetros é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 4:
        conversão = medida / 1000
        print('\033[33m{}μm\033[34m convertido para Milímetros é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 5:
        print('\033[33m{}μm\033[34m convertido para Micrômetros é\033[31m {:.2f}'.format(medida, medida))

    elif opção == 6:
        conversão = medida * 1000
        print('\033[33m{}μm\033[34m convertido para Nanômetros é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 7:
        conversão = medida / 1.609e+9
        print('\033[33m{}μm\033[34m convertido para Milhas é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 8:
        conversão = medida / 914400
        print('\033[33m{}μm\033[34m convertido para Jardas é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 9:
        conversão = medida / 304800
        print('\033[33m{}μm\033[34m convertido para Pés é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 10:
        conversão = medida / 25400
        print('\033[31m{}μm\033[34m convertido para Polegadas é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 11:
        conversão = medida / 1.852e+9
        print('\033[31m{}μm\033[34m convertido para Milha Náutica é\033[31m {:.2f}'.format(medida, conversão))


elif escolha == 6:
    if opção == 1:
        conversão = medida / 1e+12
        print('\033[33m{}nm\033[34m convertido para Quilômetros é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 2:
        conversão = medida / 1e+9
        print('\033[33m{}nm\033[34m convertido para Metros é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 3:
        conversão = medida / 1e+7
        print('\033[33m{}nm\033[34m convertido para Centímetros é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 4:
        conversão = medida / 1e+6
        print('\033[33m{}nm\033[34m convertido para Milímetros é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 5:
        conversão = medida / 1000
        print('\033[33m{}nm\033[34m convertido para Micrômetros é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 6:
        print('\033[33m{}nm\033[34m convertido para Nanômetros é\033[31m {:.2f}'.format(medida, medida))

    elif opção == 7:
        conversão = medida / 1.609e+12
        print('\033[33m{}nm\033[34m convertido para Milhas é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 8:
        conversão = medida / 9.144e+8
        print('\033[33m{}nm\033[34m convertido para Jardas é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 9:
        conversão = medida / 3.048e+8
        print('\033[33m{}nm\033[34m convertido para Pés é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 10:
        conversão = medida / 2.54e+7
        print('\033[33m{}nm\033[34m convertido para Polegadas é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 11:
        conversão = medida / 1.852e+12
        print('\033[33m{}nm\033[34m convertido para Milha Náutica é\033[31m {:.2f}'.format(medida, conversão))

elif escolha == 7:
    if opção == 1:
        conversão = medida * 1.609
        print('\033[33m{}mi\033[34m convertido para Quilômetros é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 2:
        conversão = medida * 1609
        print('\033[33m{}mi\033[34m convertido para Metros é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 3:
        conversão = medida * 160934
        print('\033[33m{}mi\033[34m convertido para Centímetros é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 4:
        conversão = medida * 1.609e+6
        print('\033[33m{}mi\033[34m convertido para Milímetros é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 5:
        conversão = medida * 1.609e+9
        print('\033[33m{}mi\033[34m convertido para Micrômetros é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 6:
        conversão = medida * 1.609e+12
        print('\033[33m{}mi\033[34m convertido para Nanômetros é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 7:
        print('\033[33m{}mi\033[34m convertido para Milhas é\033[31m {:.2f}'.format(medida, medida))

    elif opção == 8:
        conversão = medida * 1760
        print('\033[33m{}mi\033[34m convertido para Jardas é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 9:
        conversão = medida * 5280
        print('\033[33m{}mi\033[34m convertido para Pés é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 10:
        conversão = medida * 63360
        print('\033[33m{}mi\033[34m convertido para Polegadas é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 11:
        conversão = medida / 1.151
        print('\033[33m{}mi\033[34m convertido para Milha Náutica é\033[31m {:.2f}'.format(medida, conversão))


elif escolha == 8:
    if opção == 1:
        conversão = medida / 1094
        print('\033[33m{}yd\033[34m convertido para Quilômetros é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 2:
        conversão = medida / 1.094
        print('\033[33m{}yd\033[34m convertido para Metros é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 3:
        conversão = medida * 9144
        print('\033[33m{}yd\033[34m convertido para Centímetros é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 4:
        conversão = medida * 914
        print('\033[33m{}yd\033[34m convertido para Milímetros é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 5:
        conversão = medida * 914400
        print('\033[33m{}yd\033[34m convertido para Micrômetros é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 6:
        conversão = medida * 9.144e+8
        print('\033[33m{}yd\033[34m convertido para Nanômetros é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 7:
        conversão = medida / 1760
        print('\033[33m{}yd\033[34m convertido para Milhas é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 8:
        print('\033[33m{}yd\033[34m convertido para Jardas é\033[31m {:.2f}'.format(medida, medida))

    elif opção == 9:
        conversão = medida * 3
        print('\033[33m{}yd\033[34m convertido para Pés é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 10:
        conversão = medida * 36
        print('\033[33m{}yd\033[34m convertido para Polegadas é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 11:
        conversão = medida / 2025
        print('\033[33m{}yd\033[34m convertido para Milha Náutica é\033[31m {:.2f}'.format(medida, conversão))


elif escolha == 9:
    if opção == 1:
        conversão = medida / 3281
        print('\033[33m{}ft\033[34m convertido para Quilômetros é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 2:
        conversão = medida / 3.281
        print('\033[33m{}ft\033[34m convertido para Metros é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 3:
        conversão = medida * 30.48
        print('\033[33m{}ft\033[34m convertido para Centímetros é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 4:
        conversão = medida * 305
        print('\033[33m{}ft\033[34m convertido para Milímetros é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 5:
        conversão = medida * 304800
        print('\033[33m{}ft\033[34m convertido para Micrômetros é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 6:
        conversão = medida * 3.048e+8
        print('\033[33m{}ft\033[34m convertido para Nanômetros é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 7:
        conversão = medida / 5280
        print('\033[33m{}ft\033[34m convertido para Milhas é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 8:
        conversão = medida / 3
        print('\033[33m{}ft\033[34m convertido para Jardas é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 9:
        print('\033[33m{}ft\033[34m convertido para Pés é\033[31m {:.2f}'.format(medida, medida))

    elif opção == 10:
        conversão = medida * 12
        print('\033[33m{}ft\033[34m convertido para Polegadas é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 11:
        conversão = medida / 6076
        print('\033[33m{}ft\033[34m convertido para Milha Náutica é\033[31m {:.2f}'.format(medida, conversão))


elif escolha == 10:
    if opção == 1:
        conversão = medida / 39370
        print('\033[33m{}pol\033[34m convertido para Quilômetros é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 2:
        conversão = medida / 39.37
        print('\033[33m{}pol\033[34m convertido para Metros é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 3:
        conversão = medida * 2.54
        print('\033[33m{}pol\033[34m convertido para Centímetros é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 4:
        conversão = medida * 25.4
        print('\033[33m{}pol\033[34m convertido para Milímetros é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 5:
        conversão = medida * 25400
        print('\033[33m{}pol\033[34m convertido para Micrômetros é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 6:
        conversão = medida * 2.54e+7
        print('\033[33m{}pol\033[34m convertido para Nanômetros é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 7:
        conversão = medida / 63360
        print('\033[33m{}pol\033[34m convertido para Milhas é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 8:
        conversão = medida / 36
        print('\033[33m{}pol\033[34m convertido para Jardas é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 9:
        conversão = medida / 12
        print('\033[33m{}pol\033[34m convertido para Pés é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 10:
        print('\033[33m{}pol\033[34m convertido para Polegadas é\033[31m {:.2f}'.format(medida, medida))

    elif opção == 11:
        conversão = medida / 72913
        print('\033[33m{}pol\033[34m convertido para Milha Náutica é\033[31m {:.2f}'.format(medida, conversão))


elif escolha == 11:
    if opção == 1:
        conversão = medida * 1.852
        print('\033[33m{}nm\033[34m convertido para Quilômetros é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 2:
        conversão = medida * 1852
        print('\033[33m{}nm\033[34m convertido para Metros é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 3:
        conversão = medida * 185200
        print('\033[33m{}nm\033[34m convertido para Centímetros é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 4:
        conversão = medida * 1.852e+6
        print('\033[33m{}nm\033[34m convertido para Milímetros é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 5:
        conversão = medida * 1852e+9
        print('\033[33m{}nm\033[34m convertido para Micrômetros é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 6:
        conversão = medida * 1.852e+12
        print('\033[33m{}nm\033[34m convertido para Nanômetros é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 7:
        conversão = medida * 1.151
        print('\033[33m{}nm\033[34m convertido para Milhas é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 8:
        conversão = medida * 2025
        print('\033[33m{}nm\033[34m convertido para Jardas é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 9:
        conversão = medida * 6076
        print('\033[33m{}nm\033[34m convertido para Pés é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 10:
        conversão = medida * 72913
        print('\033[33m{}nm\033[34m convertido para Polegadas é\033[31m {:.2f}'.format(medida, conversão))

    elif opção == 11:
        print('\033[33m{}nm\033[34m convertido para Milha Náutica é\033[31m {:.2f}'.format(medida, medida))

else:
    print('\033[31mOPÇÃO INVÁLIDA')
