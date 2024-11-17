import tkinter
import tkinter as tk



class PantallaInicio(tk.Frame):

    def __init__(self, parent):
        super(). __init__(parent, bg="#4e7a7c")
        #Titulo
        tkinter.Label(self, text="EL AHORCADO", font=("Arial", 24), bg="#4e7a7c", fg="black").pack(pady=10)

        #Para ingresar el nombre
        tk.Label(self, text="Escriba su nombre aqui", bg="#4e7a7c", fg="black").pack(pady=10)
        self.nombre_entry = tk.Entry(self, font=("Arial, 14"))

        #Botones para seleccionar categoria
        tk.Label(self, text="Elije una categoría", bg="#4e7a7c", fg="black").pack(pady=10)
        tk.Button(self, text="Fruta", bg="#58c3ff", command=lambda: self.IniciarJuego(parent,"Fruta")).pack(pady=5)
        tk.Button(self, text="Término Informático", bg="#58c3ff",command=lambda: self.IniciarJuego(parent, "Término Informático")).pack(pady=5)
        tk.Button(self, text="Nombres", bg="#58c3ff", command=lambda: self.IniciarJuego(parent, "Nombres")).pack(pady=5)

        #Boton de Salir
        tk.Button(self, text="Salir", bg="#58c3ff", command=parent.destroy).pack(pady=10)

    #con esto pasamos de la pantalla de inicio a la pantalla dejuego
    def IniciarJuego(self, parent, Categoria):
        nombre = self.nombre_entry.get()
        if nombre:
            self.destroy()
            #parent.show_pantalla_juego(nombre, categoria)
        else:
            tk.messagebox.showerror("Invalido", "Escriba un nombre par aseguir")