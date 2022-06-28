quant = soma = 0
while True:
    numero = int(input('NÚMERO [999: SAIR]: '))
    if numero == 999: #CONDIÇÃO DE PARADA, E DESCONSIDERE O FRAG
        break
    quant += 1 # QUANTIDADE DIGITADA
    soma += numero # SOMA TOTAL
print(f'A Quantidade digitada foi {quant},\nA Soma dos números foi {soma}')
