class Producto:
    # Esta clase representa un producto en nuestro inventario.

    # Atributos:
    # id (int): Un número único para identificar el producto.
    # nombre (str): El nombre del producto.
    # cantidad (int): Cuántas unidades tenemos de este producto.
    # precio (float): Cuánto cuesta una unidad del producto.

    def __init__(self, id, nombre, cantidad, precio):
        # El constructor guarda los datos iniciales de un nuevo producto.
        self._id = id
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    # --- Métodos para OBTENER información (Getters) ---
    def get_id(self):
        return self._id

    def get_nombre(self):
        return self._nombre

    def get_cantidad(self):
        return self._cantidad

    def get_precio(self):
        return self._precio

    # --- Métodos para ESTABLECER o cambiar información (Setters) ---
    def set_cantidad(self, cantidad):
        # Actualiza la cantidad, asegurando que no sea negativa.
        if cantidad >= 0:
            self._cantidad = cantidad
        else:
            print("Error: La cantidad no puede ser negativa.")

    def set_precio(self, precio):
        # Actualiza el precio, asegurando que no sea negativo.
        if precio >= 0:
            self._precio = precio
        else:
            print("Error: El precio no puede ser negativo.")

    def __str__(self):
        # Define cómo se mostrará el producto si lo imprimimos.
        return f"ID: {self._id}, Nombre: {self._nombre}, Cantidad: {self._cantidad}, Precio: ${self._precio:.2f}"