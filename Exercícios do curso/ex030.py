# PAR OU ÍMPAR
número = int(input('\033[34mMe diga um número qualquer: '))
if número % 2 == 0:
    print('O número\033[31m {}\033[34m é\033[31m PAR'.format(número))
else:
    print('O número\033[31m {}\033[34m é\033[31m ÍMPAR'.format(número))
