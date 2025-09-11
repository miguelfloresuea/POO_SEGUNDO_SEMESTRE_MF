# 1. Importar la librería Tkinter para la interfaz gráfica.
import tkinter as tk
from tkinter import ttk

# Esta función se ejecuta cuando el usuario presiona el botón "Agregar".
def agregar_dato():
    # Se obtiene el texto del campo de entrada.
    dato = campo_texto.get()

    # Se comprueba que el texto no esté vacío.
    if dato:
        # Se inserta el dato en el control de la lista (Listbox).
        lista_datos.insert(tk.END, dato)
        # Se borra el contenido del campo de texto para una nueva entrada.
        campo_texto.delete(0, tk.END)


# Esta función elimina el elemento seleccionado.

def eliminar_dato_seleccionado():
    # Primero, se obtienen los índices de los elementos seleccionados.
    # 'curselection()' devuelve una tupla, por ej. (0,) si se selecciona el primer ítem.
    indices_seleccionados = lista_datos.curselection()

    # Se comprueba si realmente hay un elemento seleccionado.
    if indices_seleccionados:
        # Se elimina el elemento de la lista usando su índice.
        # Como solo permitimos selección simple, tomamos el primer índice.
        lista_datos.delete(indices_seleccionados[0])

#  Configuración de la Ventana Principal

# 2. Se crea la ventana principal de la aplicación.
ventana = tk.Tk()
# Se establece el título descriptivo para la ventana.
ventana.title("Tarea POO: Interfaz Gráfica")
ventana.geometry("300x400") # Se define un tamaño inicial.

# --- Creación de los Componentes (Widgets) de la GUI ---

# 3. Se crea un Frame para organizar mejor los componentes.
frame = ttk.Frame(ventana, padding="10")
frame.pack(fill=tk.BOTH, expand=True)

# Creación de la Etiqueta (Label) que indica qué hacer.
etiqueta = ttk.Label(frame, text="Introduce un dato:")
etiqueta.pack(pady=5)

# Creación del Campo de Texto (Entry) para la entrada del usuario.
campo_texto = ttk.Entry(frame, width=30)
campo_texto.pack(pady=5)

# Creación del Botón "Agregar".
boton_agregar = ttk.Button(frame, text="Agregar", command=agregar_dato)
boton_agregar.pack(pady=5)

# ###################################################################################
# CAMBIO REALIZADO: El botón ahora se llama "Eliminar Selección" y usa la nueva función.
# ###################################################################################
boton_eliminar = ttk.Button(frame, text="Eliminar Selección", command=eliminar_dato_seleccionado)
boton_eliminar.pack(pady=5)

# Creación de la Lista (Listbox) para mostrar los datos agregados.
lista_datos = tk.Listbox(frame, height=10)
lista_datos.pack(pady=10, fill=tk.BOTH, expand=True)

# --- Iniciar la Aplicación ---

# 4. Se inicia el bucle principal de la aplicación.
ventana.mainloop()