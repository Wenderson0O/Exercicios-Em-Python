from random import shuffle

#Melhorado

lista = list()
for i in range(4):
    lista.append(str(input('Digite o nome do aluno: ')).title())

#nome1 = str(input('Digite o nome do aluno: '))
#nome2 = str(input('Digite o nome do aluno: '))
#nome3 = str(input('Digite o nome do aluno: '))
#nome4 = str(input('Digite o nome do aluno: '))
#lista = [nome1, nome2, nome3, nome4]

shuffle(lista)
print(f'O aluno(a) escolhido em ordem, foram: {lista}')
