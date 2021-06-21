# ANALISANDO TRIÂNGULOS v2.0
r1 = int(input('\033[34mPrimeiro segmento: '))
r2 = int(input('Segundo segmento: '))
r3 = int(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[34mOs segmentos acimas\033[33m PODEM FORMAR\033[34m um trângulo ', end='')
    if r1 == r2 == r3:
        print('\033[31mEQUILÁTERO!')
    if r1 != r2 != r3 != r1:
        print('\033[31mESCALENO!')
    else:
        print('\033[31mISÓSCELES')
else:
    print('\033[34mOs segmentos acimas\033[33m NÃO PODEM\033[34m formar um triângulo')
