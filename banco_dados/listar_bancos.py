from mysql.connector import connect

conexao = connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='gustavo',
    auth_plugin='mysql_native_password'
)

cursor = conexao.cursor()
cursor.execute('show databases')

for i, database in enumerate(cursor, start=1):
    print(f'Banco de Dados {i}: {database[0]}')
