import pandas as pd
import os
from producto import Producto


class Inventario:
    """
    Gestiona la colección de productos, usando un archivo Excel para la persistencia de datos.
    """

    def __init__(self, archivo='inventario.xlsx'):
        self.archivo = archivo
        # La colección de productos, las claves deben ser strings
        self.productos = {}
        self.cargar_inventario()

    def agregar_producto(self, producto):
        # Aseguramos que la clave sea siempre una cadena (str)
        id_str = str(producto.get_id())

        if id_str in self.productos:
            return False
        self.productos[id_str] = producto
        self.guardar_inventario()
        return True

    def eliminar_producto(self, id_producto):
        """
        [CORRECCIÓN]: Se asegura que el ID de búsqueda sea siempre str.
        """
        id_busqueda = str(id_producto)

        if id_busqueda in self.productos:
            del self.productos[id_busqueda]
            self.guardar_inventario()
            return True
        return False

    def modificar_producto(self, id_producto, nuevo_nombre, nueva_cantidad, nuevo_precio):
        # Aseguramos que la clave sea siempre una cadena (str)
        id_busqueda = str(id_producto)

        if id_busqueda in self.productos:
            producto = self.productos[id_busqueda]
            producto.set_nombre(nuevo_nombre)
            producto.set_cantidad(nueva_cantidad)
            producto.set_precio(nuevo_precio)
            self.guardar_inventario()
            return True
        return False

    def obtener_producto(self, id_producto):
        # Aseguramos que la clave sea siempre una cadena (str) al obtener
        return self.productos.get(str(id_producto), None)

    def obtener_todos_los_productos(self):
        return list(self.productos.values())

    def guardar_inventario(self):
        """Guarda el inventario actual en un archivo Excel."""
        if not self.productos:
            if os.path.exists(self.archivo):
                # Opcional: solo eliminamos el archivo si está vacío para evitar errores
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
            # Es vital asegurar que la columna ID sea SIEMPRE STRING (cadena de texto)
            df['id'] = df['id'].astype(str)

            for index, fila in df.iterrows():
                producto = Producto(
                    fila['id'],  # Es string
                    fila['nombre'],
                    int(fila['cantidad']),
                    float(fila['precio'])
                )
                self.productos[producto.get_id()] = producto
        except FileNotFoundError:
            # Pasa silenciosamente si no encuentra el archivo (se creará al guardar)
            pass
        except Exception as e:
            # Pasa silenciosamente si hay otro error de carga, para que la app se abra
            # print(f"Ocurrió un error al cargar el inventario: {e}")
            pass