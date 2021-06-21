# DETECTOR DE PALÍNDROMO
frase = str(input('\033[34mDigite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[:: - 1]
print('\033[34mO inverso de\033[33m {}\033[34m é\033[33m {}'.format(junto, inverso))
if inverso == junto:
    print('\033[34mTemos um palíndromo!')
else:
    print('\033[34mA frase digitada não é um palíndromo!')
