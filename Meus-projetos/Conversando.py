estar = ['vc está bem']
while True:
    pessoa = str(input('Escreva alguma pergunta: ').lower())
    if 'sair de casa' in pessoa and '?' in pessoa:
        print('Sim, mas use máscara')
    if 'comeu bem' in pessoa and '?' in pessoa:
        print('Sim, comi bastante :)')
    if 'você está bem' in pessoa and '?' in pessoa:
        print('Sim estou bem')

# TENHO QUE TERMINAR
