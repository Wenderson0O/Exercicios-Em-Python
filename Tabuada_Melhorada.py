print('='*40)
print('TABUADA')
print('='*40)
while True:
    numero = int(input('Digite um número [SAIR: 0] '))
    if numero <=0:
        break
    print('''
    0 = ADIÇÃO
    1 = DIMINUIÇÃO
    2 = MUTIPLICAÇÃO
    3 = DIVIÇÃO
    ''')
    numerador = int(input('Númerador: '))
    if numerador == 0:
        for i in range(1, 11):
            print(f'{numero} + {i} = {numero+i}')
        print('='*40)
    if numerador == 1:
        for i in range(1, 11):
            print(f'{numero} - {i} = {numero-i}')
        print('='*40)
    if numerador == 2:
        for i in range(1, 11):
            print(f'{numero} x {i} = {numero*i}')
        print('='*40)
    if numerador == 3:
        for i in range(1, 11):
            print(f'{numero} / {i} = {numero/i:5.2f}')
        print('='*40)


print('FIM! VOLTE SEMPRE.')
