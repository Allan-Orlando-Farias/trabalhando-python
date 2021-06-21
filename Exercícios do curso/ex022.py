# ANALISADOR DE TEXTOS
from time import sleep
nome = str(input('\033[34mDiga o seu nome completo: ').strip())
print("\033[35mAnalisando o seu nome...")
sleep(1)
print('\033[34mSeu nome em maiúsculas é\033[31m {}'.format(nome.upper()))
print('\033[34mSeu nome em minúsculas é\033[31m {}'.format(nome.lower()))
print('\033[34mSeu nome tem ao todo\033[31m {}\033[34m letras'.format(len(nome) - nome.count(' ')))
separa = nome.split()
print('Seu primeiro nome é\033[31m {}\033[34m e ele tem\033[31m {}\033[34m letras'.format(separa[0], len(separa[0])))
