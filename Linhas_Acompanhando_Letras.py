def texto(txt):
    pos = 0
    while pos < len(txt):  # Enquanto a linha for menor que a quantidade de letras
        pos *= 1  # soma a quantidade de linhas, acompanhando a quantidade de letras
        pos += 1
    print('-' * pos)
    print(txt)
    print('-' * pos)


#PROGRAMA PRINCIPAL
texto('Olá Mundo!')
texto('O MUNDO DA PROGRAMAÇÃO É FANTASTICO E DIFICIL, MAS EU NÃO DESISTIREI')
texto('EU ESTOU APRENDENDO PYTHON, MYSQL')
