#.count('') : conta quantas vezes tem '', .find(''): conta quantas vezes encontro oq esta em ''
#.replace('',''): troca as frases, .capitalize(): primeiros caracteriz fica em maiusculo
#.title():faz a mesma coisa que o capitalize mas por espaço
#strip(): remove os espaços inútil, .split():divide as palavras
nome = str(input('Digite o seu nome completo: ')).strip()
print('Seu nome em Maiúscula é',nome.upper())
print('Seu nome em Minúscula é',nome.lower())
divido = nome.split()
print('Seu nome tem ao todo', len(nome) - nome.count(' '),'Letras')
print('a quantidade de letras no seu primeiro nome é', len(divido[0]))
