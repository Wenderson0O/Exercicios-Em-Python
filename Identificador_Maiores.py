from time import sleep

def maior(* num): #pega todos os valores e desempacota
    cont = maior = 0
    print('=' * 35)
    print('\nANALISANDO OS VALORES PASSADOS...')
    for valores in num:
        print(f'{valores} ', end='', flush=True)
        sleep(0.4)
        if cont == 0:
            maior = valores
        else:
            if valores > maior:
                maior = valores
        cont += 1
    print(f'\nFORAM INFORMADOS {cont} valores ao todo')
    print(f'O MAIOR VALOR INFORMADO É {maior}.')
    sleep(3)


#programa PRINCIPAL
maior(2, 5, 7, 3, 9)
maior(4, 5, 2, 1)
maior(0, 4, 32)

