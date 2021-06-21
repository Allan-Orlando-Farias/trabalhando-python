# PRIMEIRO E ÚLTIMO NOME DE UMA PESSOA
nome = str(input('\033[34mDigite o seu nome completo: ').strip())
print('\033[35mMuito prazer em te conhecer!')
separa = nome.split()
print('-' * 28)
print('\033[34mSeu primeiro nome é\033[31m {}'.format(separa[0]))
print('\033[34mSeu último nome é\033[31m {}'.format(separa[-1]))
