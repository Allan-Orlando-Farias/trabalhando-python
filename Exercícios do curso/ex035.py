# ANALISANDO TRIÂNGULO v1.0
print('\033[33m-=' * 30)
print('\033[31m{:^60}'.format('Analisador de triângulos'))
print('\033[33m-=' * 30)
r1 = float(input('\033[34mPrimeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[34mOs segmentos acima\033[36m PODEM FORMAR\033[34m um triângulo!')
else:
    print('\033[34mOs segmentos acima\033[31m NÃO PODEM\033[34m formar um triângulo!')
