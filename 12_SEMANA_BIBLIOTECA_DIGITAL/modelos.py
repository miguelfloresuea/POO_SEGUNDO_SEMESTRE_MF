# Este módulo define las clases de modelo de datos: Libro y Usuario.

class Libro:
    # Representa un libro en la biblioteca con sus atributos principales.
    def __init__(self, titulo: str, autor: str, categoria: str, isbn: str):
        self.info_libro = (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self) -> str:
        return f'"{self.info_libro[0]}" de {self.info_libro[1]} (ISBN: {self.isbn})'

class Usuario:
    # Representa a un usuario de la biblioteca.
    def __init__(self, nombre: str, id_usuario: str):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def __str__(self) -> str:
        return f'Usuario: {self.nombre} (ID: {self.id_usuario})'