with open('D:\curso_python_udemy\manipulacao_arquivos\pessoas.csv') as arquivo:
    for registro in arquivo:
        print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))

if arquivo.closed:
    print('O arquivo foi fechado!')
    