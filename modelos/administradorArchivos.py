import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

class AdministradorArchivos:
    def __init__(self, root, ruta_carpeta):
        self.root = root
        self.ruta_actual = ruta_carpeta
        self.root.title("Administrador de Archivos")
        self.root.geometry("800x600")

        # Estilo para los botones
        style = ttk.Style()
        style.configure('TButton', font=('Calibri', 12), borderwidth='4')
        style.map('TButton', foreground=[('active', '!disabled', 'green')], background=[('active', 'black')])

        # Frame para organizar los widgets
        self.frame = ttk.Frame(self.root, padding="10 10 10 10")
        self.frame.pack(fill="both", expand=True)

        # Etiqueta como título de la sección
        self.label_administrador = ttk.Label(self.frame, text="Explorador de Archivos con Tkinter",
                                             font=('Calibri', 14, 'bold'))
        self.label_administrador.grid(column=0, row=0, columnspan=2, pady=10)

        # Listbox para mostrar los archivos
        self.listbox_archivos = tk.Listbox(self.frame, height=15, width=50)
        self.listbox_archivos.grid(column=1, row=1, pady=10, padx=5, sticky='nsew')

        # Botón para regresar al directorio anterior
        self.boton_regresar = ttk.Button(self.frame, text="Regresar", command=self.regresar)
        self.boton_regresar.grid(column=0, row=1, sticky='nw', pady=10)

        # Botón para abrir el archivo o directorio seleccionado
        self.boton_seguir = ttk.Button(self.frame, text="Abrir", command=self.seguir)
        self.boton_seguir.grid(column=0, row=1, sticky='sw', pady=10)

        # Evento para abrir el archivo o directorio seleccionado
        self.listbox_archivos.bind("<Double-Button-1>", self.abrir_elemento)



        # Ajustes de grid para expansión adecuada
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=3)
        self.frame.rowconfigure(1, weight=1)

        # Cargar archivos de la carpeta inicial
        self.cargar_archivos(ruta_carpeta)

    def cargar_archivos(self, ruta_carpeta):
        # Actualizar la etiqueta con la ruta actual
        self.label_administrador.configure(text="Carpeta abierta: " + ruta_carpeta)
        self.listbox_archivos.delete(0, tk.END)
        # Listar todos los archivos y directorios en la carpeta
        for entry in os.listdir(ruta_carpeta):
            self.listbox_archivos.insert(tk.END, entry)

    def regresar(self):
        if os.path.dirname(self.ruta_actual) != self.ruta_actual:
            self.ruta_actual = os.path.dirname(self.ruta_actual)
            self.cargar_archivos(self.ruta_actual)

    def seguir(self):
        seleccion = self.listbox_archivos.get(self.listbox_archivos.curselection())
        ruta_siguiente = os.path.join(self.ruta_actual, seleccion)
        if os.path.isdir(ruta_siguiente):
            self.ruta_actual = ruta_siguiente
            self.cargar_archivos(ruta_siguiente)
        elif os.path.isfile(ruta_siguiente):
            os.startfile(ruta_siguiente)

    def abrir_elemento(self, event):
        seleccion = self.listbox_archivos.get(self.listbox_archivos.curselection())
        ruta_siguiente = os.path.join(self.ruta_actual, seleccion)
        if os.path.isdir(ruta_siguiente):
            self.ruta_actual = ruta_siguiente
            self.cargar_archivos(ruta_siguiente)
        elif os.path.isfile(ruta_siguiente):
            os.startfile(ruta_siguiente)  # Abrir el archivo con la aplicación predeterminada
