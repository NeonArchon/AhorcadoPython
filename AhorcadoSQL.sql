-- Eliminar la base de datos si ya existe
-- DROP DATABASE IF EXISTS AhorcadoSQL;

-- Crear la base de datos
CREATE DATABASE AhorcadoSQL;

-- Usar la base de datos
USE AhorcadoSQL;

-- Crear la tabla de jugadores
CREATE TABLE Jugadores (
    IdJugador INT AUTO_INCREMENT PRIMARY KEY, 
    NombreJugador VARCHAR(30) NOT NULL,       
    NumPartidas INT DEFAULT 0,                
    Victorias INT DEFAULT 0,                  
    Derrotas INT DEFAULT 0                    
);

-- Crear la tabla de temáticas y palabras
CREATE TABLE Tematica (
    Categoria VARCHAR(30) NOT NULL,            
    Palabra VARCHAR(30) NOT NULL               
);

-- Insertar datos en la tabla Tematica
INSERT INTO Tematica (Categoria, Palabra) VALUES
-- Frutas
('Frutas', 'manzana'),
('Frutas', 'maracuyá'),
('Frutas', 'banana'),
('Frutas', 'kiwi'),
('Frutas', 'naranja'),
('Frutas', 'uva'),
('Frutas', 'piña'),
('Frutas', 'fresa'),
('Frutas', 'mango'),
('Frutas', 'cereza'),
-- Conceptos Informáticos
('Conceptos Informáticos', 'algoritmo'),
('Conceptos Informáticos', 'recursividad'),
('Conceptos Informáticos', 'bucle'),
('Conceptos Informáticos', 'encriptación'),
('Conceptos Informáticos', 'metodo'),
('Conceptos Informáticos', 'variable'),
('Conceptos Informáticos', 'función'),
('Conceptos Informáticos', 'objeto'),
('Conceptos Informáticos', 'clase'),
('Conceptos Informáticos', 'herencia'),

-- Nombres
('Nombres', 'juan'),
('Nombres', 'pepe'),
('Nombres', 'maría'),
('Nombres', 'andrea'),
('Nombres', 'indigo'),
('Nombres', 'sofía'),
('Nombres', 'lucas'),
('Nombres', 'valentina'),
('Nombres', 'benjamin'),
('Nombres', 'clara');

SELECT * FROM Jugadores;