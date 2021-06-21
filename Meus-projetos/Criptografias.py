print('\033[31m-=-' * 10)
print('\033[33m{:^30}'.format('CRIPTOGRAFIAS'))
print('\033[31m-=-' * 10)
print('''\033[35mEscolha uma das criptografias abaixo:
    \033[31m[ 1 ]\033[36m Cifra de Bacon
    \033[31m[ 2 ]\033[36m Código de Morse''')
texto = str(input('\033[34mEscreva o seu texto aqui: ').lower())
escolha = int(input('\033[34mQual a sua escolha? ').strip()[0])
print('''\033[35mEscolha uma das opções abaixo: 
    \033[31m[ 1 ]\033[36m Criptografar
    \033[31m[ 2 ]\033[36m Decriptografar''')
depois = int(input('\033[34mQual a sua escolha? ').strip()[0])
if escolha == 1 and depois == 1:
    print('\033[34mO texto escrito foi\033[36m {}'.format(texto))
    print('\033[34mE criptografado é\033[36m {}'.format(texto.replace('a', 'aaaaa ').replace('b', 'aaaab ').replace('c', 'aaaba ').replace('d', 'aaabb ').replace('e', 'aabaa ').replace('f', 'aabab ').replace('g', 'aabba ').replace('h', 'aabbb ').replace('i', 'abaaa ').replace('j', 'abaab ').replace('k', 'ababa ').replace('l', 'ababb ').replace('m', 'abbaa ').replace('n', 'abbab ').replace('o', 'abbba ').replace('p', 'abbbb ').replace('q', 'baaaa ').replace('r', 'baaab ').replace('s', 'baaba ').replace('t', 'baabb ').replace('u', 'babaa ').replace('v', 'babab ').replace('w', 'babba ').replace('x', 'babbb ').replace('y', 'bbaaa ').replace('z', 'bbaab ')))

elif escolha == 1 and depois == 2:
    print('\033[34mO texto escrito foi\033[36m {}'.format(texto))
    print('\033[34mE descriptografado é\033[36m {}'.format(texto.replace('aaaaa ', 'a').replace('aaaab ', 'b').replace('aaaba ', 'c').replace('aaabb ', 'd').replace('aabaa ', 'e').replace('aabab ', 'f').replace('aabba ', 'g').replace('aabbb ', 'h').replace('abaaa ', 'i').replace('abaab ', 'j').replace('ababa ', 'k').replace('ababb ', 'l').replace('abbaa ', 'm').replace('abbab ', 'n').replace('abbba ', 'o').replace('abbbb ', 'p').replace('baaaa ', 'q').replace('baaab ', 'r').replace('baaba ', 's').replace('baabb ', 't').replace('babaa ', 'u').replace('babab ', 'v').replace('babba ', 'w').replace('babbb ', 'x').replace('bbaaa ', 'y').replace('bbaab ', 'z')))

if escolha == 2 and depois == 1:
    print(f'\033[34mSeu texto é\033[36m {texto}')
    print('\033[34mE ele criptografado é:\033[36m ', end='')
    print('{}'.format(texto.replace("a", ".- ").replace("b", "-... ").replace("c", "-.-. ").replace("d", "-.. ").replace("e", ". ").replace("f", "..-. ").replace("g", "--. ").replace("h", ".... ").replace("i", ".. ").replace("j", ".--- ").replace("k", "-.- ").replace("l", ".-.. ").replace("m", "-- ").replace("n", "-. ").replace("o", "--- ").replace("p", ".--. ").replace("q", "--.- ").replace("r", ".-. ").replace("s", "... ").replace("t", "- ").replace("u", "..- ").replace("v", "...- ").replace("w", ".-- ").replace("x", "-..- ").replace("y", "-.-- ").replace("z", "--.. ").replace("0", "----- ").replace("1", ".---- ").replace("2", "..--- ").replace("3", "...-- ").replace("4", "....- ").replace("5", "..... ").replace("6", "-.... ").replace("7", "--... ").replace("8", "---.. ").replace("9", "----. ")))

if escolha == 2 and depois == 2:
    print(f'\033[34mSeu texto é\033[36m {texto}')
    print('\033[34mE ele descriptografado é:\033[36m ', end='')
    print('{}'.format(texto.replace("--..", "z").replace("-.--", "y").replace("-..-", "x").replace("...-", "v").replace("--.-", "q").replace(".--.", "p").replace(".-..", "l").replace(".---", "j").replace("....", "h").replace("..-.", "f").replace("-.-.", "c").replace("-...", "b").replace(".--", "w").replace("..-", "u").replace("...", "s").replace(".-.", "r").replace("---", "o").replace("-.-", "k").replace("--.", "g").replace("-..", "d").replace("-.", "n").replace("--", "m").replace("..", "i").replace(".-", "a").replace("-", "t").replace(".", "e").replace("-----", "0").replace(".----", "1").replace("..---", "2").replace("...--", "3").replace("....-", "4").replace(".....", "5").replace("-....", "6").replace("--...", "7").replace("---..", "8").replace("----.", "9")))
