# GRUPO DA MAIORIDADE
from datetime import date
contmai = contmen = 0
for c in range(1, 8):
    ano = int(input('\033[34mEm que ano a\033[33m {}ª\033[34m pessoa nasceu? '.format(c)))
    idade = date.today().year - ano
    if idade <= 18:
        contmen += 1
    else:
        contmai += 1
print('\033[34mAo todo tivemos\033[33m {}\033[34m pessoas maiores de idade'.format(contmai))
print('\033[34mE também tivemos\033[33m {}\033[34m pessoas menores de idade'.format(contmen))
