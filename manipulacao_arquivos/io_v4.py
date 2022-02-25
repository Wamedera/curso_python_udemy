try:
    arquivo = open('D:\curso_python_udemy\manipulacao_arquivos\pessoas.csv')
  
    for registro in arquivo:
        print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))
finally:
    arquivo.close()

if arquivo.closed:
    print('O arquivo foi fechado!')
    