from locale import setlocale, LC_ALL
from calendar import mdays, month_name
from functools import reduce


# português do Brasil
setlocale(LC_ALL, 'pt_BR')


def mes_com_31(mes):
    return mdays[mes] == 31


def get_nome_mes(mes):
    return month_name[mes]


def juntar_meses(todos, nome):
    return f'{todos}\n- {nome}'


print(reduce(juntar_meses,
             map(get_nome_mes, filter(mes_com_31, range(13))),
             'Meses com 31 dias:'))
