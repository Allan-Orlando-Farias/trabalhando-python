# PROGRESSÃO ARITMÉTICA v2.0
print('\033[35mGerador de PA')
print('\033[31m-=' * 10)
primeiro = int(input('\033[34mPrimeiro termo: '))
razão = int(input('\033[34mRazão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('\033[33m{}\033[31m -> '.format(termo), end='')
    termo += razão
    cont += 1
print('\033[34mFIM')
