from locale import setlocale, LC_ALL
from calendar import mdays, month_name
from functools import reduce


# português do Brasil
setlocale(LC_ALL, 'pt_BR')

# listar todos os meses do ano com 31 dias
# 1.(filter)pegar os índices de todos os meses com 31 dias
# 2.(map)transformar os índices em nome
# 3.(reduce)juntar tudo para imprimir
meses_31 = filter(lambda mes: mdays[mes] == 31, range(13))
meses_nomes = map(lambda mes: month_name[mes], meses_31)
juntar_meses = reduce(lambda todos, nome: f'{todos}\n- {nome}',
                      meses_nomes, 'Meses com 31 dias:')

print(juntar_meses)
