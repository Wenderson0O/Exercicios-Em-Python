from datetime import date
registro = dict()
registro['NOME'] = str(input('NOME: ')).title()
ano = int(input('ANO DE NASCIMENTO: '))
registro['IDADE'] = date.today().year - ano
registro['CART_TRAB'] = int(input('Nº CARTEIRA DE TRABALHO [0 não tem]: '))
if registro['CART_TRAB'] == 0:
    for k, v in registro.items():
        print(f'-{k} tem o valor {v}')
        print()
if registro['CART_TRAB'] != 0:
    registro['ANO_CONTRAT'] = int(input('ANO DE CONTRATAÇÃO: '))
    registro['SÁLARIO'] = float(input('SÁLARIO: R$ '))
    registro['ANO APOSENTADORIA'] = registro['ANO_CONTRAT'] - ano + 35
    print('-='*30)
    for k, v in registro.items():
        print(f'-{k}: {v}')
    print()
print(registro)
