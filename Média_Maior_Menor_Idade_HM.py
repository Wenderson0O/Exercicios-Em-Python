soma_sexo = 0
soma_idade = 0
maior_idade_velho = 0
mulher20 = 0
for i in range(0, 4):
    nome = str(input('Digite o seu nome: ')).title().split()
    idade = int(input('Digite a sua idade: '))
    sexo = str(input('Digite o seu sexo: [M/F] ')).upper()
    soma_idade += idade
    if i == 1 and sexo in 'M':
        maior_idade_velho = idade
        homem_velho = nome
    if sexo in 'M' and idade > maior_idade_velho:
        maior_idade_velho = idade
        homem_velho = nome
    if sexo in 'F' and idade < 20:
        mulher20 += 1
media_idade = soma_idade / 4
print(f'A média de idade do grupo é {media_idade} anos')
print(f'O Homem mais velho tem {maior_idade_velho} anos e se chama {homem_velho}')
print(f'Ao Todo são {mulher20} mulheres com menos de 20 anos ')
