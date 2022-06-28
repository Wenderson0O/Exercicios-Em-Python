from datetime import date
idade = int(input('Digite a Data de nascimento: '))
atual = date.today().year
calculo = atual - idade #CALCULAR A IDADE ATUAL COM A DATA DE NASCIMENTO COM A ATUAL
print(f'Quem nasceu em {idade} tem {calculo} anos')
if calculo <= 9: #Se passou de 9, quer dizer que não precisa repetir
    print('Mirim')
elif calculo <= 14:
    print('Infantil')
elif calculo <= 19:
    print('Junior')
elif calculo == 20:
    print('Sénior')
elif calculo > 20:
    print('Master')
