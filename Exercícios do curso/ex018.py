# SENO, COSSENO E TANGENTE
import math
ângulo = int(input('Digite o ângulo que você deseja: '))
print('O ângulo de {} tem o SENO de {:.2f}'.format(ângulo, math.sin(math.radians(ângulo))))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ângulo, math.cos(math.radians(ângulo))))
print('O ângulo de {} tem o TANGENTE de {:.2f}'.format(ângulo, math.tan(math.radians(ângulo))))
