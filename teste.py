# class abstrata(object):
#     def metodo(self):
#         raise "Esse método precisa ser implementado na classe filha"


# class concreta(abstrata):
#     def metodo(self):
#         return "implementei com sucesso"

# batata = abstrata()

# print(batata.metodo())


def funcao(numero, lista_divisores):
    divisores_comuns = []
    for div in lista_divisores:
        if numero % div == 0:
            divisores_comuns.append(div)
    return divisores_comuns


print(funcao(512, range(1, 10)))
