""" Solução verificando cada item em sua posição
 L = [10, 2, 5, 7, 6, 3]
s = 0
for a in range(len(L)):
    if L[a] % 2 == 0:
        s += L[a]
print(s) """

# Solução verificando os itens da lista diretamente
L = [10, 2, 5, 7, 6, 3]
s = 0
for num in L:
    if num % 2 == 0:
        s += num
print(s)