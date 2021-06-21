# VERIFICANDO AS PRIMEIRAS LETRAS DE UM TEXTO
cidade = str(input('\033[34mEm que você nasceu?\033[31m ').strip().upper())
print(cidade[:5] == 'SANTO' or cidade[:5] == 'SANTOS')
