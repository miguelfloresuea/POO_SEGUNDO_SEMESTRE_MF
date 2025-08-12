
from producto import Producto

class Inventario:
    # Esta clase gestiona toda la colección de productos.
    def __init__(self):
        # El inventario comienza con una lista de productos vacía.
        self.productos = []

    def _id_existe(self, id):
        # Metodo auxiliar para verificar si un ID ya está en uso.
        for producto in self.productos:
            if producto.get_id() == id:
                return True
        return False

    def agregar_producto(self, producto):
        # Añade un producto nuevo solo si el ID no está repetido.
        if not self._id_existe(producto.get_id()):
            self.productos.append(producto)
            print(f" Producto '{producto.get_nombre()}' añadido exitosamente.")
        else:
            print(f" Error: El ID '{producto.get_id()}' ya existe.")

    def eliminar_producto(self, id):
        # Elimina un producto de la lista usando su ID.
        producto_a_eliminar = next((p for p in self.productos if p.get_id() == id), None)
        if producto_a_eliminar:
            self.productos.remove(producto_a_eliminar)
            print(f" Producto con ID '{id}' eliminado exitosamente.")
        else:
            print(f" Error: No se encontró un producto con el ID '{id}'.")

    def actualizar_producto(self, id, nueva_cantidad=None, nuevo_precio=None):
        # Encuentra un producto por ID y actualiza su cantidad y/o precio.
        producto_encontrado = next((p for p in self.productos if p.get_id() == id), None)
        if producto_encontrado:
            if nueva_cantidad is not None:
                producto_encontrado.set_cantidad(nueva_cantidad)
            if nuevo_precio is not None:
                producto_encontrado.set_precio(nuevo_precio)
            print(f" Producto con ID '{id}' actualizado exitosamente.")
        else:
            print(f" Error: No se encontró un producto con el ID '{id}'.")

    def buscar_producto(self, nombre):
        # Busca productos por nombre sin diferenciar mayúsculas de minúsculas.
        resultados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        if resultados:
            print("\n--- Resultados de la Búsqueda ---")
            for producto in resultados:
                print(producto)
            print("-FIN-")
        else:
            print(f"️ No se encontraron productos que coincidan con '{nombre}'.")

    def mostrar_inventario(self):
        # Muestra todos los productos que hay actualmente en el inventario.
        print("\n--- Inventario Actual ---")
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos:
                print(producto)
        print("-FIN-")