
import pandas as pd
import os
from producto import Producto


class Inventario:
    """
    Gestiona la colección de productos, usando un archivo Excel para la persistencia de datos.
    """

    def __init__(self, archivo='inventario.xlsx'):
        self.archivo = archivo
        self.productos = {}
        self.cargar_inventario()

    def agregar_producto(self, producto):
        if producto.get_id() in self.productos:
            return False
        self.productos[producto.get_id()] = producto
        self.guardar_inventario()
        return True

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.guardar_inventario()
            return True
        return False

    def modificar_producto(self, id_producto, nuevo_nombre, nueva_cantidad, nuevo_precio):
        if id_producto in self.productos:
            producto = self.productos[id_producto]
            producto.set_nombre(nuevo_nombre)
            producto.set_cantidad(nueva_cantidad)
            producto.set_precio(nuevo_precio)
            self.guardar_inventario()
            return True
        return False

    def obtener_producto(self, id_producto):
        return self.productos.get(id_producto, None)

    def obtener_todos_los_productos(self):
        return list(self.productos.values())

    def guardar_inventario(self):
        """Guarda el inventario actual en un archivo Excel."""
        if not self.productos:
            if os.path.exists(self.archivo):
                os.remove(self.archivo)
            df = pd.DataFrame(columns=["id", "nombre", "cantidad", "precio"])
            df.to_excel(self.archivo, index=False, engine='openpyxl')
            return

        lista_de_productos = [p.to_dict() for p in self.productos.values()]
        df = pd.DataFrame(lista_de_productos)
        df.to_excel(self.archivo, index=False, engine='openpyxl')

    def cargar_inventario(self):
        """Carga el inventario desde un archivo Excel al iniciar."""
        try:
            df = pd.read_excel(self.archivo, engine='openpyxl')
            df['id'] = df['id'].astype(str)

            for index, fila in df.iterrows():
                producto = Producto(
                    fila['id'],
                    fila['nombre'],
                    int(fila['cantidad']),
                    float(fila['precio'])
                )
                self.productos[producto.get_id()] = producto
        except FileNotFoundError:
            print("Archivo de inventario no encontrado. Se creará uno nuevo al guardar.")
        except Exception as e:
            print(f"Ocurrió un error al cargar el inventario: {e}")