def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO: por favor, digite um número inteiro válido.')
            continue
        except (KeyboardInterrupt):
            print('Usúario prefiriu não digitar.')
            return 0
        else:
            return n

        
def leiareal(msg):
    while True:
        try:
            n = float(input(msg).replace(',','.'))
        except (ValueError, TypeError):
            print('ERRO. Por Favor, Digite um Número REAL Válido.')
            continue
        except KeyboardInterrupt:
            print('Usúario prefiriu não digitar.')
            return 0
        else:
            return n


r1 = leiaint('Digite um Valor Inteiro: ')
r2 = leiareal('Digite um Número Real: ')
print(f'O Número INTEIRO Digitado foi {r1}. O Número REAL Digitado foi {r2}')
