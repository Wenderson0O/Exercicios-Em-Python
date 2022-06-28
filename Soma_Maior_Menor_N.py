numero = 1
quant_numero = 0
soma_numero = 0
maior = 0
menor = 0
resp = 'S'
while resp in 'Ss': # IN: DENTRO,  WHILE: ENQUANTO, enquanto resp dentro 'S'...
    numero = int(input('Digite um número: '))
    quant_numero += 1
    soma_numero += numero  # SOMA OS NÚMEROS
    soma = soma_numero / quant_numero
    if quant_numero == 1: #SABER O VALOR MAIOR E MENOR
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    resp = str(input('DESEJA CONTINUAR [S/N]: ')).upper().strip()[0]
print(f'A MÉDIA DOS NÚMEROS FOI {soma}')
print(f'A MAIOR FOI {maior}')
print(f'E MENOR FOI {menor}')
