from datetime import date
ano = int(input('Que ano quer analisar? Digite 0 para analisar o ano atual: '))
if ano == 0 :
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 4 == 0:
    print('BISSEXTO,',ano)
else:
    print(' Não BISSEXTO,',ano)
