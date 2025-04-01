import mysql.connector
from mysql.connector import Error

# Configurações do banco de dados
dbname = "delivery"
user = "root"
password = "admin"
host = "localhost"

try:
    # Conecta ao MySQL
    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password
    )
    
    # Cria o cursor
    cur = conn.cursor()
    
    # Cria o banco de dados
    cur.execute("CREATE DATABASE IF NOT EXISTS delivery")
    print("Banco de dados 'delivery' criado com sucesso!")
    
    # Seleciona o banco de dados
    cur.execute("USE delivery")
    
    # Cria a tabela pedido
    cur.execute("""
        CREATE TABLE IF NOT EXISTS pedido (
            id INT NOT NULL AUTO_INCREMENT,
            cliente VARCHAR(100) NOT NULL,
            produto VARCHAR(100) NOT NULL,
            valor FLOAT NOT NULL,
            CONSTRAINT pedido PRIMARY KEY(id)
        ) ENGINE = InnoDB AUTO_INCREMENT = 1
    """)
    
    print("Tabela 'pedido' criada com sucesso!")
    
    # Commit das alterações
    conn.commit()
    
except Error as e:
    print(f"Erro ao executar os comandos: {e}")
finally:
    if 'conn' in locals() and conn.is_connected():
        cur.close()
        conn.close()
        print("Conexão com o MySQL fechada") 