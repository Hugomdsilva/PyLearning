def eh_primo(n):
    if n < 2:
        return False
    i = n // 2
    while i > 1:
        if n % i == 0:
            return False
        i -= 1
    return True


def result(num):
    men = 'O numero {} nao é primo'.format(num)
    if (eh_primo(num)):
        men = 'O numero {} é primo'.format(num)
    return men


while True:
    numero = eval(input('Digite um numero:'))
    msg = result(numero)
    print(msg)
