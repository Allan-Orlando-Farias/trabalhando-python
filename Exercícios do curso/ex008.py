# CONVERSOR DE MEDIDAS
distância = int(input('\033[34mUma distância em metros: '))
km = distância / 1000
hm = distância / 1000
dam = distância / 10
dm = distância * 10
cm = distância * 100
mm = distância * 1000
print(f'''A medida de\033[31m {distância}\033[34mm corresponde a
\033[31m{km}\033[33m km\033[31m
{hm}\033[33m hm\033[31m
{dam}\033[33m dam\033[31m
{dm}\033[33m dm\033[31m
{cm}\033[33m cm\033[31m
{mm}\033[33m mm''')
