sálario = float(input('Digite o valor do Sálario: R$'))
if sálario > 1250:
    #aumento: sálario + (sálario * 10 / 100)
    # desconto: produto - (produto * 10 / 100)
    aumento = sálario + (sálario * 10 / 100)
    print(f'Seu aumento foi de 10%, Seu atual Sálario é R${aumento}')
else:
   aumento1 = sálario + (sálario * 15 / 100)
   print(f'Seu aumento foi de 15%, seu atual Sálario é R${aumento1}')
