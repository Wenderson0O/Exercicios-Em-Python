def notas(* nota, situação = False):
    """
    -> função para analisar notas e varios alunos
    :para nota: uma o mais notas dos alunos (aceita variavel)
    :para situação: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """
    dicionario = dict()
    dicionario['TOTAL'] = len(nota)
    dicionario['MAIOR'] = max(nota)
    dicionario['MENOR'] = min(nota)
    dicionario['MÉDIA'] = sum(nota)/len(nota)
    if situação:
        if dicionario['MÉDIA'] >= 7:
            dicionario['SITUAÇÃO'] = 'BOA'
        elif dicionario['MÉDIA'] >= 5:
            dicionario['SITUAÇÃO'] = 'RAZOÁVEL'
        else:
            dicionario['SITUAÇÃO'] = 'RUIM'
    return dicionario


#programa principal
respostas = notas(9, 4.3, 5, 10, 9.5, situação=True)
print(respostas)
#help(notas)
