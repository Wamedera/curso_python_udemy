def soma_2(a, b):
    return a + b


def soma_3(a, b, c):
    return a + b + c


def soma_n(*numeros):
    print(type(numeros))
    soma = 0
    for n in numeros:
        soma += n
    
    return soma


if __name__ == '__main__':
    print(soma_2(5, 8))
    print(soma_3(5, 8, 10))
    print(soma_n(5))
    print(soma_n(5, 6, 2))
    print(soma_n(5, 6, 1, 8, 4, 9))
