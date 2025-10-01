# Archivo: main.py

import tkinter as tk
from tkinter import ttk, messagebox
from producto import Producto
from inventario import Inventario


class VentanaProductos(tk.Toplevel):
    """
    Ventana para la gestión de productos (CRUD).
    """

    def __init__(self, parent):
        super().__init__(parent)
        self.inventario = Inventario()
        self.parent = parent

        self.title("Gestión de Productos")
        self.geometry("800x600")
        self.protocol("WM_DELETE_WINDOW", self.cerrar)

        frame_controles = ttk.LabelFrame(self, text="Datos del Producto")
        frame_controles.pack(fill="x", padx=10, pady=10)

        ttk.Label(frame_controles, text="ID:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.id_entry = ttk.Entry(frame_controles)
        self.id_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        ttk.Label(frame_controles, text="Nombre:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.nombre_entry = ttk.Entry(frame_controles)
        self.nombre_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        ttk.Label(frame_controles, text="Cantidad:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.cantidad_entry = ttk.Entry(frame_controles)
        self.cantidad_entry.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

        ttk.Label(frame_controles, text="Precio:").grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.precio_entry = ttk.Entry(frame_controles)
        self.precio_entry.grid(row=3, column=1, padx=5, pady=5, sticky="ew")

        frame_botones = ttk.Frame(self)
        frame_botones.pack(fill="x", padx=10, pady=5)

        ttk.Button(frame_botones, text="Agregar", command=self.agregar_producto).pack(side="left", fill="x",
                                                                                      expand=True, padx=5)
        ttk.Button(frame_botones, text="Modificar", command=self.modificar_producto).pack(side="left", fill="x",
                                                                                          expand=True, padx=5)
        ttk.Button(frame_botones, text="Eliminar", command=self.eliminar_producto).pack(side="left", fill="x",
                                                                                        expand=True, padx=5)
        ttk.Button(frame_botones, text="Limpiar Campos", command=self.limpiar_campos).pack(side="left", fill="x",
                                                                                           expand=True, padx=5)

        self.tree = ttk.Treeview(self, columns=("ID", "Nombre", "Cantidad", "Precio"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Cantidad", text="Cantidad")
        self.tree.heading("Precio", text="Precio")
        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

        self.tree.bind("<<TreeviewSelect>>", self.seleccionar_item)
        self.tree.bind("<Delete>", self.eliminar_producto_con_tecla)

        self.actualizar_treeview()

    def actualizar_treeview(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for producto in self.inventario.obtener_todos_los_productos():
            self.tree.insert("", "end", values=(producto.get_id(), producto.get_nombre(), producto.get_cantidad(),
                                                f"{producto.get_precio():.2f}"))

    def agregar_producto(self):
        try:
            id_prod = self.id_entry.get()
            nombre = self.nombre_entry.get()
            cantidad = int(self.cantidad_entry.get())
            precio = float(self.precio_entry.get())

            if not all([id_prod, nombre]):
                messagebox.showwarning("Campos Vacíos", "ID y Nombre son campos obligatorios.")
                return

            producto = Producto(id_prod, nombre, cantidad, precio)
            if self.inventario.agregar_producto(producto):
                messagebox.showinfo("Éxito", "Producto agregado correctamente.")
                self.actualizar_treeview()
                self.limpiar_campos()
            else:
                messagebox.showerror("Error", f"El producto con ID '{id_prod}' ya existe.")
        except ValueError:
            messagebox.showerror("Error de Formato", "Cantidad y Precio deben ser números válidos.")

    def modificar_producto(self):
        if not self.tree.focus():
            messagebox.showwarning("Sin Selección", "Por favor, seleccione un producto para modificar.")
            return
        try:
            id_prod = self.id_entry.get()
            nombre = self.nombre_entry.get()
            cantidad = int(self.cantidad_entry.get())
            precio = float(self.precio_entry.get())

            if self.inventario.modificar_producto(id_prod, nombre, cantidad, precio):
                messagebox.showinfo("Éxito", "Producto modificado correctamente.")
                self.actualizar_treeview()
                self.limpiar_campos()
            else:
                messagebox.showerror("Error", f"No se encontró un producto con ID '{id_prod}'.")
        except ValueError:
            messagebox.showerror("Error de Formato", "Cantidad y Precio deben ser números válidos.")

    def eliminar_producto(self):
        if not self.tree.focus():
            messagebox.showwarning("Sin Selección", "Por favor, seleccione un producto para eliminar.")
            return

        id_prod = self.tree.item(self.tree.focus())['values'][0]

        if messagebox.askyesno("Confirmar Eliminación",
                               f"¿Está seguro de que desea eliminar el producto con ID '{id_prod}'?"):
            if self.inventario.eliminar_producto(id_prod):
                messagebox.showinfo("Éxito", "Producto eliminado correctamente.")
                self.actualizar_treeview()
                self.limpiar_campos()
            else:
                messagebox.showerror("Error", "No se pudo eliminar el producto.")

    def eliminar_producto_con_tecla(self, event):
        self.eliminar_producto()

    def seleccionar_item(self, event):
        if self.tree.focus():
            valores = self.tree.item(self.tree.focus())['values']
            self.limpiar_campos()
            self.id_entry.insert(0, valores[0])
            self.nombre_entry.insert(0, valores[1])
            self.cantidad_entry.insert(0, valores[2])
            self.precio_entry.insert(0, valores[3])

    def limpiar_campos(self):
        self.id_entry.delete(0, tk.END)
        self.nombre_entry.delete(0, tk.END)
        self.cantidad_entry.delete(0, tk.END)
        self.precio_entry.delete(0, tk.END)
        if self.tree.selection():
            self.tree.selection_remove(self.tree.selection()[0])

    def cerrar(self):
        self.parent.deiconify()
        self.destroy()


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Gestión de Inventario")
        self.geometry("600x450")

        frame_info = ttk.LabelFrame(self, text="Información del Proyecto")
        frame_info.pack(padx=20, pady=20, fill="x")

        ttk.Label(frame_info, text="TEMA:", font=("Helvetica", 12, "bold")).pack(pady=(10, 0))
        ttk.Label(frame_info, text="SISTEMA DE GESTIÓN DE INVENTARIO", font=("Helvetica", 12)).pack()
        ttk.Label(frame_info, text="INTEGRANTES:", font=("Helvetica", 12, "bold")).pack(pady=(15, 0))
        ttk.Label(frame_info, text="MIGUEL ÁNGEL FLORES YÉPEZ", font=("Helvetica", 12)).pack()
        ttk.Label(frame_info, text="JESSICA PAOLA PESANTEZ TUAPANTE", font=("Helvetica", 12)).pack()
        ttk.Label(frame_info, text="ASIGNATURA:", font=("Helvetica", 12, "bold")).pack(pady=(15, 0))
        ttk.Label(frame_info, text="PROGRAMACIÓN ORIENTADA A OBJETOS", font=("Helvetica", 12)).pack()
        ttk.Label(frame_info, text="CARRERA:", font=("Helvetica", 12, "bold")).pack(pady=(15, 0))
        ttk.Label(frame_info, text="TECNOLOGÍAS DE LA INFORMACIÓN - PARALELO 'A'", font=("Helvetica", 12)).pack(
            pady=(0, 10))

        frame_botones = ttk.Frame(self)
        frame_botones.pack(padx=20, pady=10, fill='x', expand=True)

        btn_acceder = ttk.Button(frame_botones, text="Gestionar Inventario", command=self.abrir_productos)
        btn_acceder.pack(side='left', fill='x', expand=True, padx=5)

        btn_salir = ttk.Button(frame_botones, text="Salir", command=self.quit)
        btn_salir.pack(side='left', fill='x', expand=True, padx=5)

        # --- SECCIÓN DEL MENÚ SUPERIOR ELIMINADA ---
        # El código que creaba la barra de menú "Opciones" ha sido removido.

        # Atajo de teclado: Tecla "Escape" para cerrar la app (se mantiene)
        self.bind("<Escape>", lambda event: self.quit())

    def abrir_productos(self):
        self.withdraw()
        ventana_prod = VentanaProductos(self)
        ventana_prod.grab_set()


if __name__ == "__main__":
    app = App()
    app.mainloop()