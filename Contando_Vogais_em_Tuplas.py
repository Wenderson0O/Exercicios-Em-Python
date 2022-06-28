palavras = ('MERCADO', 'LEITE', 'CURSO', 'PYTHON', 'LOJA', 'EXERCICIO',
            'TATUAGEM', 'MARGARITA', 'VIDEO')
for i in palavras: #analisa cada elemento da tupla
    print(f'\nNA PALAVRA {i.upper()} temos ', end='')
    for palavras in i: #analisa se a letra esta no grupo das vogais(sem acento)
        if palavras.lower() in 'aeiou': #pode fazer com acento mais tem que coloca no grupo
            print(palavras, end=' ')
