from producto import Producto

class Inventario:
    # Esta clase gestiona la colección de productos y su persistencia en un archivo de texto.
    def __init__(self, nombre_archivo='inventario.txt'):
        # CAMBIO: Usamos un diccionario para un acceso O(1) por ID.
        # La clave es el ID del producto, el valor es el objeto Producto.
        self.productos = {}
        self.nombre_archivo = nombre_archivo
        # Carga los datos del archivo de texto al iniciar el programa.
        self.cargar_inventario()

    def cargar_inventario(self):
        # Carga los productos desde el archivo de texto.
        try:
            with open(self.nombre_archivo, 'r') as f:
                for linea in f:
                    # Parsea cada línea (formato: id,nombre,cantidad,precio).
                    id_str, nombre, cantidad_str, precio_str = linea.strip().split(',')
                    id = int(id_str)
                    producto = Producto(id, nombre, int(cantidad_str), float(precio_str))
                    # CAMBIO: Añade el producto al diccionario usando su ID como clave.
                    self.productos[id] = producto
            print(f" Inventario cargado exitosamente desde '{self.nombre_archivo}'.")
        except FileNotFoundError:
            # Si el archivo no existe, informa y continúa (se creará al guardar).
            print(f"ℹ Archivo '{self.nombre_archivo}' no encontrado. Se creará uno nuevo.")
        except Exception as e:
            # Captura cualquier otro error durante la carga.
            print(f" Error inesperado al cargar el inventario: {e}")

    def guardar_inventario(self):
        # Guarda la lista actual de productos en el archivo de texto.
        try:
            with open(self.nombre_archivo, 'w') as f:
                # CAMBIO: Iteramos sobre los valores del diccionario.
                for producto in self.productos.values():
                    # Formatea cada producto en una línea separada por comas.
                    linea = f"{producto.get_id()},{producto.get_nombre()},{producto.get_cantidad()},{producto.get_precio()}\n"
                    f.write(linea)
        except Exception as e:
            print(f" Error inesperado al guardar el inventario: {e}")

    def agregar_producto(self, producto):
        # Añade un producto y guarda el estado actual en el archivo de texto.
        id_producto = producto.get_id()
        # CAMBIO: La verificación de existencia es ahora O(1).
        if id_producto not in self.productos:
            self.productos[id_producto] = producto
            self.guardar_inventario() # Guarda los cambios
            print(f" Producto '{producto.get_nombre()}' añadido y guardado en el archivo.")
        else:
            print(f" Error: El ID '{id_producto}' ya existe.")

    def eliminar_producto(self, id):
        # Elimina un producto y guarda el estado actual en el archivo de texto.
        # CAMBIO: La eliminación es directa y O(1).
        if id in self.productos:
            del self.productos[id]
            self.guardar_inventario() # Guarda los cambios
            print(f" Producto con ID '{id}' eliminado y guardado en el archivo.")
        else:
            print(f" Error: No se encontró un producto con el ID '{id}'.")

    def actualizar_producto(self, id, nueva_cantidad=None, nuevo_precio=None):
        # Actualiza un producto y guarda el estado actual en el archivo de texto.
        # CAMBIO: El acceso al producto es directo y O(1).
        if id in self.productos:
            producto_encontrado = self.productos[id]
            if nueva_cantidad is not None:
                producto_encontrado.set_cantidad(nueva_cantidad)
            if nuevo_precio is not None:
                producto_encontrado.set_precio(nuevo_precio)
            self.guardar_inventario() # Guarda los cambios
            print(f" Producto con ID '{id}' actualizado y guardado en el archivo.")
        else:
            print(f" Error: No se encontró un producto con el ID '{id}'.")

    def buscar_producto(self, nombre):
        # Busca productos por nombre. La búsqueda por nombre sigue siendo O(n)
        # ya que debemos revisar todos los productos.
        resultados = [p for p in self.productos.values() if nombre.lower() in p.get_nombre().lower()]
        if resultados:
            print("\n--- Resultados de la Búsqueda ---")
            for producto in resultados:
                print(producto)
            print("---------------------------------")
        else:
            print(f"️ℹ No se encontraron productos que coincidan con '{nombre}'.")

    def mostrar_inventario(self):
        # Muestra todos los productos que hay actualmente en el inventario.
        print("\n--- Inventario Actual ---")
        if not self.productos:
            print("El inventario está vacío.")
        else:
            # CAMBIO: Iteramos sobre los valores del diccionario.
            for producto in self.productos.values():
                print(producto)
        print("-------------------------")