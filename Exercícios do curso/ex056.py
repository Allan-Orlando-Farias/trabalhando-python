# ANALISADOR COMPLETO
media = cont = maioridadehomem = 0
nomevelho = ''
for c in range(1, 5):
    print('\033[31m-----\033[33m {}ª\033[34m PESSOA\033[31m -----'.format(c))
    nome = str(input('\033[34mNome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo\033[35m [M/F]: ').strip()[0].upper())
    media += idade / 4
    if idade < 20 and sexo == 'F':
        cont += 1
    if c == 1 and sexo == 'M':
        maioridadehomem = idade
        nomevelho = nome
print('\033[34mA média de idade do grupo é\033[33m {}\033[34m anos'.format(media))
print('\033[34mO homem mais velho tem\033[33m {}\033[34m anos e se chama\033[33m {}'.format(maioridadehomem, nomevelho))
print('\033[34mAo todo são\033[33m {}\033[34m mulheres com menos de\033[33m 20\033[34m anos'.format(cont))
