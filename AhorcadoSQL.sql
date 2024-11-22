-- Eliminar la base de datos si ya existe
DROP DATABASE IF EXISTS AhorcadoSQL;

-- Crear la base de datos
CREATE DATABASE AhorcadoSQL;

-- Usar la base de datos
USE AhorcadoSQL;

-- tabla de jugadores
CREATE TABLE Jugadores (
    IdJugador INT AUTO_INCREMENT PRIMARY KEY, 
    NombreJugador VARCHAR(30) NOT NULL,       
    NumPartidas INT DEFAULT 0,                
    Victorias INT DEFAULT 0,                  
    Derrotas INT DEFAULT 0                    
);
 -- tabla de juego
CREATE TABLE Juego (
    IdJuego INT AUTO_INCREMENT PRIMARY KEY,
    IdJugador INT NOT NULL,
    FOREIGN KEY (IdJugador) REFERENCES Jugadores (IdJugador)
);

-- tabla de temáticas y palabras
CREATE TABLE Tematica (
    Categoria VARCHAR(30) NOT NULL,            
    Palabra VARCHAR(30) NOT NULL,
    IdCategoria INT NOT NULL,
    IdJuego INT,
    FOREIGN KEY (IdJuego) REFERENCES Juego (IdJuego)
);

-- Insertar datos en la tabla Tematica
INSERT INTO Tematica (Categoria, Palabra, IdCategoria) VALUES
('Frutas', 'manzana', 1),
('Frutas', 'maracuyá', 1),
('Frutas', 'banana', 1),
('Frutas', 'kiwi', 1),
('Frutas', 'naranja', 1),
('Frutas', 'uva', 1),
('Frutas', 'piña', 1),
('Frutas', 'fresa', 1),
('Frutas', 'mango', 1),
('Frutas', 'cereza', 1),
('Conceptos Informáticos', 'algoritmo', 2),
('Conceptos Informáticos', 'recursividad', 2),
('Conceptos Informáticos', 'bucle', 2),
('Conceptos Informáticos', 'encriptación', 2),
('Conceptos Informáticos', 'metodo', 2),
('Conceptos Informáticos', 'variable', 2),
('Conceptos Informáticos', 'función', 2),
('Conceptos Informáticos', 'objeto', 2),
('Conceptos Informáticos', 'clase', 2),
('Conceptos Informáticos', 'herencia', 2),
('Nombres', 'juan', 3),
('Nombres', 'pepe', 3),
('Nombres', 'maría', 3),
('Nombres', 'andrea', 3),
('Nombres', 'indigo', 3),
('Nombres', 'sofía', 3),
('Nombres', 'lucas', 3),
('Nombres', 'valentina', 3),
('Nombres', 'benjamin', 3),
('Nombres', 'clara', 3);

SELECT * FROM Jugadores;