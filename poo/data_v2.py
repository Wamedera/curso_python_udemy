class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano


    def __str__(self):
        return f'{self.dia}/{self.mes}/{self.ano}'


d1 = Data(5, 2, 2022)
print(d1)

d2 = Data(7, 12, 2021)
d2.mes = 11
print(d2)
