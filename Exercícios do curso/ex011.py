# PINTANDO PAREDE
largura = float(input('\033[34mQual a largura da parede: '))
alt = float(input('Qual a altura da parede: '))
area = largura * alt
quantidade = area / 2
print('Sua parede tem dimensão de\033[31m {}\033[34m x\033[31m {}\033[34m e a sua área é de\033[31m {}\033[34mm²'.format(largura, alt, area))
print('Para pintar essa parede, você precisará de\033[31m {:.2f}\033[34ml de tinta'.format(quantidade))
