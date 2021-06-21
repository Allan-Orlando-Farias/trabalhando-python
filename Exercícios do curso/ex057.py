# VALIDAÇÃO DE DADOS
sexo = str(input('\033[34mInforme seu sexo:\033[33m [M/f] ').strip().upper())
while True:
    if sexo not in 'FM':
        print('\033[31mDados inválidos.\033[34m Por favor, ', end='')
        sexo = str(input('Informe seu sexo: ').strip().upper())
    else:
        break
print('\033[34mSexo\033[33m {}\033[34m registrado com sucesso'.format(sexo))
