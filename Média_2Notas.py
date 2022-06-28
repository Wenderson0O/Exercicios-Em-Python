nota1 = float(input('Digite a sua primeira nota: '))
nota2 = float(input('Digite a sua segunda nota: '))
media = (nota1 + nota2) / 2
if media >= 7.0:
    print(f'Aluno APROVADO!, Sua média foi {media}')
elif media >= 5.0 and media <= 6.9:
    print(f'Aluno de RECUPERAÇÃO!, Sua média foi {media}')
elif media < 5.0:
    print(f'Aluno REPROVADO!, Sua média foi {media}')
