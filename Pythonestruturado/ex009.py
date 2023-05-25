"""
*estratégia 01

def fatorial_iterativo(n):
    f=1
    for i in range(1,n+1):
        f = f*i
    return f

estrategia 02

def fatorial_recursivo(n):
    if((n==0)or(n==1):
        return 1
    return n* fatorial_recursivo(n-1)

"""
""" oque eu fiz
def fat(num):
    aux = num
    for c in range(1, num):
        f = aux * (num - 1)
        aux = f
        num -= 1
    return f """


def fat(num):
    if num >= 2:
        f = 1
        for i in range(1, num + 1):
            f *= i
        return f
    elif num >= 0:
        return 1
    else:
        return 'impossivel'


n = 0
print('O fatorial de {} é {}'.format(n, fat(n)))
