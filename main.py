#Sistemas Operativos, escritorio con tkinter
#Autor: Eduardo Villamil


import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk


import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk

class Escritorio:
    def __init__(self, root):
        self.root = root
        self.root.title("Escritorio")
        self.root.geometry("1280x800")

        # Estilos
        self.estilo = ttk.Style()
        self.estilo.configure("Titulo.TLabel", font=("Segoe UI", 24), foreground="#FFFFFF")
        self.estilo.configure("Boton.TButton", font=("Segoe UI", 10))

        # Área de trabajo
        self.area_trabajo = tk.Frame(self.root)
        self.area_trabajo.pack(expand=True, fill="both")

        # Configurar el fondo de pantalla inicial
        self.fondo = Image.open("imagenes/Fondoprueba.png")
        self.fondo = ImageTk.PhotoImage(self.fondo)
        self.label_fondo = tk.Label(self.area_trabajo, image=self.fondo)
        self.label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

        # Barra de tareas
        self.barra_tareas = tk.Frame(self.root, bg="#0078D7", height=40)
        self.barra_tareas.pack(side="bottom", fill="x")

        #Boton de inicio
        self.icono_inicio = ImageTk.PhotoImage(Image.open("imagenes/logo.png").resize((30, 30)))
        self.boton_inicio = ttk.Button(self.barra_tareas, image=self.icono_inicio, command=self.volver_inicio, style="Boton.TButton")
        self.boton_inicio.pack(pady=5, padx=10, side="left")

        #Boton para seleccionar fondo de pantalla
        self.icono_fondo = ImageTk.PhotoImage(Image.open("imagenes/icono_wall.png").resize((30, 30)))
        self.boton_fondo = ttk.Button(self.barra_tareas, image=self.icono_fondo, command=self.seleccionar_fondo, style="Boton.TButton")
        self.boton_fondo.pack(pady=5, padx=10, side="left")

        #Boton para salir
        self.icono_salir = ImageTk.PhotoImage(Image.open("imagenes/icono_salir.png").resize((30, 30)))
        self.boton_salir = ttk.Button(self.barra_tareas, text="Salir", image=self.icono_salir, command=root.quit, style="Boton.TButton")
        self.boton_salir.pack(pady=5, padx=10, side="right")



        # Centrar la barra de tareas horizontalmente
        self.barra_tareas.place(relx=0.5, rely=1, anchor="s")


    def seleccionar_fondo(self):
        filename = filedialog.askopenfilename(filetypes=[("Archivos de imagen", "*.png;*.jpg;*.jpeg")])
        if filename:
            self.fondo = Image.open(filename)
            self.fondo = ImageTk.PhotoImage(self.fondo)
            self.label_fondo.configure(image=self.fondo)


    #Ir a la pantalla de inicio
    def volver_inicio(self):
        # Aquí va la lógica para volver a la pantalla de inicio
        print("Ir a la pantalla de inicio")



if __name__ == "__main__":
    root = tk.Tk()
    root.config(bg="#EDEDED")
    escritorio = Escritorio(root)
    root.mainloop()
