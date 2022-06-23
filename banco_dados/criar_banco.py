from mysql.connector import connect

conexao = connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='gustavo',
    auth_plugin='mysql_native_password'
)

cursor = conexao.cursor()
# create database if not exists agenda
cursor.execute('create database agenda')
