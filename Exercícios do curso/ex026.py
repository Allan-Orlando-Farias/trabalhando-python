# PRIMEIRA E ÚLTIMA OCORRÊNCIA DE UMA STRING
frase = str(input('\033[34mDigite uma frase: ').strip().upper())
print('A letra A aparece\033[31m {}\033[34m vezes na frase.'.format(frase.count('A')))
print('A primeira letra A apareceu na posição\033[31m {}'.format(frase.find('A') + 1))
print('\033[34mA última letra A apareceu na posição\033[31m {}'.format(frase.rfind('A') + 1))
