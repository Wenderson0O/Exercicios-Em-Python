maior = 0
menor = 0
for p in range(1,6):
    peso = float(input(f'Digite o peso da {p}° pessoa: '))
    if p == 1: #significa que esta lendo o peso da primeira pessoa
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O Maior peso lido é {maior}kg')
print(f'O Menor peso lido foi {menor}kg')
