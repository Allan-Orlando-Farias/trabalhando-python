# SIMULADOR DE CAIXA ELETRÔNICO
valor = int(input("\033[35minforme o valor a ser sacado : "))
nota50 = valor // 50
valor %= 50
nota20 = valor // 20
valor %= 20
nota10 = valor // 10
valor %= 10
nota1 = valor // 1
print(f"\033[34mnotas de\033[31m 50\033[34m =\033[33m {nota50}")
print(f"\033[34mnotas de\033[31m 20\033[34m =\033[33m {nota20}")
print(f"\033[34mnotas de\033[31m 10\033[34m =\033[33m {nota10}")
print(f"\033[34mnotas de\033[31m 1\033[34m =\033[33m {nota1}")
