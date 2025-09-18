import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry  # Importar el DatePicker


class AgendaApp:
    def __init__(self, root):

        # Constructor de la clase AgendaApp.
        # Inicializa la ventana principal y los componentes de la GUI.

        self.root = root
        self.root.title("Agenda Personal")
        self.root.geometry("650x500")

        # --- Creación de Frames para organizar la GUI ---

        # Frame para los campos de entrada de datos
        self.frame_entrada = ttk.Frame(self.root, padding="10")
        self.frame_entrada.pack(pady=10, fill='x')

        # Frame para la lista (TreeView) de eventos
        self.frame_lista = ttk.Frame(self.root, padding="10")
        self.frame_lista.pack(pady=10, fill='both', expand=True)

        # Frame para los botones de acción
        self.frame_acciones = ttk.Frame(self.root, padding="10")
        self.frame_acciones.pack(pady=10, fill='x')

        # --- Inicializar los componentes en cada Frame ---
        self.crear_widgets_entrada()
        self.crear_widgets_lista()
        self.crear_widgets_acciones()

    def crear_widgets_entrada(self):

        # Crea los widgets para el frame de entrada (Labels, Entries, DatePicker).

        # Etiqueta y campo para la Fecha (usando DateEntry)
        ttk.Label(self.frame_entrada, text="Fecha:").grid(row=0, column=0, padx=5, pady=5, sticky='w')
        # Usamos DateEntry como DatePicker. 'date_pattern' define el formato.
        self.date_entry = DateEntry(self.frame_entrada, width=12, background='darkblue',
                                    foreground='white', borderwidth=2, date_pattern='dd/MM/yyyy')
        self.date_entry.grid(row=0, column=1, padx=5, pady=5)

        # Etiqueta y campo para la Hora
        ttk.Label(self.frame_entrada, text="Hora (HH:MM):").grid(row=0, column=2, padx=5, pady=5, sticky='w')
        self.time_entry = ttk.Entry(self.frame_entrada, width=10)
        self.time_entry.grid(row=0, column=3, padx=5, pady=5)

        # Etiqueta y campo para la Descripción
        ttk.Label(self.frame_entrada, text="Descripción:").grid(row=1, column=0, padx=5, pady=5, sticky='w')
        # Usamos 'columnspan=3' para que el campo de descripción ocupe más espacio
        self.desc_entry = ttk.Entry(self.frame_entrada, width=50)
        self.desc_entry.grid(row=1, column=1, columnspan=3, padx=5, pady=5, sticky='we')

        # Hacemos que la columna 1 (donde están los 'Entry') se expanda
        self.frame_entrada.grid_columnconfigure(1, weight=1)
        self.frame_entrada.grid_columnconfigure(3, weight=1)

    def crear_widgets_lista(self):

        # Crea el TreeView para mostrar la lista de eventos.

        # Definir las columnas
        columnas = ('fecha', 'hora', 'descripcion')

        self.tree = ttk.Treeview(self.frame_lista, columns=columnas, show='headings')

        # Configurar las cabeceras
        self.tree.heading('fecha', text='Fecha')
        self.tree.heading('hora', text='Hora')
        self.tree.heading('descripcion', text='Descripción')

        # Configurar el ancho de las columnas
        self.tree.column('fecha', width=100, anchor=tk.CENTER)
        self.tree.column('hora', width=80, anchor=tk.CENTER)
        self.tree.column('descripcion', width=400)

        # Añadir un Scrollbar (barra de desplazamiento)
        scrollbar = ttk.Scrollbar(self.frame_lista, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        # Empaquetar el TreeView y el Scrollbar
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    def crear_widgets_acciones(self):

        # Crea los botones de acción (Agregar, Eliminar, Salir).

        # Botón para Agregar Evento
        self.btn_agregar = ttk.Button(self.frame_acciones, text="Agregar Evento", command=self.agregar_evento)
        self.btn_agregar.pack(side=tk.LEFT, padx=10, pady=5)

        # Botón para Eliminar Evento
        self.btn_eliminar = ttk.Button(self.frame_acciones, text="Eliminar Evento Seleccionado",
                                       command=self.eliminar_evento)
        self.btn_eliminar.pack(side=tk.LEFT, padx=10, pady=5)

        # Botón para Salir
        self.btn_salir = ttk.Button(self.frame_acciones, text="Salir", command=self.root.quit)
        self.btn_salir.pack(side=tk.RIGHT, padx=10, pady=5)

    # --- Funciones de los Botones (Manejo de Eventos) ---

    def agregar_evento(self):

        # Obtiene los datos de los campos de entrada y los añade al TreeView.

        # Obtener los valores de los campos
        fecha = self.date_entry.get()
        hora = self.time_entry.get()
        descripcion = self.desc_entry.get()

        # Validación simple: asegurarse de que los campos no estén vacíos
        if not fecha or not hora or not descripcion:
            messagebox.showwarning("Campos vacíos", "Por favor, complete todos los campos.")
            return

        # Insertar los valores en el TreeView
        # '' indica que se inserta en el nivel raíz, tk.END al final de la lista
        self.tree.insert('', tk.END, values=(fecha, hora, descripcion))

        # Limpiar los campos de entrada después de agregar
        self.time_entry.delete(0, tk.END)
        self.desc_entry.delete(0, tk.END)
        # Opcionalmente, puedes resetear la hora a un valor predeterminado, ej: "08:00"
        # self.time_entry.insert(0, "08:00")

    def eliminar_evento(self):

        # Elimina el evento que está actualmente seleccionado en el TreeView.

        # Obtener el ítem seleccionado
        selected_item = self.tree.selection()

        if not selected_item:
            messagebox.showwarning("Nada seleccionado", "Por favor, seleccione un evento de la lista para eliminar.")
            return

        # Diálogo de confirmación (Opcional pero recomendado)
        confirmar = messagebox.askyesno("Confirmar eliminación",
                                        "¿Está seguro de que desea eliminar el evento seleccionado?")

        if confirmar:
            # Eliminar el ítem seleccionado
            for item in selected_item:
                self.tree.delete(item)


# --- Bloque principal para ejecutar la aplicación ---
if __name__ == "__main__":
    # Crear la ventana principal
    root = tk.Tk()

    # Crear una instancia de la aplicación
    app = AgendaApp(root)

    # Iniciar el bucle principal de la GUI
    root.mainloop()