#Sistemas Operativos, escritorio con tkinter
#Autor: Eduardo Villamil


import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk


class Escritorio:
    def __init__(self, root):
        self.root = root
        self.root.title("Escritorio")
        self.root.geometry("800x600")

        # Estilos
        self.estilo = ttk.Style()
        self.estilo.configure("Titulo.TLabel", font=("Segoe UI", 24), foreground="#FFFFFF")
        self.estilo.configure("Boton.TButton", font=("Segoe UI", 10))

        # Barra de tareas
        self.barra_tareas = tk.Frame(self.root, bg="#0078D7", height=40)
        self.barra_tareas.pack(side="top", fill="x")

        # Botón para seleccionar fondo de pantalla
        self.boton_fondo = ttk.Button(self.barra_tareas, text="Seleccionar Fondo", command=self.seleccionar_fondo,
                                      style="Boton.TButton")
        self.boton_fondo.pack(pady=5, padx=10, side="left")

        self.titulo = ttk.Label(self.barra_tareas, text="Escritorio", style="Titulo.TLabel", background="#0078D7")
        self.titulo.pack(pady=5, padx=10, side="left")

        # Área de trabajo
        self.area_trabajo = tk.Frame(self.root)
        self.area_trabajo.pack(expand=True, fill="both")

        # Configurar el fondo de pantalla inicial
        self.fondo = Image.open("imagenes/Fondoprueba.png")
        self.fondo = ImageTk.PhotoImage(self.fondo)
        self.label_fondo = tk.Label(self.area_trabajo, image=self.fondo)
        self.label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

        self.boton_salir = ttk.Button(self.area_trabajo, text="Salir", command=root.quit, style="Boton.TButton")
        self.boton_salir.pack(pady=10, padx=20, side="right")

    def seleccionar_fondo(self):
        filename = filedialog.askopenfilename(filetypes=[("Archivos de imagen", "*.png;*.jpg;*.jpeg")])
        if filename:
            self.fondo = Image.open(filename)
            self.fondo = ImageTk.PhotoImage(self.fondo)
            self.label_fondo.configure(image=self.fondo)


if __name__ == "__main__":
    root = tk.Tk()
    root.config(bg="#EDEDED")
    escritorio = Escritorio(root)
    root.mainloop()
