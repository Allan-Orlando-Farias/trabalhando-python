# ALUGUEL DE CARROS
dias = int(input('\033[34mQuantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
alugueld = dias * 60
aluguelk = km * 0.15
aluguel = alugueld + aluguelk
print('O total a pagar é de R$\033[31m {}'.format(aluguel))
