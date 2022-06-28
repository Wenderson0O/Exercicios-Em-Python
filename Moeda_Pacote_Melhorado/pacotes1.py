#PACOTES
def aumentar(n=0):
    res = n + (n * 5 / 100)
    return res


def diminuir(n=0):
    res = n - (n * 10 / 100)
    return res


def dobro(n=0):
    res = n * 2
    return res


def metade(n=0):
    res =  n / 2
    return res


def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:5.2f}'.replace('.', ',')

