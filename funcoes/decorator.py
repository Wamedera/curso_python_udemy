def log(function):
    def decorator(*args, **kwargs):
        print()
        print(f'Nome da função: {function.__name__}')
        print(f'Args: {args}')
        print(f'Kwrgs: {kwargs}')
        resultado = function(*args, **kwargs)
        print(f'Resultado da chamada: {resultado}')
        return resultado
    return decorator


@log
def soma(a, b):
    return a + b


@log
def sub(a, b):
    return a / b


if __name__ == '__main__':
    print(soma(5, 7))
    print(sub(5, b=7))
    