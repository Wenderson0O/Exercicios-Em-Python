from datetime import date
quant = 0
quantt = 0
for i in range(0, 5):
    ano_nascimento = int(input('Digite o seu ano de nascimento: '))
    atual = date.today().year
    idade = atual - ano_nascimento
    if idade >= 18:
        quantt += 1
        print(f'MAIOR DE IDADE, idade de {idade} anos')
    else:
        quant += 1
        print(f'MENOR DE IDADE, Idade de {idade} anos')
else:
    print('MENOR DE IDADE, Quantidade: ', quant)
    print('MAIOR DE IDADE, Quantidade: ', quantt)
