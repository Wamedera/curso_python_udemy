arquivo = open('D:\curso_python_udemy\manipulacao_arquivos\pessoas.csv')
dados = arquivo.read()
arquivo.close()

for registro in dados.splitlines():
    print('Nome: {}, Idade: {}'.format(*registro.split(',')))
    