"""""
Programa: Sistema de Registro de Biblioteca
Asignatura: Programación Orientada a Objetos
Autor: Miguel Flores
Descripción:
Este programa permite registrar libros en una biblioteca, mostrar el catálogo
y buscar si un libro específico está disponible o no.
Aplica el uso de clases, objetos, tipos de datos  y buenas prácticas.
"""""

# Definimos la clase Libro, que representa cada libro dentro de la biblioteca.
class Libro:
    def __init__(self, titulo: str, autor: str, anio_publicacion: int, precio: float, disponible: bool):
        # Atributos de la clase Libro usando distintos tipos de datos
        self.titulo = titulo                  # Cadena de texto
        self.autor = autor                    # Cadena de texto
        self.anio_publicacion = anio_publicacion  # Entero
        self.precio = precio                  # Flotante
        self.disponible = disponible          # Booleano (verdadero/falso

    def mostrar_detalles(self):
        # Muestra la información del libro
        estado = "Disponible" if self.disponible else "Prestado"
        print(f"- {self.titulo} ({self.anio_publicacion}) por {self.autor} - ${self.precio:.2f} - Estado: {estado}")


# Clase Biblioteca, que contiene y gestiona una lista de libros (objetos de la clase Libro)
class Biblioteca:
    def __init__(self):
        # Inicializa un catálogo vacío (lista) para almacenar libros
        self.catalogo_libros = []

    def agregar_libro(self, libro: Libro):
        # Agrega un objeto de tipo Libro al catálogo
        self.catalogo_libros.append(libro)

    def mostrar_catalogo(self):
        # Muestra todos los libros registrados en la biblioteca
        print("Catálogo de Libros:")
        if not self.catalogo_libros:
            print("No hay libros registrados.")  # Si la lista está vacía
        else:
            for libro in self.catalogo_libros:
                libro.mostrar_detalles()         # Llama al metodo de cada libro

    def buscar_libro_por_titulo(self, titulo_buscado: str):
        # Busca un libro por su título (sin importar mayúsculas/minúsculas)
        for libro in self.catalogo_libros:
            if libro.titulo.lower() == titulo_buscado.lower():
                estado = "disponible" if libro.disponible else "no disponible"
                print(f"El libro '{libro.titulo}' está {estado} y cuesta ${libro.precio:.2f}.")
                return
        # Si no se encuentra el libro
        print(f"El libro '{titulo_buscado}' no se encuentra en el catálogo.")


# Función principal que se ejecuta al iniciar el programa
def main():
    # Se crea un objeto Biblioteca
    biblioteca = Biblioteca()

    # Se agregan libros con valores ya definidos
    biblioteca.agregar_libro(Libro("Fisica", "Newton", 1990, 9.99, True))
    biblioteca.agregar_libro(Libro("Matematica", "Baldor", 1980, 14.50, False))

    # Muestra el catálogo completo de libros
    biblioteca.mostrar_catalogo()

# Ejecuta el programa
if __name__ == "__main__":
    main()
