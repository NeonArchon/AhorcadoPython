import tkinter
import tkinter as tk
from Conexion import ConexionBD

class PantallaJuego(tk.Frame):


    def __init__(self, parent, nombre, categoria):
        super().__init__(parent, bg="#f9e10d")
        # Titulo
        tkinter.Label(self, text="EL AHORCADO", font=("Arial", 24), bg="#f9e10d", fg="black").pack(pady=10)

        #Informacion del jugador
        tk.Label(self, text=f"Adivine la palabra, {nombre}", bg="#f9e10d", fg="black").pack(pady=5)
        tk.Label(self, text=f"Categoría: {categoria}", bg="#f9e10d", fg="black").pack(pady=5)

        #Espacio de las letras
        tk.Entry(self, font=("Arial", 14)).pack(pady=5)

        #Espacio para progreso (placehorlder por ahora)
        tk.Label(self, text="Palabra: _ _ _ _ _ _", bg="#fffefd", fg="black", font=("Arial", 18)).pack(pady=10)



        #Estadisticas
        tk.Label(self, text="Juegos: 0", bg="#f9e10d", fg="black").pack()
        tk.Label(self, text="Aciertos: 0", bg="#f9e10d", fg="black").pack()
        tk.Label(self, text="Fallos: 0", bg="#f9e10d", fg="black").pack()

        # Botón para Salir
        # Boton de Salir
        tk.Button(self, text="Salir", bg="#ef4a00", command=parent.destroy, width=18, height=1).pack(pady=10)


    def VolverAlInicio(self, parent):
        self.destroy()
        parent.show_pantalla_inicio()
