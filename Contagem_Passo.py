from time import sleep
def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print('-'*30)
    print(f'contando de {inicio} ate {fim} de {passo} em {passo}')
    sleep(0.5)
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.4)
            cont += passo
        print()
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.4)
            cont -= passo
        print()


#programa PRINCIPAL
contador(1, 10, 1)
contador(10, 0, 2)
print('-'*30)
print('CONTAGEM PERSONALIZADA')
ini = int(input('INÍCIO: '))
fi = int(input('FIM: '))
pas = int(input('PASSO: '))
contador(ini, fi, pas)
