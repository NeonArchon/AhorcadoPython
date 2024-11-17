import tkinter as tk
from tkinter import ttk

#Aqui vamos a controlar las diferentes pantallas, mayormente transiciones

class Principal(tk.Tk):
    def __init__(self): #definir el constructor
        super().__init__() #llamade del constructor
        self.title("EL AHORCADO")
        self.geometry("600x400") #dimensiones del app
        self.resizable(False, False) #para que el tamano sea fijo
        self.show_pantalla_inicio() #para mostras la pantalla

    def MostrarPantallaInicio(self):
        frame = PantallaInicio(self)
        frame.pack(fill="both", expand = True)

    #def MostrarPantallaJuego(selfself, nombre, categoria):
    #    frame = PantallaJuego(selfself, nombre, categoria)
    #   frame.pack(fill="both", expand=True)

if __name__ == "__main__":
    app = Principal()
    app.mainloop()