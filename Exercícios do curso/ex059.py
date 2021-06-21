# CRIANDO UM MENU DE OPÇÕES
n1 = int(input('\033[34mPrimeiro valor: '))
n2 = int(input('Segundo valor: '))
opção = 0
while opção != 5:
    print('''    \033[31m[ 1 ]\033[33m somar
    \033[31m[ 2 ]\033[33m multiplicar
    \033[31m[ 3 ]\033[33m maior
    \033[31m[ 4 ]\033[33m novos números
    \033[31m[ 5 ]\033[33m sair do programa''')
    opção = int(input('\033[36m>>>\033[34m Qual é a sua opção? '))
    if opção == 1:
        resultado = n1 + n2
        print(f'\033[34mA soma entre\033[31m {n1}\033[33m +\033[31m {n2}\033[34m é\033[31m {resultado}')
    elif opção == 2:
        resultado = n1 * n2
        print(f'\033[34mO resultado de\033[31m {n1}\033[33m x\033[31m {n2}\033[34m é\033[31m {resultado}')
    elif opção == 3:
        if n1 > n2:
            resultado = n1
        else:
            resultado = n2
        print(f'\033[34mEntre\033[31m {n1}\033[34m e\033[31m {n2}\033[34m o maior é\033[31m {resultado}')
    elif opção == 4:
        n1 = int(input('\033[34mPrimeiro valor: '))
        n2 = int(input('\033[34mSegundo valor: '))
    elif opção == 5:
        print('\033[35mFinalizando...')
    else:
        print('\033[31mOpção inválida.\033[34m Tente novamente')
    print('\033[36m=-=' * 10)
print('\033[34mFim do programa! Volte sempre!')
