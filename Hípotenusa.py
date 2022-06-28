import math
cateto_oposto = float(input('Digite o número do cateto oposto: '))
cateto_adjecente = float(input('Digite o número do cateto adjecente: '))
#print(f'O comprimento da Hipotenusa é:{(cateto_oposto**2 + cateto_adjecente**2) ** (1/2):.2f}')
hi = math.hypot(cateto_oposto, cateto_adjecente)
print(f'A hipotenusa vai Valer {hi:.2f}')
