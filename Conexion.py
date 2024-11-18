import mysql.connector
import self


class ConexionBD:
    def __init__(self):
        self.con = mysql.connector.connect(
        host ="localhost",
        user ="root",
        passwd = "",
        dabatase ="AhorcadoSQL",
        port = "3306"
        )

self.cursor = self.con.cursor()

def Consulta (self, consulta, parametros=None):
    self.cursor.execute(consulta, parametros or ())
    return self.cursor.fetchall()


def Desconectar (self):
    self.cursor.close()
    self.conn.close()
