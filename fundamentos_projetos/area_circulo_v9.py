#!/usr/local/bin/python3
from math import pi


def circulo(raio):
    area = pi*raio**2

    return area


if __name__ == '__main__':
    raio = float(input('Digite o raio: '))
    area = circulo(raio)

    print(f'Área: {area}')
