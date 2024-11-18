import tkinter as tk
from tkinter import ttk
from Conexion import ConexionBD
from PantallaInicio import PantallaInicio
from PantallaJuego import PantallaJuego


#Aqui vamos a controlar las diferentes pantallas, mayormente transiciones

class Principal(tk.Tk):
    def __init__(self): #definir el constructor
        super().__init__() #llamade del constructor
        self.title("EL AHORCADO")
        self.geometry("450x600") #dimensiones del app
        self.resizable(False, False) #para que el tamano sea fijo
        self.PantallaInicio() #para mostras la pantalla

    def PantallaInicio(self):
        frame = PantallaInicio(self)
        frame.pack(fill="both", expand = True)

    def PantallaJuego(selfself, nombre, categoria):
        frame = PantallaJuego(selfself, nombre, categoria)
        frame.pack(fill="both", expand=True)


if __name__ == "__main__":
    app = Principal()
    app.mainloop()