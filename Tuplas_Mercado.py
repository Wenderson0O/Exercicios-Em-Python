produtos = ('ARROS', 5, 'LEITE EM PACOTE', 8, 'FEIJÃO', 7, 'OVO', 1,'MASCARA', 2.50, 'REFRI', 5.60, 'CARNE BOVINA', 15.99)
print('-'*40)
print(f'{"LISTA DE PREÇO":^40}')
print('-'*40)
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end='')
    else:
        print(f'R${produtos[pos]:>7.2f}')
print('-'*40)
