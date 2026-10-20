# =============================================================================
# TP 11 - Acceso a datos
# Sistema de Gestión de Biblioteca (POO + SQLite)
# Alumno: Bautista Cano
# =============================================================================

import os
import sqlite3

NOMBRE_BD = "biblioteca.db"


# =============================================================================
# EJERCICIO 1: MODELADO DE CLASES (POO)
# =============================================================================
class Autor:
    def __init__(self, id_autor, nombre, nacionalidad):
        self.id_autor = id_autor
        self.nombre = nombre
        self.nacionalidad = nacionalidad

    def __str__(self):
        return f"Autor #{self.id_autor}: {self.nombre} ({self.nacionalidad})"


class Libro:
    def __init__(self, id_libro, titulo, anio_publicacion, autor):
        self.id_libro = id_libro
        self.titulo = titulo
        self.anio_publicacion = anio_publicacion
        self.autor = autor      # Agregación: el libro "tiene un" objeto Autor

    def __str__(self):
        return (f"Libro #{self.id_libro}: '{self.titulo}' "
                f"({self.anio_publicacion}) - de {self.autor.nombre}")


# =============================================================================
# EJERCICIO 2: CREACIÓN DEL ESQUEMA EN LA BASE DE DATOS
# =============================================================================
def conectar():
    """Abre la conexión con la base de datos y activa las claves foráneas."""
    conexion = sqlite3.connect(NOMBRE_BD)
    # SQLite no controla las claves foráneas si no se activa esta opción
    conexion.execute("PRAGMA foreign_keys = ON")
    return conexion


def inicializar_bd():
    """Crea el archivo biblioteca.db con las tablas autores y libros."""
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS autores (
            id           INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre       TEXT,
            nacionalidad TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS libros (
            id       INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo   TEXT,
            anio     INTEGER,
            autor_id INTEGER,
            FOREIGN KEY (autor_id) REFERENCES autores(id)
        )
    """)

    conexion.commit()
    conexion.close()
    print("Base de datos inicializada correctamente.")


# =============================================================================
# EJERCICIO 3: REPOSITORIO CRUD
# =============================================================================
def registrar_autor(nombre, nacionalidad):
    """Inserta un autor y retorna el ID que le asignó la base de datos."""
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute(
        "INSERT INTO autores (nombre, nacionalidad) VALUES (?, ?)",
        (nombre, nacionalidad)
    )
    conexion.commit()
    id_generado = cursor.lastrowid
    conexion.close()
    return id_generado


def registrar_libro(titulo, anio, autor_id):
    """Inserta un libro vinculado a un autor. Retorna el ID del libro."""
    conexion = conectar()
    cursor = conexion.cursor()
    try:
        cursor.execute(
            "INSERT INTO libros (titulo, anio, autor_id) VALUES (?, ?, ?)",
            (titulo, anio, autor_id)
        )
        conexion.commit()
        return cursor.lastrowid
    except sqlite3.IntegrityError:
        # Pasa si el autor_id no existe en la tabla autores
        print(f"Error: no existe un autor con id {autor_id}.")
        return None
    finally:
        conexion.close()


def listar_libros():
    """Muestra título, año y autor de cada libro (SELECT con JOIN).
    También devuelve la lista de filas."""
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("""
        SELECT libros.id, libros.titulo, libros.anio, autores.nombre
        FROM libros
        JOIN autores ON libros.autor_id = autores.id
        ORDER BY libros.id
    """)
    filas = cursor.fetchall()
    conexion.close()

    print(f"{'ID':<4}{'Título':<42}{'Año':<8}{'Autor'}")
    print("-" * 72)
    if len(filas) == 0:
        print("(No hay libros registrados)")
    for fila in filas:
        print(f"{fila[0]:<4}{fila[1]:<42}{fila[2]:<8}{fila[3]}")
    return filas


def actualizar_titulo_libro(id_libro, nuevo_titulo):
    """Actualiza el título de un libro. Devuelve True si lo encontró."""
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute(
        "UPDATE libros SET titulo = ? WHERE id = ?",
        (nuevo_titulo, id_libro)
    )
    conexion.commit()
    modificado = cursor.rowcount > 0    # rowcount = cantidad de filas afectadas
    conexion.close()
    return modificado


def eliminar_libro(id_libro):
    """Elimina un libro por su ID. Devuelve True si lo encontró."""
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM libros WHERE id = ?", (id_libro,))
    conexion.commit()
    eliminado = cursor.rowcount > 0
    conexion.close()
    return eliminado


def obtener_libro(id_libro):
    """Busca un libro por ID y lo devuelve como objeto Libro (con su Autor).
    Si no existe devuelve None. Sirve para verificar los cambios."""
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("""
        SELECT libros.id, libros.titulo, libros.anio,
               autores.id, autores.nombre, autores.nacionalidad
        FROM libros
        JOIN autores ON libros.autor_id = autores.id
        WHERE libros.id = ?
    """, (id_libro,))
    fila = cursor.fetchone()
    conexion.close()

    if fila is None:
        return None
    autor = Autor(fila[3], fila[4], fila[5])
    return Libro(fila[0], fila[1], fila[2], autor)


# =============================================================================
# EJERCICIO 4: INTEGRACIÓN Y PRUEBA INTEGRAL
# =============================================================================
if __name__ == '__main__':
    # Se borra la base anterior para que cada ejecución arranque de cero
    # y no se dupliquen los datos de prueba.
    if os.path.exists(NOMBRE_BD):
        os.remove(NOMBRE_BD)

    # 1. Inicializar la base de datos
    print("\n=== 1. INICIALIZACIÓN ===")
    inicializar_bd()

    # 2. Registrar 2 autores y 3 libros
    print("\n=== 2. REGISTRO DE AUTORES Y LIBROS ===")
    id_borges = registrar_autor("Jorge Luis Borges", "Argentina")
    id_garcia = registrar_autor("Gabriel García Márquez", "Colombia")
    print(f"Autores registrados con ID {id_borges} y {id_garcia}.")

    id_libro1 = registrar_libro("El Aleph", 1949, id_borges)
    id_libro2 = registrar_libro("Ficciones", 1944, id_borges)
    id_libro3 = registrar_libro("Cien años de soledad", 1967, id_garcia)
    print(f"Libros registrados con ID {id_libro1}, {id_libro2} y {id_libro3}.")

    # 3. Listar todos los libros
    print("\n=== 3. LISTADO DE LIBROS ===")
    listar_libros()

    # 4. Actualizar un título y verificar el cambio
    print("\n=== 4. ACTUALIZACIÓN DE TÍTULO ===")
    print("Antes: ", obtener_libro(id_libro3))
    actualizar_titulo_libro(id_libro3, "Cien años de soledad (Edición especial)")
    print("Después:", obtener_libro(id_libro3))

    # 5. Eliminar un libro y mostrar el listado resultante
    print("\n=== 5. ELIMINACIÓN DE UN LIBRO ===")
    if eliminar_libro(id_libro2):
        print(f"Libro con ID {id_libro2} eliminado.")
    listar_libros()
