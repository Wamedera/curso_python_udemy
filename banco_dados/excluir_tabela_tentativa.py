from mysql.connector import ProgrammingError
from db import nova_conexao

drop = """
    drop table emails
"""

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(drop)
    except ProgrammingError as e:
            print(f'erro: {e.msg}')
