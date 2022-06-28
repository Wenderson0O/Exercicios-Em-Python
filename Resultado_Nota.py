aluno = dict()
aluno['ALUNO'] = str(input('NOME: ')).title()
aluno['NOTA'] = float(input(f'NOTA do(a) {aluno["ALUNO"]}: '))
if aluno["NOTA"] >= 7:
    aluno['SITUAÇÃO'] = 'APROVADO'
if aluno["NOTA"] >= 6 and aluno["NOTA"] < 7:
    aluno['SITUAÇÃO'] = 'RECUPERAÇÃO'
if aluno["NOTA"] <= 5:
    aluno['SITUAÇÃO'] = 'REPROVADO'
print('-'*30)
for k, v in aluno.items():
    print(f' - {k}: {v}')
