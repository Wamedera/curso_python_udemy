# implementação simplificada do map


def mapear(funcao, lista):
    for i in lista:
        yield funcao(i)


if __name__ == '__main__':
    '''
    generator retorna várias vezes, ao ser convertido para o tipo lista,
    é necessário puxar todos os valores de uma vez, porém caso a função
    mapear() fosse chamada a partir da função next, os valores seriam
    gerados um de cada vez, tornando a chamada mais eficiente, lembrando
    que para execução do next, é necessário atribuir a função mapear()
    a uma variável, para que guarde as etapas da execução

    resultado = mapear(lambda x: x ** 2, [2, 3, 4])
    print(next(resultado))
    print(next(resultado))
    print(next(resultado))
    '''
    print(list(mapear(lambda x: x ** 2, [2, 3, 4])))
