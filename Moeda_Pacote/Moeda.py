#PROGRAMA PRINCIPAL
import pacotes
real = float(input('Digite a sua moeda: R$'))
print(f'A MOEDA FOI R${real}')
print(f'''
aumento de 5%: {pacotes.aumentar(real)}
diminuição de 10%: {pacotes.diminuir(real)}
dobro: {pacotes.dobro(real)}
metade {pacotes.metade(real)}''')
