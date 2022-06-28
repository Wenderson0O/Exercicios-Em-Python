from datetime import date
data_nascimento = int(input('Digite a seu ano de nascimento: '))
ano = date.today().year
idade = ano - data_nascimento
print(f'Quem nasceu em {data_nascimento} tem {idade} anos em {ano}')
sexo = str(input('Digite o seu sexo [M/F] : ')).upper()[0]
if sexo == 'M':
    if idade == 18:
        print('Você tem que se ALISTAR IMEDIATAMENTE!')
    elif idade < 18:
        falta = 18 - idade
        print(f'Ainda falta {falta} anos para o alistamento.')
    elif idade > 18:
        falta = idade - 18
        data =  ano - falta
        print(f'Você ja deveria ter se alistado há {falta} anos')
        print(f' Seu alistamento foi em {data}')
else:
    print('O alistmento Militar não é obrigario para Mulheres.')
