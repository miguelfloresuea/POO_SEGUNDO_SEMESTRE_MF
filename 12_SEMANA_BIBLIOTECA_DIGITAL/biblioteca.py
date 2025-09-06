
# Gestiona la lógica del sistema y la persistencia de datos en biblioteca.txt.

import json
from modelos import Libro, Usuario

class Biblioteca:
    # Gestiona las colecciones y la persistencia de datos en un archivo .txt con formato JSON.
    def __init__(self, archivo_datos: str = 'biblioteca.txt'):
        self.archivo_datos = archivo_datos
        self.catalogo_libros = {}
        self.usuarios = {}
        self.cargar_datos()

    def cargar_datos(self):
        # Carga los datos desde el archivo biblioteca.txt.
        try:
            with open(self.archivo_datos, 'r', encoding='utf-8') as f:
                datos = json.load(f)
                for isbn, data_libro in datos.get('libros', {}).items():
                    self.catalogo_libros[isbn] = Libro(data_libro['titulo'], data_libro['autor'], data_libro['categoria'], isbn)
                for id_usuario, data_usuario in datos.get('usuarios', {}).items():
                    usuario = Usuario(data_usuario['nombre'], id_usuario)
                    for data_libro_prestado in data_usuario.get('libros_prestados', []):
                        libro_prestado = Libro(data_libro_prestado['titulo'], data_libro_prestado['autor'], data_libro_prestado['categoria'], data_libro_prestado['isbn'])
                        usuario.libros_prestados.append(libro_prestado)
                    self.usuarios[id_usuario] = usuario
            print(f"Datos cargados desde '{self.archivo_datos}'.")
        except (FileNotFoundError, json.JSONDecodeError):
            print(f"Archivo '{self.archivo_datos}' no encontrado o vacío. Se creará uno nuevo al guardar.")
            self.catalogo_libros = {}
            self.usuarios = {}

    def guardar_datos(self):
        # Guarda el estado actual de la biblioteca en el archivo biblioteca.txt.
        datos_a_guardar = {'libros': {}, 'usuarios': {}}
        for isbn, libro in self.catalogo_libros.items():
            datos_a_guardar['libros'][isbn] = {'titulo': libro.info_libro[0], 'autor': libro.info_libro[1], 'categoria': libro.categoria}
        for id_usuario, usuario in self.usuarios.items():
            datos_a_guardar['usuarios'][id_usuario] = {
                'nombre': usuario.nombre,
                'libros_prestados': [{'titulo': lp.info_libro[0], 'autor': lp.info_libro[1], 'categoria': lp.categoria, 'isbn': lp.isbn} for lp in usuario.libros_prestados]
            }
        with open(self.archivo_datos, 'w', encoding='utf-8') as f:
            json.dump(datos_a_guardar, f, indent=4, ensure_ascii=False)
        print("-> Datos guardados automáticamente.")

    def anadir_libro(self, libro: Libro):
        if libro.isbn in self.catalogo_libros:
            print(f"Error: El libro con ISBN {libro.isbn} ya existe.")
        else:
            self.catalogo_libros[libro.isbn] = libro
            print(f"Libro '{libro.info_libro[0]}' añadido al catálogo.")
            self.guardar_datos()

    def quitar_libro(self, isbn: str):
        if isbn in self.catalogo_libros:
            libro_removido = self.catalogo_libros.pop(isbn)
            print(f"Libro '{libro_removido.info_libro[0]}' eliminado del catálogo.")
            self.guardar_datos()
        else:
            print(f"Error: No se encontró el libro con ISBN {isbn}.")

    def registrar_usuario(self, usuario: Usuario):
        if usuario.id_usuario in self.usuarios:
            print(f"Error: El ID de usuario '{usuario.id_usuario}' ya está registrado.")
        else:
            self.usuarios[usuario.id_usuario] = usuario
            print(f"Usuario '{usuario.nombre}' registrado exitosamente.")
            self.guardar_datos()

    def dar_baja_usuario(self, id_usuario: str):
        if id_usuario in self.usuarios:
            if not self.usuarios[id_usuario].libros_prestados:
                usuario_eliminado = self.usuarios.pop(id_usuario)
                print(f"Usuario '{usuario_eliminado.nombre}' ha sido dado de baja.")
                self.guardar_datos()
            else:
                print("Error: El usuario debe devolver todos sus libros antes de darse de baja.")
        else:
            print(f"Error: No se encontró el usuario con ID {id_usuario}.")

    def prestar_libro(self, isbn: str, id_usuario: str):
        if isbn in self.catalogo_libros and id_usuario in self.usuarios:
            libro = self.catalogo_libros.pop(isbn)
            self.usuarios[id_usuario].libros_prestados.append(libro)
            print(f"El libro '{libro.info_libro[0]}' ha sido prestado a {self.usuarios[id_usuario].nombre}.")
            self.guardar_datos()
        else:
            print("Error: Libro no disponible o usuario no encontrado.")

    def devolver_libro(self, isbn: str, id_usuario: str):
        usuario = self.usuarios.get(id_usuario)
        if not usuario:
            print(f"Error: Usuario no encontrado.")
            return
        libro_a_devolver = next((libro for libro in usuario.libros_prestados if libro.isbn == isbn), None)
        if libro_a_devolver:
            usuario.libros_prestados.remove(libro_a_devolver)
            self.catalogo_libros[isbn] = libro_a_devolver
            print(f"El libro '{libro_a_devolver.info_libro[0]}' ha sido devuelto.")
            self.guardar_datos()
        else:
            print("Error: El usuario no tiene prestado un libro con ese ISBN.")

    def buscar_libros(self, query: str, por: str = 'titulo'):
        todos_los_libros = list(self.catalogo_libros.values())
        for u in self.usuarios.values():
            todos_los_libros.extend(u.libros_prestados)
        resultados = []
        if por == 'titulo':
            resultados = [lib for lib in todos_los_libros if query.lower() in lib.info_libro[0].lower()]
        elif por == 'autor':
            resultados = [lib for lib in todos_los_libros if query.lower() in lib.info_libro[1].lower()]
        elif por == 'categoria':
            resultados = [lib for lib in todos_los_libros if query.lower() == lib.categoria.lower()]
        print(f"\n--- Resultados de búsqueda por '{por}': '{query}' ---")
        if resultados:
            for libro in resultados:
                print(f"  - {libro}")
        else:
            print("No se encontraron libros.")
        print("-" * 40)

    def listar_libros_prestados(self, id_usuario: str):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            print(f"\n--- Libros prestados a {usuario.nombre} ---")
            if usuario.libros_prestados:
                for libro in usuario.libros_prestados:
                    print(f"  - {libro}")
            else:
                print("Este usuario no tiene libros en préstamo.")
            print("-" * 40)
        else:
            print("Error: Usuario no encontrado.")