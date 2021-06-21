# PROGRESSÃO ARITMÉTICA
print('\033[31m=' * 30)
print('\033[33m{:^30}'.format('10 TERMOS DE PA'))
print('\033[31m=' * 30)
termo = int(input('\033[34mPrimeiro termo: '))
razão = int(input('Razão:\033[36m '))
décimo = termo + (10 - 1) * razão
for c in range(termo, décimo + razão, razão):
    print(c, end=' ')
print('\033[35mAcabou!')
