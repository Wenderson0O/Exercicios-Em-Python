distancia = float(input('Digite a distancia da viagem KM: '))
if distancia <= 200:
    custo = distancia * 0.50
    print(f'Viagem curta, preço a partir de R${custo:.2f}')
else:
    custo1 = distancia * 0.45
    print(f'Viagem longa, preço a partir de R${custo1:.2f}')
print('Tenha uma Boa Viagem!')
