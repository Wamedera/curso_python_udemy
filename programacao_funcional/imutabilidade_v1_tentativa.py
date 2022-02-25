from locale import setlocale, LC_ALL
from calendar import mdays, month_name
from functools import reduce
from operator import index


# português do Brasil
setlocale(LC_ALL, 'pt_BR')

# listar todos os meses do ano com 31 dias
mes_dias = []
for i in range(13):
    mes_dias.append({'mes': month_name[i], 'dias': mdays[i]})

print(mes_dias)
