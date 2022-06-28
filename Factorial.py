from math import factorial
def fatorial(x, show=False):
    if show == False:
        print(factorial(x))
    if show == True:
        if x > 1:
            print(factorial(x), end=' ')
        else:
            print(factorial(x))

x = int(input('DIGITE UM NÚMERO: '))
fatorial(x, show=False)
