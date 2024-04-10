import tkinter as tk
from tkinter import ttk, filedialog, messagebox

class AdministradorArchivos:
    def __init__(self, tk):
        self.root = tk
        self.root.title("Administrador de Archivos")
        self.root.geometry("800x600")

        # Mejora: Estilo para los botones
        style = ttk.Style()
        style.configure('TButton', font=('Calibri', 12), borderwidth='4')
        style.map('TButton', foreground=[('active', '!disabled', 'green')], background=[('active', 'black')])

        # Utiliza un frame para organizar los widgets
        self.frame = ttk.Frame(self.root, padding="10 10 10 10")
        self.frame.pack(fill="both", expand=True)

        # Etiqueta como título de la sección
        self.label_administrador = ttk.Label(self.frame,
                                             text="Explorador de Archivos con Tkinter",
                                             font=('Calibri', 14, 'bold'))
        self.label_administrador.grid(column=0, row=0, columnspan=2, pady=10)

        # Botón para abrir archivos
        self.boton_abrir = ttk.Button(self.frame, text="Abrir Archivo", command=self.cargar_archivos)
        self.boton_abrir.grid(column=0, row=1, pady=10, padx=5)

        # Ajusta el grid para que los widgets se expandan adecuadamente
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.rowconfigure(0, weight=1)
        self.frame.rowconfigure(1, weight=1)

    def cargar_archivos(self):
        nombre_archivo = filedialog.askopenfilename(initialdir="/",
                                                    title="Seleccionar archivo",
                                                    filetypes=(("Todos los archivos", "*.*"), ("Archivos de texto", "*.txt*")))
        if nombre_archivo:  # Solo actualiza la etiqueta si se seleccionó un archivo
            self.label_administrador.configure(text="Archivo abierto: " + nombre_archivo)