# VALIDANDO EXPRESSÕES MATEMÁTICAS
expr = str(input('\033[34mDigite a expressão matemática: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('\033[35mSua expressão está válida!')
else:
    print('\033[31mSua expressão está errada!')
