# Clase que representa un producto
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre  # Nombre del producto
        self.precio = precio  # Precio del producto

# Clase que representa el carrito de compras
class Carrito:
    def __init__(self):
        self.productos = []  # Lista donde se almacenan los productos agregados

    def agregar_producto(self, producto):
        # Agrega un producto a la lista
        self.productos.append(producto)
        print(f"Producto '{producto.nombre}' agregado al carrito.")

    def mostrar_carrito(self):
        # Muestra los productos dentro del carrito y el total a pagar
        if not self.productos:
            print("El carrito está vacío.")
            return

        print("\nProductos en el carrito:")
        total = 0
        for p in self.productos:
            print(f"- {p.nombre}: ${p.precio}")
            total += p.precio
        print(f"Total a pagar: ${total}")

# Programa principal
carrito = Carrito()

# Menú interactivo
while True:
    print("\n--- Menú de Tienda ---")
    print("1. Agregar producto al carrito")
    print("2. Ver carrito")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        # Solicita nombre y precio al usuario
        nombre = input("Nombre del producto: ")
        precio = float(input("Precio del producto: "))
        producto = Producto(nombre, precio)
        carrito.agregar_producto(producto)

    elif opcion == "2":
        # Muestra el contenido del carrito
        carrito.mostrar_carrito()

    elif opcion == "3":
        print("Gracias por usar la tienda. ¡Hasta pronto!")
        break

    else:
        print("Opción inválida. Intente nuevamente.")