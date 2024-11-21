import tkinter as tk
from tkinter import messagebox
import mysql.connector
import pip
from PIL import Image, ImageTk
from PIL.FontFile import WIDTH

from Conexion import conectar_db

# Variables globales
palabra = ""
letras_adivinadas = []
intentos = 0
nombre_jugador = ""

# Función para obtener una palabra aleatoria de la base de datos según categoría
def obtener_palabra_aleatoria(categoria):
    try:
        conexion = conectar_db()
        cursor = conexion.cursor()
        cursor.execute("SELECT Palabra FROM Tematica WHERE Categoria = %s ORDER BY RAND() LIMIT 1", (categoria,))
        resultado = cursor.fetchone()
        conexion.close()
        return resultado[0] if resultado else None
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"No se pudo conectar a la base de datos: {e}")
        return None

# Función para registrar un jugador si no existe
def registrar_jugador(nombre):
    try:
        conexion = conectar_db()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM Jugadores WHERE NombreJugador = %s", (nombre,))
        if not cursor.fetchone():  # Si no existe el jugador
            cursor.execute("INSERT INTO Jugadores (NombreJugador) VALUES (%s)", (nombre,))
        conexion.commit()
        conexion.close()
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"No se pudo registrar al jugador: {e}")

# Función para actualizar estadísticas del jugador
def actualizar_estadisticas(nombre, victoria):
    try:
        conexion = conectar_db()
        cursor = conexion.cursor()
        if victoria:
            cursor.execute("""
                UPDATE Jugadores 
                SET NumPartidas = NumPartidas + 1, Victorias = Victorias + 1 
                WHERE NombreJugador = %s
            """, (nombre,))
        else:
            cursor.execute("""
                UPDATE Jugadores 
                SET NumPartidas = NumPartidas + 1, Derrotas = Derrotas + 1 
                WHERE NombreJugador = %s
            """, (nombre,))
        conexion.commit()
        conexion.close()
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"No se pudieron actualizar las estadísticas: {e}")

# Función para iniciar el juego
def iniciar_juego(categoria):
    global palabra, letras_adivinadas, intentos
    palabra = obtener_palabra_aleatoria(categoria)
    if not palabra:
        messagebox.showerror("Error", "No se encontraron palabras en la categoría seleccionada.")
        return
    letras_adivinadas = []
    intentos = 0
    ImagenesAhorcado(intentos)
    actualizar_tablero()
    frame1.pack_forget()
    frame2.pack()

# Función para verificar la letra ingresada
def verificar_letra():
    global intentos
    letra = entry_letra.get()
    entry_letra.delete(0, tk.END)
    label_imagen = tk.Label(frame2, bg="#4E7C7E")
    label_imagen.pack(pady=10)

    #logica para mostrar imagenes
    imagenes = []
    for i in range(7):
        try:
            img = Image.open(f"imagenes/Ahorcado0{i}.png")  # Ruta de las imágenes
            img = img.resize((150, 150))  # Redimensionar la imagen
            imagenes.append(ImageTk.PhotoImage(img))
        except FileNotFoundError:
            print(f"Advertencia: No se encontró la imagen imagenes/Ahorcado_0{i}.png")
            imagenes.append(None)


    if len(letra) != 1 or not letra.isalpha():
        messagebox.showerror("Error", "Por favor, ingresa una sola letra válida.")
        return

    if letra in letras_adivinadas:
        messagebox.showwarning("Advertencia", "Ya ingresaste esta letra.")
        return

    letras_adivinadas.append(letra)

    if letra not in palabra:
        intentos += 1
  #      label_imagen.config(image=imagenes[intentos]) # Actualiza la imagen
        ImagenesAhorcado(intentos)

    actualizar_tablero()

    if intentos == 6:
        messagebox.showinfo("Derrota", f"Perdiste. La palabra era: {palabra}")
        actualizar_estadisticas(nombre_jugador, False)
        reiniciar_juego()
    elif all(letra in letras_adivinadas for letra in palabra):
        messagebox.showinfo("Victoria", "Has adivinado la palabra.")
        actualizar_estadisticas(nombre_jugador, True)
        reiniciar_juego()

# Función para actualizar el tablero
def actualizar_tablero():
    estado = " ".join([letra if letra in letras_adivinadas else "_" for letra in palabra])
    label_tablero.config(text=estado)
    label_intentos.config(text=f"Intentos: {intentos}/6")


#funcion para mostrar imagenes
def ImagenesAhorcado(intentos):

    try:

        if intentos == 0:
            f"imagenes/Ahorcado00.png"

        # Construir la ruta de la imagen automáticamente
        ruta_imagen = f"imagenes/Ahorcado0{intentos}.png"

        # Cargar y redimensionar la imagen
        img = Image.open(ruta_imagen).resize((150, 150))

        # Convertir a un objeto compatible con Tkinter
        img_tk = ImageTk.PhotoImage(img)

        # Mostrar la imagen en el label
        label_imagen.config(image=img_tk)
        label_imagen.image = img_tk  # Mantener referencia para evitar el recolector de basura



    except FileNotFoundError:
        # Mostrar un mensaje de error
        messagebox.showerror("Error", f"No se encontró la imagen")
        # Usar una imagen de error predeterminada (opcional)
        img_tk = None


# Función para reiniciar el juego
def reiniciar_juego():
    frame2.pack_forget()
    frame1.pack()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("El Ahorcado")
ventana.geometry("400x500")
ventana.configure(bg="#00e5fc")

# Frame inicial (Frame 1)
frame1 = tk.Frame(ventana, bg="#00e5fc")
frame1.pack()

label_titulo = tk.Label(frame1, text="El Ahorcado", font=("Arial", 24, "bold"), bg="#00e5fc", fg="black")
label_titulo.pack(pady=10)

label_nombre = tk.Label(frame1, text="Escribe tu nombre", bg="#00e5fc", fg="black", font=("Arial", 12))
label_nombre.pack(pady=5)

entry_nombre = tk.Entry(frame1, font=("Arial", 12))
entry_nombre.pack(pady=5)


#metodo para iniciar
def comenzar_juego(categoria):
    global nombre_jugador
    nombre_jugador = entry_nombre.get().strip()
    if not nombre_jugador:
        messagebox.showerror("Error", "Debes ingresar un nombre para jugar.")
        return
    registrar_jugador(nombre_jugador)
    iniciar_juego(categoria)

label_categoria = tk.Label(frame1, text="Elije una categoría", bg="#00e5fc", fg="black", font=("Arial", 12))
label_categoria.pack(pady=10)

boton_fruta = tk.Button(frame1, text="Frutas", bg="#02c3ff",width=18, height=1, command=lambda: comenzar_juego("Frutas"))
boton_fruta.pack(pady=5)

boton_termino = tk.Button(frame1, text="Conceptos Informáticos", bg="#02c3ff",width=18, height=1, command=lambda: comenzar_juego("Conceptos Informáticos"))
boton_termino.pack(pady=5)

boton_nombres = tk.Button(frame1, text="Nombres", bg="#02c3ff",width=18, height=1, command=lambda: comenzar_juego("Nombres"))
boton_nombres.pack(pady=5)

boton_salir = tk.Button(frame1, text="Salir", bg="#e42500",width=18, height=1, command=ventana.quit)
boton_salir.pack(pady=10)

# Frame del juego (Frame 2)
frame2 = tk.Frame(ventana, bg="#00e5fc")

label_titulo_juego = tk.Label(frame2, text="El Ahorcado", font=("Arial", 24, "bold"), bg="#00e5fc", fg="black")
label_titulo_juego.pack(pady=10)

label_tablero = tk.Label(frame2, text="", font=("Courier", 18, "bold"), bg="#00e5fc", fg="white")
label_tablero.pack(pady=20)

# Frame para mostrar la imagen
label_imagen = tk.Label(frame2, bg="#e8feff")
label_imagen.pack(pady=10)

entry_letra = tk.Entry(frame2, font=("Arial", 12))
entry_letra.pack(pady=5)

boton_verificar = tk.Button(frame2, text="Verificar Letra", bg="#02c3ff",width=18, height=1, command=verificar_letra)
boton_verificar.pack(pady=10)

label_intentos = tk.Label(frame2, text="Intentos: 0/6", bg="#00e5fc", fg="white", font=("Arial", 12))
label_intentos.pack(pady=10)

boton_volver = tk.Button(frame2, text="Volver", bg="#53f015", width=18, height=1, command=reiniciar_juego)
boton_volver.pack(pady=10)

ventana.mainloop()