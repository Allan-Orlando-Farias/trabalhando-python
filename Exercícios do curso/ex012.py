# CALCULANDO DESCONTOS
preço = float(input('\033[34mQual é o preço do produto? '))
promoção = preço - (preço * 5 / 100)
print('O produto que custava R$\033[31m {}\033[34m, na promoção de\033[31m 5%\033[34m vai custar R$\033[31m {:.2f}'.format(preço, promoção))
