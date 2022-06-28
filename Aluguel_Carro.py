km = float(input('Digite a quantidade de Km percorrido: '))
dias = int(input('Quantos dias foi alugado? '))
preço = (dias * 60) + (km * 0.15)
print(f'O total a pagar é de R${preço:.2f}')
