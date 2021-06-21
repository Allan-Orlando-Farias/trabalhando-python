# ÍNDICE DE MASSA CORPORAL
peso = float(input('\033[34mQual é o seu peso\033[33m (Kg)'))
altura = float(input('\033[34mQual é a sua altura?\033[33m (m)'))
imc = peso / (altura ** 2)
print('\033[34mO imc dessa pessoa é de\033[31m {:.1f}'.format(imc))
if imc < 18.5:
    print('\033[34mVocê está\033[31m ABAIXO DO PESO\033[34m normal')
elif 18.5 <= imc < 25:
    print('\033[36mPARABÉNS\033[34m, você está na faixa de\033[33m PESO NORMAL')
elif 25 <= imc < 30:
    print('\033[34mVocê etá em\033[31m SOBREPESO')
elif 30 <= imc < 40:
    print('\033[34mVocê está em\033[31m OBESIDADE\033[34m, cuidado!')
elif imc >= 40:
    print('\033[34mVocê está em\033[31m OBESIDADE MÓRBIDA\033[34m, cuidado!')
