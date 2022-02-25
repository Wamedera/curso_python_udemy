#!/usr/local/bin/python3
from math import pi
import sys


def circulo(raio):
    area = pi*raio**2

    return area


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('É necessário informar o raio do círculo.')
        print(f'Sintaxe: {sys.argv[0]} <raio>')
    else:
        raio = sys.argv[1]
        area = circulo(raio)
    
        print(f'Área: {area}')
