# ANO BISSEXTO
from datetime import date
ano = int(input('\033[34mQue ano quer analisar? Coloque\033[31m 0\033[34m para o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('\033[34mO ano\033[31m {}\033[34m é\033[36m BISSEXTO'.format(ano))
else:
    print('\033[34mO ano\033[31m {} NÃO\033[34m é\033[36m BISSEXTO'.format(ano))
