""" num1 = int(input('escreva um numero:'))
num2 = int(input('escreva outro numero:'))
if num1 > num2:
    print('O numero {} é maior que o numero {}'.format(num1, num2))
else:
    print('O numero {} é maior que o numero {}'.format(num2, num1)) """

num1 = int(input('Escreva um numero:'))
num2 = int(input('Escreva outro numero'))
maior = num1
if num2 > maior:
    maior = num2
print(f'O maior numero é o : {maior}')