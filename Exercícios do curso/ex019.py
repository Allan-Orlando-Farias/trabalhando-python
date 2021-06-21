# SORTEANDO UM ITEM NA LISTA
import random
a1 = str(input('\033[34mPrimeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))
lista = [a1, a2, a3, a4]
escolhido = random.choice(lista)
print('O aluno escolhido foi\033[31m {}'.format(escolhido))
