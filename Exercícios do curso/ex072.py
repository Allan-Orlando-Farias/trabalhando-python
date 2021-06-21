# NÚMEROS POR EXTENSO
números = ('zero', 'um', 'dois', 'três', 'quatro',
           'cinco', 'seis', 'sete', 'oito', 'nove',
           'dez', 'onze', 'doze', 'treze', 'quatorze',
           'quinze', 'dezesseis', 'dezessete', 'dezoito',
           'dezenove', 'vinte')
while True:
    n = int(input('\033[35mDigite um número entre 0 e 20: '))
    if 0 < n < 20:
        break
    print('\033[31mTente novamente...')
print(f'\033[34mVocê digitou o número\033[31m {números[n]}')
