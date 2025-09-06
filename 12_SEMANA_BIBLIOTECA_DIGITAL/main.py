# Punto de entrada principal con una interfaz de consola interactiva.

from modelos import Libro, Usuario
from biblioteca import Biblioteca

def mostrar_menu():
    # Imprime el menú de opciones para el usuario.
    print("\n--- Sistema de Gestión de Biblioteca Digital ---")
    print("1. Añadir un nuevo libro")
    print("2. Registrar un nuevo usuario")
    print("3. Prestar un libro")
    print("4. Devolver un libro")
    print("5. Buscar libros")
    print("6. Mostrar libros prestados a un usuario")
    print("7. Quitar un libro del catálogo")
    print("8. Dar de baja a un usuario")
    print("9. Salir")
    print("---------------------------------------------")

def main():
    # Función principal que ejecuta el bucle interactivo.
    biblioteca = Biblioteca() # Carga los datos al iniciar

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            # Opción para añadir un libro
            titulo = input("Ingrese el título del libro: ")
            autor = input("Ingrese el autor del libro: ")
            categoria = input("Ingrese la categoría del libro: ")
            isbn = input("Ingrese el ISBN del libro: ")
            libro = Libro(titulo, autor, categoria, isbn)
            biblioteca.anadir_libro(libro)

        elif opcion == '2':
            # Opción para registrar un usuario
            nombre = input("Ingrese el nombre del usuario: ")
            id_usuario = input("Ingrese el ID único para el usuario: ")
            usuario = Usuario(nombre, id_usuario)
            biblioteca.registrar_usuario(usuario)

        elif opcion == '3':
            # Opción para prestar un libro
            isbn = input("Ingrese el ISBN del libro a prestar: ")
            id_usuario = input("Ingrese el ID del usuario que lo presta: ")
            biblioteca.prestar_libro(isbn, id_usuario)

        elif opcion == '4':
            # Opción para devolver un libro
            isbn = input("Ingrese el ISBN del libro a devolver: ")
            id_usuario = input("Ingrese el ID del usuario que lo devuelve: ")
            biblioteca.devolver_libro(isbn, id_usuario)

        elif opcion == '5':
            # Opción para buscar libros
            criterio = input("Buscar por (titulo, autor, categoria): ").lower()
            if criterio in ['titulo', 'autor', 'categoria']:
                busqueda = input(f"Ingrese el {criterio} a buscar: ")
                biblioteca.buscar_libros(busqueda, por=criterio)
            else:
                print("Criterio de búsqueda no válido.")

        elif opcion == '6':
            # Opción para listar libros prestados
            id_usuario = input("Ingrese el ID del usuario para ver sus préstamos: ")
            biblioteca.listar_libros_prestados(id_usuario)

        elif opcion == '7':
            # Opción para quitar un libro
            isbn = input("Ingrese el ISBN del libro a eliminar del catálogo: ")
            biblioteca.quitar_libro(isbn)

        elif opcion == '8':
            # Opción para dar de baja a un usuario
            id_usuario = input("Ingrese el ID del usuario a dar de baja: ")
            biblioteca.dar_baja_usuario(id_usuario)

        elif opcion == '9':
            # Opción para salir del programa
            print("Saliendo del sistema. ¡Hasta pronto!")
            break

        else:
            # Manejo de opción no válida
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()