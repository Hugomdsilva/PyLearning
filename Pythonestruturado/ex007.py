from random import sample


def encontrar_minimo(lista):
    minimo = lista[0]
    for elem in lista:
        if elem < minimo:
            minimo = elem
    return minimo

 
lista_teste = list(sample(range(1,11), k=10))
print(lista_teste)
menor = encontrar_minimo(lista_teste)
print('O menor elemento da lista é [{}]'.format(menor))
