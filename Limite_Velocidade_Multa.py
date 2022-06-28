carro = float(input('Digite a velocidade do carro km/h: '))
if carro > 80:
    custo = (carro - 80) * 7 #Calculo de Multa com cada 1 km percorrido depois do limite, R$7.0 a cada km
    print(f'Você foi multado! limite de 80km/h, multa de R${custo:.2f}')
else:
    print('Tenha um Bom Dia, diriga com cuidado!')
