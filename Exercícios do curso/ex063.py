# SEQUÊNCIA DE FIBONNACI
print('\033[31m-' * 30)
print('\033[35mSEQUÊNCIA DE FIBONACCI')
print('\033[31m-' * 30)
n = int(input('\033[34mQuantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('\033[31m~' * 30)
print('\033[33m{}\033[31m ->\033[33m {}'.format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' \033[31m->\033[33m {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' \033[31m->\033[34m FIM')
print('\033[31m~' * 30)
