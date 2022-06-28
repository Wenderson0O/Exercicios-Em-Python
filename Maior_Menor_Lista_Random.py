from random import randint
maior = menor = 0
for i in range(0, 5):
    numeros = (randint(1, 10))
    print(numeros, end=' ')
    if i == 0:
        maior = numeros
        menor = numeros
    else:
        if numeros > maior:
            maior = numeros
        if numeros < menor:
            menor = numeros

print(f'\nMAIOR É {maior}')
print(f'MENOR É {menor}')
#Com max(numeros) ele pega o maior número em tuplas
#Com min(numeros) ele pega o menor número em tuplas