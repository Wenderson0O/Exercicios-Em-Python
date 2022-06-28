n1 = int(input('Digite o Primeiro número: '))
n2 = int(input('Digite o Segundo número: '))
if n1 > n2:
    print(f'O maior é {n1}')
elif n2 > n1:
    print(f'O maior é {n2}')
elif n1 == n2:
    print('Os Valores são iguais')
