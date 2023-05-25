print('--' * 10)
print('Calculo IMC\n')
peso = float(input('Informe o peso Kg '))
altura = float(input('informe a altura '))

IMC = peso / altura ** 2
print('O IMC em questão é de {:.2f}'.format(IMC))
