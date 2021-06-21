# REAJUSTE SALARIAL
salário = float(input('\033[34mQual é o salário do Funcionário? R$'))
aumento = salário + (salário * 15 / 100)
print('Um funcionário que ganhava R$\033[31m {}\033[34m, com\033[31m 15%\033[34m de aumento, passa a receber R$\033[31m {:.2f}'.format(salário, aumento))
