n = int(input('Quantos termos quer: '))
t1 = 0  #FIBONACCI
t2 = 1  #FAZ UMA SEQUENCIA, t1, t2, t3 / t3 = t1 + t2 t1= t2, t2= t3
print(t1, t2, end=' ')
cont = 3 #PRECISA DO 3 NÚMERO PARA SABER A SEQUENCIA
while cont <= n:
    t3 = t1 + t2
    print(t3, end=' ')
    t1 = t2
    t2 = t3
    cont += 1
print(' FIM')
