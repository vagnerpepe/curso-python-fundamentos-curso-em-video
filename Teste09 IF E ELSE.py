import os
os.system ('cls' if os.name == 'nt' else 'clear')

tempo = int(input('Quantos anos tem seu carro?: '))
if tempo <= 3:
    print('Carro novo.')
else:
    print('Carro velho.')
print ('--Fim--')

tempo = int(input('Quantos anos tem seu carro?: '))
print('Carro novo.' if tempo<=3 else 'Carro velho.')
print('--FIM--')
