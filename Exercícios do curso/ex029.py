# RADAR ELETRÔNICO
velocidade = int(input('\033[34mQual é a velocidade atual de um carro? '))
if velocidade > 80:
    multa = velocidade - 80
    valor = multa * 7
    print('\033[31mMULTADO! Você excedeu o limite permitido que é de 80Km/h')
    print('Você deve pagar uma multa de\033[33m R${}!'.format(valor))
print('\033[34mTenha um bom dia! Dirija com segurança!')
