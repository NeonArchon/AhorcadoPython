import mysql.connector

# Configuración de conexión a la base de datos
def conectar_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="AhorcadoSQL"
    )
