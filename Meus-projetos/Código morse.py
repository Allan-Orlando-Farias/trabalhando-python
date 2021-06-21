print('\033[31m=' * 30)
print('\033[35m{:^30}'.format('CÓDIGO MORSE'))
print('\033[31m=' * 30)
while True:
    texto = str(input('\033[34mDigite aqui o seu texto (Sem espaços): ').lower())
    print('''\033[35mOpções:
    \033[31m[ 1 ]\033[36m criptografar
    \033[31m[ 2 ]\033[36m descriptografar''')
    escolha = int(input('\033[35mQual a sua escolha? ').strip())
    if escolha == 1:
        print(f'\033[34mSeu texto é\033[36m {texto}')
        print('\033[34mE ele criptografado é:\033[36m ', end='')
        print('{}'.format(texto.replace("a", ".- ").replace("b", "-... ").replace("c", "-.-. ").replace("d", "-.. ").replace("e", ". ").replace("f", "..-. ").replace("g", "--. ").replace("h", ".... ").replace("i", ".. ").replace("j", ".--- ").replace("k", "-.- ").replace("l", ".-.. ").replace("m", "-- ").replace("n", "-. ").replace("o", "--- ").replace("p", ".--. ").replace("q", "--.- ").replace("r", ".-. ").replace("s", "... ").replace("t", "- ").replace("u", "..- ").replace("v", "...- ").replace("w", ".-- ").replace("x", "-..- ").replace("y", "-.-- ").replace("z", "--.. ").replace("0", "----- ").replace("1", ".---- ").replace("2", "..--- ").replace("3", "...-- ").replace("4", "....- ").replace("5", "..... ").replace("6", "-.... ").replace("7", "--... ").replace("8", "---.. ").replace("9", "----. ")))
    if escolha == 2:
        print(f'\033[34mSeu texto é\033[36m {texto}')
        print('\033[34mE ele descriptografado é:\033[36m ', end='')
        print('{}'.format(texto.replace("--..", "z").replace("-.--", "y").replace("-..-", "x").replace("...-", "v").replace("--.-", "q").replace(".--.", "p").replace(".-..", "l").replace(".---", "j").replace("....", "h").replace("..-.", "f").replace("-.-.", "c").replace("-...", "b").replace(".--", "w").replace("..-", "u").replace("...", "s").replace(".-.", "r").replace("---", "o").replace("-.-", "k").replace("--.", "g").replace("-..", "d").replace("-.", "n").replace("--", "m").replace("..", "i").replace(".-", "a").replace("-", "t").replace(".", "e").replace("-----", "0").replace(".----", "1").replace("..---", "2").replace("...--", "3").replace("....-", "4").replace(".....", "5").replace("-....", "6").replace("--...", "7").replace("---..", "8").replace("----.", "9")))
    continuar = str(input('\033[35mDeseja continuar? [S/N] ').lower().strip()[0])
    if continuar != 's':
        break
print('\033[31m-=-' * 10)
print('\033[33mFim :)')
