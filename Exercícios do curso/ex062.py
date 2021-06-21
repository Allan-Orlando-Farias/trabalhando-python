# SUPER PROGRESSÃO ARITMÉTICA v3.0
print('\033[36mGerador de PA')
print('\033[31m-=' * 10)
primeiro = int(input('\033[34mPrimeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('\033[31m{}\033[33m -> '.format(termo), end='')
        termo += razão
        cont += 1
    print('\033[35mPAUSA')
    mais = int(input('\033[34mQuantos termos você quer mostrar a mais? '))
print('\033[34mProgressão finalizada com\033[31m {}\033[34m termos mostrados.'.format(total))
