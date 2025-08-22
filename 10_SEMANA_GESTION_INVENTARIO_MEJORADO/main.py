from producto import Producto
from inventario import Inventario

def mostrar_menu():
    # Esta función solo imprime las opciones del menú.
    print("\n--- Sistema de Gestión de Inventarios ---")
    print("1. Añadir nuevo producto")
    print("2. Eliminar producto por ID")
    print("3. Actualizar producto por ID")
    print("4. Buscar producto por nombre")
    print("5. Mostrar todos los productos")
    print("6. Salir")
    print("---------------------------------------")

def main():
    # La función principal que controla el programa.
    # Al crear la instancia, automáticamente carga el inventario desde 'inventario.txt'.
    inventario = Inventario()

    # Se eliminaron los productos de ejemplo. El inventario se carga desde el archivo.

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        try:
            # Opción 1: Añadir un producto nuevo.
            if opcion == '1':
                print("\n--- Añadir Nuevo Producto ---")
                id = int(input("Ingrese ID del producto: "))
                nombre = input("Ingrese nombre del producto: ")
                cantidad = int(input("Ingrese cantidad del producto: "))
                precio = float(input("Ingrese precio del producto: "))
                inventario.agregar_producto(Producto(id, nombre, cantidad, precio))

            # Opción 2: Eliminar un producto por su ID.
            elif opcion == '2':
                print("\n--- Eliminar Producto ---")
                id = int(input("Ingrese el ID del producto a eliminar: "))
                inventario.eliminar_producto(id)

            # Opción 3: Actualizar un producto.
            elif opcion == '3':
                print("\n--- Actualizar Producto ---")
                id = int(input("Ingrese el ID del producto a actualizar: "))
                cantidad_str = input("Ingrese nueva cantidad (Enter para no cambiar): ")
                precio_str = input("Ingrese nuevo precio (Enter para no cambiar): ")
                nueva_cantidad = int(cantidad_str) if cantidad_str else None
                nuevo_precio = float(precio_str) if precio_str else None
                if nueva_cantidad is not None or nuevo_precio is not None:
                    inventario.actualizar_producto(id, nueva_cantidad, nuevo_precio)
                else:
                    print("ℹ No se proporcionaron datos para actualizar.")

            # Opción 4: Buscar productos por nombre.
            elif opcion == '4':
                print("\n--- Buscar Producto ---")
                nombre = input("Ingrese el nombre a buscar: ")
                inventario.buscar_producto(nombre)

            # Opción 5: Mostrar todos los productos.
            elif opcion == '5':
                inventario.mostrar_inventario()

            # Opción 6: Salir del programa.
            elif opcion == '6':
                print("👋 Saliendo del sistema. ¡Hasta pronto!")
                break

            # Si el usuario ingresa una opción no válida.
            else:
                print(" Opción no válida. Por favor, intente de nuevo.")

        # Manejo de errores si el usuario ingresa letras en lugar de números.
        except ValueError:
            print(" Error: Entrada inválida. Asegúrese de ingresar números donde se requiera.")

        # Manejo de cualquier otro error inesperado.
        except Exception as e:
            print(f" Ocurrió un error inesperado: {e}")

# Esta línea asegura que la función main() se ejecute al correr el script.
if __name__ == "__main__":
    main()