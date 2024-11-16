import mysql

Conexion = mysql.connector.connect(
    host ="localhost",
    user ="root",
    passwd = "",
    dabatase ="AhorcadoPython",
    port = "3306"

)

cursor = Conexion.cursor()

micursor = Conexion.cursor()

#micursor.execute("SELECT * FROM Clientes")

print(micursor.fetchall())