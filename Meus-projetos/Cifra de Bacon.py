print('\033[31m-=' * 15)
print('\033[33m{:^30}'.format('CIFRA DE BACON'))
print('\033[31m-=' * 15)
while True:
    texto = str(input('\033[34mDigite o texto: ').lower())
    print('''\033[34mEscolha uma das opções abaixo:
    \033[31m[ 1 ]\033[33m para CRIPTOGRAFAR
    \033[31m[ 2 ]\033[33m para DESCRIPTOGRAFAR''')
    escolha = int(input('\033[34mQual a sua escolha? '))
    if escolha == 1:
        print('\033[34mO texto escrito foi\033[36m {}'.format(texto))
        print('\033[34mE criptografado é\033[36m {}'.format(texto.replace('a', 'aaaaa ').replace('b', 'aaaab ').replace('c', 'aaaba ').replace('d', 'aaabb ').replace('e', 'aabaa ').replace('f', 'aabab ').replace('g', 'aabba ').replace('h', 'aabbb ').replace('i', 'abaaa ').replace('j', 'abaab ').replace('k', 'ababa ').replace('l', 'ababb ').replace('m', 'abbaa ')
                                                            .replace('n', 'abbab ').replace('o', 'abbba ').replace('p', 'abbbb ').replace('q', 'baaaa ').replace('r', 'baaab ').replace('s', 'baaba ').replace('t', 'baabb ').replace('u', 'babaa ').replace('v', 'babab ').replace('w', 'babba ').replace('x', 'babbb ').replace('y', 'bbaaa ').replace('z', 'bbaab ')))

    elif escolha == 2:
        print('\033[34mO texto escrito foi\033[36m {}'.format(texto))
        print('\033[34mE descriptografado é\033[36m {}'.format(texto.replace('aaaaa ', 'a').replace('aaaab ', 'b').replace('aaaba ', 'c').replace('aaabb ', 'd').replace('aabaa ', 'e').replace('aabab ', 'f').replace('aabba ', 'g').replace('aabbb ', 'h').replace('abaaa ', 'i').replace('abaab ', 'j').replace('ababa ', 'k').replace('ababb ', 'l').replace('abbaa ', 'm')
                                                               .replace('abbab ', 'n').replace('abbba ', 'o').replace('abbbb ', 'p').replace('baaaa ', 'q').replace('baaab ', 'r').replace('baaba ', 's').replace('baabb ', 't').replace('babaa ', 'u').replace('babab ', 'v').replace('babba ', 'w').replace('babbb ', 'x').replace('bbaaa ', 'y').replace('bbaab ', 'z')))

    else:
        print('\033[31mOPÇÃO INVÁLIDA!!!')
    continuar = str(input('Quer continuar? [S/N] ').strip().lower()[0])
    if continuar != 's':
        break
