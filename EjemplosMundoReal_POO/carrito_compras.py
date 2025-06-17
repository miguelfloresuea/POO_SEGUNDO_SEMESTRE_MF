# Clase que representa un producto
class Producto:
    def __init__(self, nombre, precio):
        # Constructor que inicializa el nombre y precio del producto
        self.nombre = nombre  # Nombre del producto
        self.precio = precio  # Precio del producto

# Clase que representa el carrito de compras
class Carrito:
    def __init__(self):
        # Constructor que inicializa la lista de productos en el carrito
        self.productos = []  # Lista donde se almacenan los productos agregados

    def agregar_producto(self, producto):
        # Metodo que agrega un producto a la lista del carrito
        self.productos.append(producto)  # Añade el producto a la lista
        print(f"Producto '{producto.nombre}' agregado al carrito.")  # Confirma al usuario

    def mostrar_carrito(self):
        # Metodo que muestra los productos del carrito y el total a pagar
        if not self.productos:
            print("El carrito está vacío.")  # Si no hay productos, lo indica
            return

        print("\nProductos en el carrito:")
        total = 0  # Variable para calcular el total
        for p in self.productos:
            print(f"- {p.nombre}: ${p.precio}")  # Muestra nombre y precio de cada producto
            total += p.precio  # Suma el precio al total
        print(f"Total a pagar: ${total}")  # Muestra el total acumulado

# Programa principal: se crea una instancia del carrito
carrito = Carrito()

# Bucle del menú interactivo
while True:
    # Muestra las opciones del menú al usuario
    print("\n--- Menú de Tienda ---")
    print("1. Agregar producto al carrito")
    print("2. Ver carrito")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")  # Captura la opción del usuario

    if opcion == "1":
        # Opción para agregar un producto
        nombre = input("Nombre del producto: ")  # Pide el nombre
        precio = float(input("Precio del producto: "))  # Pide el precio (convertido a float)
        producto = Producto(nombre, precio)  # Crea una instancia de Producto
        carrito.agregar_producto(producto)  # Agrega el producto al carrito

    elif opcion == "2":
        # Opción para mostrar el contenido del carrito
        carrito.mostrar_carrito()

    elif opcion == "3":
        # Opción para salir del programa
        print("Gracias por usar la tienda. ¡Hasta pronto!")
        break  # Termina el bucle

    else:
        # Si la opción no es válida
        print("Opción inválida. Intente nuevamente.")