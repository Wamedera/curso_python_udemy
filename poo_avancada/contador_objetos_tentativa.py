class ClasseSimples:
    contador = 0

    @classmethod
    def __init__(cls):
        cls.contador += 1


if __name__ == '__main__':
    lista = [ClasseSimples(), ClasseSimples()]
    print(ClasseSimples.contador)  # esperado 2
