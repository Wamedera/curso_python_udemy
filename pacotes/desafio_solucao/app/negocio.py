NOMES = ['João', 'Maria', 'José', 'Ana']

def backend():
    def add_nome(nome):
        NOMES.append(nome)

def nome_existe(nome):
    return True if nome in NOMES else False
    