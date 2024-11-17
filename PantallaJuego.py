import tkinter
import tkinter as tk

class PantallaJuego(tk.Frame):


    def __init__(self, parent, nombre, categoria):
        super().__init__(parent, bg="#4e7a7c")
        # Titulo
        tkinter.Label(self, text="EL AHORCADO", font=("Arial", 24), bg="#4e7a7c", fg="black").pack(pady=10)

        #Informacion del jugador
        tk.Label(self, text=f"Adivine la palabra, {nombre}", bg="#4e7a7c", fg="black").pack(pady=5)
        tk.Label(self, text=f"Categoría: {categoria}", bg="#4e7a7c", fg="black").pack(pady=5)

        #Espacio de las letras
        tk.Entry(self, font=("Arial", 14)).pack(pady=5)

        #Espacio para progreso (placehorlder por ahora
        tk.Label(self, text="Palabra: _ _ _ _ _ _", bg="#4e7a7c", fg="black", font=("Arial", 18)).pack(pady=10)

        #Estadisticas
        tk.Label(self, text="Juegos: 0", bg="#4e7a7c", fg="black").pack()
        tk.Label(self, text="Aciertos: 0", bg="#4e7a7c", fg="black").pack()
        tk.Label(self, text="Fallos: 0", bg="#4e7a7c", fg="black").pack()

        # Botón Volver
        tk.Button(self, text="Volver", bg="#58c3ff", command=lambda: self.VolverAlInicio(parent)).pack(pady=10)


    def VolverAlInicio(self, parent):
        self.destroy()
        parent.show_pantalla_inicio()
