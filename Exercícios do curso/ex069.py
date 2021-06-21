# ANÁLISE DE DADOS DE GRUPO
tot = hom = mul = 0
while True:
    print('\033[31m-' * 30)
    print('\033[35m{:^30}'.format('CADASTRE UMA PESSOA'))
    print('\033[31m-' * 30)
    idade = int(input('\033[34mIdade: '))
    sexo = str(input('\033[34mSexo:\033[33m [M/F] ').strip().lower())
    print('\033[31m-' * 30)
    continuar = str(input('\033[34mQuer continuar?\033[33m [S/N] ').strip().lower())
    if idade > 18:
        tot += 1
    if sexo == 'm':
        hom += 1
    if idade < 20 and sexo == 'f':
        mul += 1
    if continuar not in 's':
        break
print(f'\033[34mTotal de pessoas com mais de 18 anos:\033[31m {tot}')
print(f'\033[34mAo todo temos\033[31m {hom}\033[34m homens cadastrados')
print(f'\033[34mE temos\033[31m {mul}\033[34m mulheres com menos de 20 anos')
