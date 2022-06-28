nome = str(input('Digite o seu nome completo: ')).strip().title()
n = nome.split()
print('Primeiro Nome: ',n[0])
print('Ultimo Nome: ',n[len(n)-1])
