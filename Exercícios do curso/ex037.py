# CONVERSOR DE BASES NUMÉRICAS
n = int(input('\033[34mDigite um número inteiro: '))
print('''Escolha uma das bases para a conversão:
\033[31m[ 1 ]\033[34m converter para\033[36m BINÁRIO
\033[31m[ 2 ]\033[34m converter para\033[36m OCTAL
\033[31m[ 3 ]\033[34m converter para\033[36m HEXADECIMAL''')
escolha = int(input('\033[34mSua opção: '))
if escolha == 1:
    print('\033[31m{}\033[34m convertido para\033[36m BINÁRIO\033[34m é igual a\033[31m {}'.format(n, bin(n)[2:]))
elif escolha == 2:
    print('\033[31m{}\033[34m convertido para\033[36m OCTAL\033[34m é igual a\033[31m {}'.format(n, oct(n)[2:]))
else:
    print('\033[31m{}\033[34m convertido para\033[36m HEXADECIMAL\033[34m é igual a\033[31m {}'.format(n, hex(n))[2:])
