lista = []
quant = 0
while True:
    lista.append(int(input('Número: ')))
    quant += 1


    while True: #LOOP DE PERGUNTA
        perg = str(input('DESEJA CONTINUAR [S/N] ')).strip().upper()[0]
        if perg in 'SN':
            break
    if perg in 'N':
        break
lista.sort(reverse=True) #ORDEM DECRESCENTE
print(f'VALORES DIGITADOS {quant} ')
print(f'A lista de valores ordenados de forma DECRESCENTE {lista} ')
if 5 in lista: #SABER SE O NÚMERO 5 FOI DIGITADO
    print('O VALOR 5 FOI DIGITADO E ESTÁ NA LISTA')
else:
    print('O VALOR 5 NÃO FOI DIGITADO E NÃO ESTÁ NA LISTA')
