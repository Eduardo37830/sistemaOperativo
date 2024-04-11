import tkinter as tk
from tkinter import ttk, filedialog, messagebox


class EditorTexto:
    def __init__(self, master):
        self.master = master
        self.master.title("Editor de Texto Simple")
        self.master.geometry("600x400")

        self.texto = tk.Text(self.master, undo=True)
        self.texto.pack(expand=True, fill='both')

        self.crear_menu()

    def crear_menu(self):
        self.menubar = tk.Menu(self.master)

        # Archivo
        menu_archivo = tk.Menu(self.menubar, tearoff=0)
        menu_archivo.add_command(label="Nuevo", command=self.nuevo_archivo)
        menu_archivo.add_command(label="Abrir", command=self.abrir_archivo)
        menu_archivo.add_command(label="Guardar", command=self.guardar_archivo)
        menu_archivo.add_separator()
        menu_archivo.add_command(label="Salir", command=self.master.quit)

        self.menubar.add_cascade(label="Archivo", menu=menu_archivo)

        # Editar
        menu_editar = tk.Menu(self.menubar, tearoff=0)
        menu_editar.add_command(label="Deshacer", command=self.texto.edit_undo)
        menu_editar.add_command(label="Rehacer", command=self.texto.edit_redo)
        menu_editar.add_separator()
        menu_editar.add_command(label="Cortar", command=lambda: self.master.focus_get().event_generate('<<Cut>>'))
        menu_editar.add_command(label="Copiar", command=lambda: self.master.focus_get().event_generate('<<Copy>>'))
        menu_editar.add_command(label="Pegar", command=lambda: self.master.focus_get().event_generate('<<Paste>>'))

        self.menubar.add_cascade(label="Editar", menu=menu_editar)

        self.master.config(menu=self.menubar)

    def nuevo_archivo(self):
        self.texto.delete(1.0, tk.END)

    def abrir_archivo(self):
        ruta_archivo = filedialog.askopenfilename(defaultextension=".txt",
                                                  filetypes=[("Todos los archivos", "*.*"),
                                                             ("Archivos de texto", "*.txt"),
                                                             ("Archivos de Python", "*.py")])
        if ruta_archivo:
            self.texto.delete(1.0, tk.END)
            with open(ruta_archivo, "r") as archivo:
                self.texto.insert(1.0, archivo.read())

    def guardar_archivo(self):
        ruta_archivo = filedialog.asksaveasfilename(defaultextension=".txt",
                                                    filetypes=[("Todos los archivos", "*.*"),
                                                               ("Archivos de texto", "*.txt"),
                                                               ("Archivos de Python", "*.py")])
        if ruta_archivo:
            with open(ruta_archivo, "w") as archivo:
                archivo.write(self.texto.get(1.0, tk.END))
