# TUPLAS COM TIMES DE FUTEBOL
times = ['Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense', 'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife', 'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético GO']
print('\033[31m=-=' * 30)
print(f'\033[33mLista de times do Brasileirão: {times}')
print('\033[31m=-=' * 30)
print(f'\033[34mOs 5 primeiros são\033[35m {times[0:5]}')
print('\033[31m=-=' * 30)
print(f'\033[34mOs 4 últimos são\033[35m {times[- 4:]}')
print('\033[31m=-=' * 30)
print(f'\033[34mTimes em ordem alfabética:\033[35m {sorted(times)}')
print('\033[31m=-=' * 30)
print(f'\033[34mO Chapecoense está na\033[35m {times.index("Chapecoense") + 1}ª\033[34m posição')
