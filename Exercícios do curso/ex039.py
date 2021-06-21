# ALISTAMENTO MILITAR
from datetime import date
nascimento = int(input('\033[34mAno de nascimento: '))
idade = date.today().year - nascimento
print('\033[34mQuem nasceu em\033[31m {}\033[34m tem\033[31m {}\033[34m anos em\033[31m {}\033[34m.'.format(nascimento, idade, date.today().year))
if idade < 18:
    alistamento = 18 - idade
    ano = nascimento + 18
    print('\033[34mAinda faltam\033[31m {}\033[34m anos para o alistamento'.format(alistamento))
    print('\033[34mSeu alistamento será em\033[31m {}\033[34m.'.format(ano))
elif idade == 18:
    print('\033[34mVocê tem que se alistar\033[31m IMEDIATAMENTE!')
else:
    ano = nascimento + 18
    alistamento = idade - 18
    print('\033[34mVocê já deveria ter se alistado há\033[31m {}\033[34m anos.'.format(alistamento))
    print('\033[34mSeu alistamento foi em\033[31m {}.'.format(ano))
