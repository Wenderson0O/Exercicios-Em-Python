#Porcentagem
produto = float(input('Digite o Preço do produto: R$'))
desconto = produto-(produto*5/100)
print(f'O produto que custava R${produto:.2f}, com o desconto de 5%, valera: R${desconto:.2f}')
