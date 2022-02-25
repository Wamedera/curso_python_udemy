import csv

with open('D:\curso_python_udemy\manipulacao_arquivos\pessoas.csv') as arquivo:
    for pessoa in csv.reader(arquivo):
        print('Nome: {}, Idade: {}'.format(*pessoa))
