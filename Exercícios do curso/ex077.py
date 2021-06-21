# CONTANDO VOGAIS COM TUPLAS
palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')
for p in palavras:
    print(f'\n\033[34mNa palavra\033[33m {p.upper()}\033[34m temos\033[31m ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end='')
