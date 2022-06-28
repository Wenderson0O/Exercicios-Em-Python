from datetime import date

def voto(vtc):
    idade = date.today().year - ano
    if idade <= 17:
        print(f'SUA IDADE É DE {idade} ANOS, AINDA NÃO PODE VOTAR.')
    if idade >=18 and idade <=107:
        print(f'SUA IDADE É DE {idade} ANOS, VOTO OBRIGATORIO.')
    if idade >=108:
        print(f'SUA IDADE É DE {idade} ANOS, PARABÉNS!, VOTO OPCIONAL.')


#PROGRAMA PRINCIPAL
ano = int(input('ANO DE NASCIMENTO: '))
voto(0)
