import pacotes1
real = float(input('Digite a sua moeda: R$'))
print(f'aumento de 5%: {pacotes1.moeda(pacotes1.aumentar(real))}')
print(f'diminuição de 10%: {pacotes1.moeda(pacotes1.diminuir(real))}')
print(f'dobro: {pacotes1.moeda(pacotes1.dobro(real))}')
print(f'metade: {pacotes1.moeda(pacotes1.metade(real))}')
