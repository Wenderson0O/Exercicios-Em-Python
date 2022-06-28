def area(larg, compri): #FUNÇÃO. eu so coloco o calculo
    calc = larg * compri
    print(f'A área De um terreno {larg}x{compri}  é de {calc}m²')


#PROGRAMA PRINCIPAL
print('='*30)
print('CALCULO DA ÁREA DE UM TERRENO')
print('='*30)
larg = float(input('LARGURA(m): '))
compri = float(input('COMPRIMENTO(m): '))
print('='*30)
area(larg, compri)
