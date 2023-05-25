from random import sample


def soma_par (L):
    soma = 0
    for elem in L:
        if elem % 2 == 0:
            soma += elem
    return soma


L = list(sample(range(1,100), k=10))
print(L)
print('A soma dos itens pares da lista é de {}'.format(soma_par(L)))