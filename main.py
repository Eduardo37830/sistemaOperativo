#Sistemas Operativos, escritorio con tkinter
#Autor: Eduardo Villamil


import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk

class IniciarSesion:
    def __init__(self, root):
        self.root = root
        self.root.title("Inicio de Sesión")
        self.root.geometry("300x200")

        # Etiqueta y campo de entrada para el nombre de usuario
        self.label_usuario = ttk.Label(self.root, text="Usuario:")
        self.label_usuario.pack(pady=(20, 5))
        self.entry_usuario = ttk.Entry(self.root)
        self.entry_usuario.pack(pady=5)

        # Etiqueta y campo de entrada para la contraseña
        self.label_contrasena = ttk.Label(self.root, text="Contraseña:")
        self.label_contrasena.pack(pady=(10, 5))
        self.entry_contrasena = ttk.Entry(self.root, show="*")
        self.entry_contrasena.pack(pady=5)

        # Botón de inicio de sesión
        self.boton_ingresar = ttk.Button(self.root, text="Ingresar", command=self.verificar_credenciales)
        self.boton_ingresar.pack(pady=10)

    def verificar_credenciales(self):
        # Lógica para verificar las credenciales
        usuario = self.entry_usuario.get()
        contrasena = self.entry_contrasena.get()

        # Ejemplo básico de verificación de credenciales
        if usuario == "admin" and contrasena == "admin":
            print("Inicio de sesión exitoso")
            self.root.destroy()  # Cerrar la ventana de inicio de sesión
            self.mostrar_escritorio()  # Mostrar el escritorio después del inicio de sesión exitoso
        else:
            print("Credenciales incorrectas")

    def mostrar_escritorio(self):
        root = tk.Tk()
        root.config(bg="#EDEDED")
        Escritorio(root)
        root.mainloop()

class Escritorio:
    def __init__(self, root):
        self.root = root
        self.root.title("Escritorio")
        self.root.geometry("1280x720")

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
        self.barra_tareas.pack(side="bottom", fill="x", padx=10, pady=(1000)) #padding

        # Botón de inicio con el ícono redimensionado
        self.icono_inicio = self.resize_image("imagenes/logo.png")
        self.boton_inicio = ttk.Button(self.barra_tareas, image=self.icono_inicio, command=self.volver_inicio, style="Boton.TButton")
        self.boton_inicio.pack(pady=5, padx=10, side="left")

        # Botón para seleccionar fondo de pantalla
        self.icono_fondo = self.resize_image("imagenes/icono_wall.png")
        self.boton_fondo = ttk.Button(self.barra_tareas, image=self.icono_fondo, command=self.seleccionar_fondo, style="Boton.TButton")
        self.boton_fondo.pack(pady=5, padx=10, side="left")

        # Botón para salir
        self.icono_salir = self.resize_image("imagenes/icono_salir.png")
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

    def resize_image(self, ruta):
        return ImageTk.PhotoImage(Image.open(ruta).resize((30, 30)))

if __name__ == "__main__":
    root = tk.Tk()
    login = IniciarSesion(root)
    root.mainloop()