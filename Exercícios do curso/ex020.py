# SORTEANDO UMA ORDEM NA LISTA
import random
a1 = str(input('\033[34mPrimeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print('A ordem de apresentação será\033[31m')
print(lista)
