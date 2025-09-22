# Aplicación de Lista de Tareas (OOP) usando Tkinter

import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkfont
from typing import List

# Definición de la clase Tarea
class Tarea:
    def __init__(self, description: str, completed: bool = False):
        # Atributos de la tarea
        self.description = description
        self.completed = completed

    def __repr__(self):
        # Representación en texto, útil al imprimir listas de tareas
        return f"Tarea(description={self.description!r}, completed={self.completed})"

    def __eq__(self, other):
        # Permite comparar dos tareas por sus atributos
        if isinstance(other, Tarea):
            return self.description == other.description and self.completed == other.completed
        return False


# Clase principal de la aplicación
class TodoApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Lista de Tareas - OOP (Tkinter)")
        self.root.geometry("520x420")
        self.root.minsize(400, 300)

        # Lista interna de tareas
        self.tasks: List[Tarea] = []

        # Fuentes: normal y tachada
        self.default_font = tkfont.nametofont("TkDefaultFont")
        self.strike_font = self.default_font.copy()
        self.strike_font.configure(overstrike=1)

        # --- Interfaz ---
        top_frame = tk.Frame(self.root)
        top_frame.pack(padx=10, pady=(10, 6), fill="x")

        # Campo de entrada
        self.entry = tk.Entry(top_frame, font=self.default_font)
        self.entry.pack(side="left", fill="x", expand=True)
        self.entry.bind("<Return>", self.on_enter)

        add_btn = tk.Button(top_frame, text="Añadir Tarea", command=self.add_task)
        add_btn.pack(side="left", padx=(6, 0))

        # Listbox con scrollbar
        middle_frame = tk.Frame(self.root)
        middle_frame.pack(padx=10, pady=6, fill="both", expand=True)

        self.listbox = tk.Listbox(
            middle_frame,
            selectmode=tk.EXTENDED,
            activestyle="none",
            font=self.default_font
        )
        self.listbox.pack(side="left", fill="both", expand=True)

        scrollbar = tk.Scrollbar(middle_frame, orient="vertical", command=self.listbox.yview)
        scrollbar.pack(side="right", fill="y")
        self.listbox.config(yscrollcommand=scrollbar.set)

        # Eventos de la lista
        self.listbox.bind("<Double-Button-1>", self.on_double_click)

        # Botones de acción
        bottom_frame = tk.Frame(self.root)
        bottom_frame.pack(padx=10, pady=(6, 10), fill="x")

        complete_btn = tk.Button(bottom_frame, text="Marcar como Completada", command=self.mark_completed)
        complete_btn.pack(side="left")

        delete_btn = tk.Button(bottom_frame, text="Eliminar Tarea", command=self.delete_task)
        delete_btn.pack(side="left", padx=(6, 0))

        # Etiqueta de estado
        self.status = tk.Label(self.root, text="0 tareas", anchor="w")
        self.status.pack(side="bottom", fill="x", padx=10, pady=(0,6))

        # Binds globales
        self.root.bind("<Delete>", self.delete_task_event)
        self.root.bind("<Control-Return>", lambda e: self.add_task())

        self.update_task_list()

    # --- Manejadores de eventos ---
    def on_enter(self, event):
        self.add_task()

    def add_task(self):
        text = self.entry.get().strip()
        if not text:
            return
        self.tasks.append(Tarea(description=text))
        self.entry.delete(0, tk.END)
        self.update_task_list()

    def mark_completed(self):
        selected = self.listbox.curselection()
        if not selected:
            messagebox.showinfo("Atención", "Selecciona al menos una tarea para marcar como completada.")
            return
        for idx in selected:
            if 0 <= idx < len(self.tasks):
                self.tasks[idx].completed = True
        self.update_task_list()

    def delete_task(self):
        selected = list(self.listbox.curselection())
        if not selected:
            messagebox.showinfo("Atención", "Selecciona al menos una tarea para eliminar.")
            return
        for idx in reversed(selected):
            if 0 <= idx < len(self.tasks):
                del self.tasks[idx]
        self.update_task_list()

    def delete_task_event(self, event):
        self.delete_task()

    def on_double_click(self, event):
        index = self.listbox.nearest(event.y)
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = not self.tasks[index].completed
            self.update_task_list()

    def update_task_list(self):
        self.listbox.delete(0, tk.END)
        for i, tarea in enumerate(self.tasks):
            prefix = "[✔] " if tarea.completed else "[ ] "
            display_text = prefix + tarea.description
            self.listbox.insert(tk.END, display_text)
            try:
                if tarea.completed:
                    self.listbox.itemconfig(i, fg="gray", font=self.strike_font)
                else:
                    self.listbox.itemconfig(i, fg="black", font=self.default_font)
            except Exception:
                pass
        total = len(self.tasks)
        completed = sum(1 for t in self.tasks if t.completed)
        self.status.config(text=f"{total} tarea(s) — {completed} completada(s)")


# Punto de entrada
if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
