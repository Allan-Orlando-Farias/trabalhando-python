# AQUELE CLÁSSICO DA MÉDIA
nota1 = float(input('\033[34mPrimeiro nota: '))
nota2 = float(input('Segunda nota: '))
média = (nota1 + nota2) / 2
print('Tirando\033[31m{}\033[34m e\033[31m {}\033[34m, a média do aluno é\033[31m {:.1f}'.format(nota1, nota2, média))
if média < 5:
    print('\033[34mO aluno foi\033[31m REPROVADO')
elif 5 < média < 6.9:
    print('\033[34mO aluno está em\033[35m RECUPERAÇÃO')
elif média > 7:
    print('\033[34mO aluno foi\033[36m APROVADO')
