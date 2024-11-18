import tkinter
import tkinter as tk
from tkinter import messagebox
from Conexion import ConexionBD


class PantallaInicio(tk.Frame):

    def __init__(self, parent):
        super(). __init__(parent, bg="#f9e10d")

        #Titulo
        tkinter.Label(self, text="EL AHORCADO", font=("Arial", 24), bg="#f9e10d", fg="black").pack(pady=10)

        #Para ingresar el nombre
        tk.Label(self, text="Escriba su nombre aqui", bg="#f9e10d", fg="black").pack(pady=10)
        self.nombre_entry = tk.Entry(self, font=("Arial, 14"))
        #area para colocar el nombre
        self.nombre_entry = tk.Entry(self, font=("Arial", 14))  # El widget Entry para el nombre
        self.nombre_entry.pack(pady=14)  # Colocarlo en la interfaz

        #boton para añadir el nombre
        tk.Button(self, text="Añadir Nombre", bg="#21bfec",command=self.validar_nombre, width=18, height=1).pack(pady=5)


        #Botones para seleccionar categoria
        tk.Label(self, text="Elije una tematica", bg="#f9e10d", fg="black").pack(pady=10)
        tk.Button(self, text="Frutas", bg="#21bfec", command=lambda: self.IniciarJuego(parent,"Fruta"),width=18, height=1).pack(pady=5)
        tk.Button(self, text="Terminos Informaticos", bg="#21bfec",command=lambda: self.IniciarJuego(parent, "Término Informático"), width=18, height=1).pack(pady=5)
        tk.Button(self, text="Nombres", bg="#21bfec", command=lambda: self.IniciarJuego(parent, "Nombres"), width=18, height=1).pack(pady=5)

        #Boton de Salir
        tk.Button(self, text="Salir", bg="#ef4a00", command=parent.destroy, width=18, height=1).pack(pady=10)

    #Metodo para validar el nombre
    def validar_nombre(self):
        nombre = self.nombre_entry.get()
        if not nombre.strip():
            tk.messagebox.showerror("Error", "Por favor, ingrese un nombre válido.")
        else:
            tk.messagebox.showinfo("Nombre registrado", f"¡Hola, {nombre}!")

    #Metodo para pasar de la pantalla de inicio a la pantalla dejuego
    def IniciarJuego(self, parent, Categoria):
        #Captar nombre del jugador
        nombre = self.nombre_entry.get().strip()

        #Validar si en nombre no esta vacio
        if not nombre:
            messagebox.showerror("Nombe no ingresad","Debe ingresar un nombre para seguir")
            return

        if nombre:
            self.destroy()
            parent.PantallaJuego(nombre, Categoria)
        else:
            tk.messagebox.showerror("Invalido", "Escriba un nombre para seguir")