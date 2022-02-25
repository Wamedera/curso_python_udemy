#!/usr/local/bin/python3
from math import pi


def circulo(raio):
    area = pi*raio**2

    print(f'Área: {area}')


if __name__ == '__main__':
    raio = float(input('Digite o raio: '))
    circulo(raio)
