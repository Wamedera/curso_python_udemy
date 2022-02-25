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
    nums_2 = (5, 8)
    print(soma_2(*nums_2))
    nums_3 = (5, 8, 10)
    print(soma_3(*nums_3))
    nums_n = [5, 6, 1, 8, 4, 9]
    print(soma_n(*nums_n))
    