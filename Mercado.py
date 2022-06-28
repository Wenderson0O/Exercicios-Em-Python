continuar = 'S'
total_gasto = produto_caro = menor = cont = 0
barato = ''
while continuar == 'S':
    print('~'*40)
    print('SUPER - MERCADO MARIODIO')
    print('~'*40)
    produto = str(input('DIGITE O NOME DO PRODUTO: ')).upper().strip()
    preco = float(input('DIGITE O PREÇO: '))
    cont += 1
    if cont == 1 or preco < menor: #nome do produto mais barato
        menor = preco
        barato = produto
    continuar = str(input('DESEJA CONTINUAR [S/N]: ')).upper().strip()[0]
    total_gasto += preco #SOMA
    if preco > 1000:
        produto_caro += 1
print(f'''
O TOTAL DE PREÇO DOS PRODUTOS COMPRADOS FORAM R$:{total_gasto}
A QUANTIDADE DE PRODUTOS QUE CUSTA MAIS DE R$:1000 É {produto_caro}
O NOME DO PRODUTO MAIS BARATO É {barato}. QUE CUSTA R${menor:.2f}''')
