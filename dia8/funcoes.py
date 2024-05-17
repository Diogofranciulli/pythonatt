a = int(input('digite o primeiro numero'))
b = int(input('digite o segundo numero'))
c = int(input('digite o terceiro numero'))


def grau (a , b , c):
    delta = ((b**2) - 4 * a * c)

    x1 = (-b + (delta**0.5))/ 2 * a
    x2 = (-b - (delta**0.5))/ 2 * a
    print(x1, x2)
    return
grau(a , b, c)

