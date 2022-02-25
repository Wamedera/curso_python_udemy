def fibonacci(quantidade):
    resultado = [0, 1]
    while True:
        resultado.append(sum(resultado[-2:]))
        if len(resultado) == quantidade:
            break
        
    return resultado


if __name__ == '__main__':
    for termo in fibonacci(10):
        print(f'{termo}', end=', ')
        