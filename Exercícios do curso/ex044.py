# GERENCIADOR DE PAGAMENTOS
print('\033[31m=' * 30)
print('\033[33m{:^30}'.format('LOJAS FARIAS'))
print('\033[31m=' * 30)
preço = float(input('\033[34mPreço das compras: R$'))
print('''FORMAS DE PAGAMENTO
\033[31m[ 1 ]\033[34m à vista dinheiro/cheque
\033[31m[ 2 ]\033[34m à vista cartão
\033[31m[ 3 ]\033[34m 2x no cartão
\033[31m[ 4 ]\033[34m 3x ou mais no cartão''')
opção = int(input('\033[36mQual é a opção? '))
total = preço
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print('\033[34mSua compra será parcelada em\033[31m 2\033[34m x de\033[33m R${:.2f}'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input('\033[34mQuantas parcelas? '))
    parcela = total / totparc
    print('\033[34mA sua compra será parcelada em\033[31m {}\033[34m x de\033[33m R${:.2f}'.format(totparc, parcela))
else:
    total = 0
    print('\033[31mOPÇÃO INVÁLIDA\033[34m de pagamento. Tente novamente!')
print('\033[34mSua compra de\033[33m R${:.2f}\033[34m vai custar\033[33m R${:.2f}\033[34m no final.'.format(preço, total))
