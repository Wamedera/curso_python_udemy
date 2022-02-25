import csv
from urllib import request

def read(url):
    with request.urlopen(url) as arquivo:
        print('Baixando arquivo')
        dados = arquivo.read().decode('latin1')
        print('Download completo!')
        for cidade in csv.reader(dados.splitlines()):
            print(f'{cidade[3]}: {cidade[8]}')


if __name__ == '__main__':
    read(r'http://files.cod3r.com.br/curso-python/desafio-ibge.csv')
