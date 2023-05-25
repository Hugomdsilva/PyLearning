import math


def leituradados():
    quantidade = float(input('Digite o valor do coeficiente'))
    return quantidade


def calculodelta(A, B, C):
    delt = B ** 2 - 4 * A * C
    return delt


def calcularraiz(A, B, D):
    if D < 0:
        return 'A equação nao possui raizes nos numeros reais'
    elif D == 0:
        x = (-B) / (2 * A)
        return 'A equação possui apenas a raiz {}'.format(x)
    else:
        D = math.sqrt(D)
        x1 = ((-B - D) / (2 * A))
        x2 = ((-B + D) / (2 * A))
        return 'A equação possui as raizes {} e {}'.format(x2, x1)


# f(x) = Ax^2+bx+c
a = leituradados()
b = leituradados()
c = leituradados()

delta = calculodelta(a, b, c)
print(calcularraiz(a, b, delta))
