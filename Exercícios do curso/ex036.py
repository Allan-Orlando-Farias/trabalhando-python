# APROVANDO EMPRÉSTIMO
valor = float(input('\033[34mValor da casa: R$'))
salário = float(input('Salário do comprador: R$'))
financiamento = int(input('Quantos anos de financiamento? '))
maximo = salário * 30 / 100
prestação = valor / (financiamento * 12)
print('Para pagar uma casa de\033[33m R${:.2f}\033[34m em\033[33m {}\033[34m anos a prestação será de\033[33m R${:.2f}'.format(valor, financiamento, prestação))
if prestação <= maximo:
    print('\033[34mEmpréstimo\033[36m ACEITO')
else:
    print('\033[34mEmpréstimo\033[31m NEGADO')
