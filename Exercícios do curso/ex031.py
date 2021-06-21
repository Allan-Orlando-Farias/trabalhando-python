# CUSTO DA VIAGEM
distância = float(input('\033[34mQual a distância da sua viagem? '))
print('Você está prestes a iniciar uma viagem de\033[31m {}Km'.format(distância))
if distância <= 200:
    custo = distância * 0.50
    print('\033[34mE o preço da sua passagem será de\033[31m R${:.2f}'.format(custo))
else:
    custo = distância * 0.45
    print('\033[34mE o preço da sua passagem será de\033[31m R${:.2f}'.format(custo))
