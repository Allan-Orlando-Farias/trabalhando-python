# CLASSIFICANDO ATLETAS
from datetime import date
nascimento = int(input('\033[34mAno de Nascimento: '))
idade = date.today().year - nascimento
print('\033[34mO atleta tem\033[31m {}\033[34m anos.'.format(idade))
if idade < 9:
    print('\033[34mClassificação:\033[33m MIRIM')
elif 9 < idade <= 14:
    print('\033[34mClassificação:\033[33m INFANTIL')
elif 14 < idade <= 19:
    print('\033[34mClassificação:\033[33m JUNIOR')
elif 19 < idade <= 25:
    print('\033[34mClassificação:\033[33m SÊNIOR')
else:
    print('\033[34mClassificação:\033[33m MASTER')
