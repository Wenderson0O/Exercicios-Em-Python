numeros = ('ZERO', 'UM', 'DOIS', 'TREIS', 'QUATRO', 'CINCO', 'SEIS',
           'SETE', 'OITO', 'NOVE', 'DEUS', 'ONZE', 'DOZE', 'TREZE',
           'QUATORZE', 'QUINZE', 'DEZESES', 'DEZESSETE', 'DEZOITO',
           'DEZENOVE', 'VINTE')
while True: #FAZ A PERGUNTA INFINITA, ATE O USUARIO DIGITA O NÚMERO DESEJADA
    perg = int(input('Digite um número entre 0 e 20: '))
    if 0 <= perg <= 20:
        break
    print('TENTE NOVAMENTE!')
print('você Digitou O NÚMERO', numeros[perg])
