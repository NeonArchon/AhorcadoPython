import mysql.connector

# Configuración de conexión a la base de datos
def conectar_db():
    return mysql.connector.connect(
        host="localhost",       # Cambia si tu base de datos está en otro host
        user="root",            # Tu usuario de MySQL
        password="",    # Tu contraseña
        database="AhorcadoSQL"  # La base de datos creada
    )
