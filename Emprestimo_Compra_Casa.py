sálario = float(input('Digite o seu Sálario: R$'))
casa = float(input('Digite o valor da casa: R$'))
anos_apagar = int(input('Digite em quantos anos deseja pagar: '))
prestação_mensal = sálario * 30 / 100
apagar = casa / (anos_apagar * 12)
if apagar <= prestação_mensal:
    print(f'Emprestimo CONFIRMADO! Pagarar R${apagar:.2f} por MÊS, todo o ano, em {anos_apagar} ANOS')
else:
    print('EMPRESTIMO NEGADO!')
