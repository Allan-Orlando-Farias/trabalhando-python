# CONVERSOR DE TEMPERATURAS
temperatura = float(input('\033[34mInforme a Temperatura em ºC: '))
conversor = ((9 * temperatura) / 5) + 32
print('A temperatura de\033[31m {}\033[34mºC corresponde a\033[31m {:.1f}\033[34mºF!'.format(temperatura, conversor))
