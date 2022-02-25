from datetime import datetime, timedelta


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f'Cliente: {self.nome}.\nIdade: {self.idade}.'

    def is_adulto(self):
        return True if self.idade >= 18 else False


class Compra:
    def __init__(self, vendedor, data, valor):
        self.vendedor = vendedor
        self.data = data
        self.valor = valor


class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.compras = []

    def regitrar_compra(self, compra):
        self.compras.append(compra)

    def get_data_ultima_compra(self):
        return self.compras[-1].data

    def total_compras(self):
        return len(self.compras)


class Vendedor(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario


def main():
    vendedor_jr1 = Vendedor('José', 32, 1500.0)
    vendedor_pl1 = Vendedor('Pietra', 27, 1900.0)
    print(vendedor_jr1)
    print(vendedor_pl1)

    compra1 = Compra(vendedor_jr1, datetime.now() - timedelta(days=7), 30.0)
    compra2 = Compra(vendedor_jr1, datetime.now() - timedelta(days=5), 7.5)
    compra3 = Compra(vendedor_pl1, datetime.now() - timedelta(days=3), 92.3)
    compra4 = Compra(vendedor_pl1, datetime.now() - timedelta(days=1), 24.0)

    cliente = Cliente('Pedro', 15)
    cliente.regitrar_compra(compra1)
    cliente.regitrar_compra(compra2)
    cliente.regitrar_compra(compra3)
    cliente.regitrar_compra(compra4)
    print(f'Data da última compra: {cliente.get_data_ultima_compra()}')
    print(f'Total de compras de {cliente.nome}: {cliente.total_compras()}')


if __name__ == '__main__':
    main()
