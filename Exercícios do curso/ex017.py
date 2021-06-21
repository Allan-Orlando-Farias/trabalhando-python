# CATETOS E HIPOTENUSA
import math
catetoO = float(input('\033[34mComprimento do cateto oposto: '))
catetoA = float(input('Comprimento do cateto adjacente: '))
hipotenusa = math.hypot(catetoO, catetoA)
print('A hipotenusa vai medir\033[31m {:.2f}'.format(hipotenusa))
