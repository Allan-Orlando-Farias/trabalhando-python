# AUMENTOS MÚLTIPLOS
salário = float(input('\033[34mQual é o salário do funcionário? R$'))
if salário <= 1250:
    aumento = salário + (salário * 15 / 100)
else:
    aumento = salário + (salário * 10 / 100)
print('Quem ganhava\033[33m R${:.2f}\033[34m passa a receber\033[33m R${:.2f}\033[34m agora.'.format(salário, aumento))
