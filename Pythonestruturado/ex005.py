valor = int(input('Quantos produtos voce deseja comprar?'))
if valor <= 10:
    print('O valor da compra é de {}R$'.format(valor * 10))
elif valor <= 20:
    print('O valor da compra é de {}R$ com 10% de desconto'.format((valor * 10) * 0.9))

else:
    print('O valor da compra é de {}R$ com 20% de desconto'.format((valor * 10) * 0.8))
