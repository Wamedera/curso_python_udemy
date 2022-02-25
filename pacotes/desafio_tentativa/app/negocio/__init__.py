NOMES = ['João', 'Maria', 'José', 'Ana']
  

def nome_existe(nome):
    return True if nome in NOMES else False


__all__ = ['nome_existe']
