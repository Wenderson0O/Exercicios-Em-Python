print('='*30)
print('SIMULADOR DE CAIXA ELETRONICA')
print('='*30)
valor = int(input('SAQUE: '))
total = valor #total do saque
ced = 50 #cédula de maior valor [50,20,10,1]
celtotal = 0 #total de cédulas
while True: #LUPER INFINITO
    if total >= ced:
        total -= ced #tirar
        celtotal += 1 #verificar quantas vezes precisa tirar a cédula
    else:
        if celtotal > 0:
            print(f'TOTAL DE {celtotal} CÉDULAS DE R${ced} ')
        if ced == 50: #tirando as notas
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        celtotal = 0 #faz o total de cédulas volta a zero
        if total == 0: #se não estiver devendo nada, termina o programa
            break
print('~'*30)
print('VOLTE SEMPRE!')
