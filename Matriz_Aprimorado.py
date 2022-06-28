matriz = [[], [], []] #MATRIZ APRIMORAD0
soma = s = 0
for a in range(3):
    num = int(input('NÚMERO: '))
    matriz[0].append(num)
for b in range(3):
    num = int(input('NÚMERO: '))
    matriz[1].append(num)
for c in range(3):
    num = int(input('NÚMERO: '))
    matriz[2].append(num)
    for m in range(3):
        if matriz[c][m] % 2 == 0:
            soma += matriz[c][m]
soma3 = matriz[0][2]+matriz[1][2]+matriz[2][2]
print(f'''    MATRIZ
[ {matriz[0][0]} ][ {matriz[0][1]} ][ {matriz[0][2]} ]
[ {matriz[1][0]} ][ {matriz[1][1]} ][ {matriz[1][2]} ]
[ {matriz[2][0]} ][ {matriz[2][1]} ][ {matriz[2][2]} ]
A SOMA DOS VALORES DA TERCEIRA COLUNA: {soma3}
O MAIOR VALOR DA SEGUNDA LINHA: {max(matriz[1])}''')
print(f'A SOMA DOS VALORES PARES É {soma}')
