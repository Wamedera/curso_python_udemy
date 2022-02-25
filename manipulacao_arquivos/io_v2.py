arquivo = open('D:\curso_python_udemy\manipulacao_arquivos\pessoas.csv')
for registro in arquivo:
    print('Nome: {}, Idade: {}'.format(*registro.split(',')))

arquivo.close()