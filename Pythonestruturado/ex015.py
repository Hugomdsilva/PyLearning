def dividir(x, y):
    try:
        print('A resposta é :', x / y)
    except ZeroDivisionError:
        print('Nao é possivel dividir por zero')

dividir(42, 2)