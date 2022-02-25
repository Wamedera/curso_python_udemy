#!/usr/local/bin/python3
from math import pi
import sys


def circulo(raio):
    area = pi*raio**2

    return area


if __name__ == '__main__':
    raio = sys.argv[1]
    area = circulo(raio)

    print(f'Área: {area}')
