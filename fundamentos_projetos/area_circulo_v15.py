#!/usr/local/bin/python3
from math import pi
import sys
import errno


class TerminalColor:
    ERRO = '\033[91m'
    NORMAL = '\033[0m'


def help():
    print('É necessário informar o raio do círculo.')
    print(f'Sintaxe: {sys.argv[0]} <raio>')


def circulo(raio):
    area = pi*raio**2

    return area


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
        sys.exit(errno.EPERM)
    elif not sys.argv[1].isnumeric():
        help()
        print(TerminalColor.ERRO, 'O raio deve ser um valor numérico.',
            TerminalColor.NORMAL)
        sys.exit(errno.EINVAL)
        
    raio = sys.argv[1]
    area = circulo(raio)
    
    print(f'Área: {area}')
