import tkinter as tk
import os
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
from modelos.gestionUsuarios import GestorUsuarios

class IniciarSesion:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.frame = tk.Frame(self.root)  # Creamos un frame principal para todos los widgets
        self.frame.pack(fill="both", expand=True)
        self.gestor_usuarios = GestorUsuarios()
        self.setup_ui()

    def setup_ui(self):
        self.root.title("Inicio de Sesión")
        self.root.geometry("1920x1080")
        self.root.state('zoomed')

        # Fondo de bienvenida
        imagen_bienvenida = Image.open("imagenes/logo.png")
        imagen_bienvenida = ImageTk.PhotoImage(imagen_bienvenida)
        label_bienvenida = tk.Label(self.frame, image=imagen_bienvenida)
        label_bienvenida.image = imagen_bienvenida  # Mantener una referencia
        label_bienvenida.pack(pady=(20, 0))

        # Etiqueta y campo de entrada para el nombre de usuario
        label_usuario = ttk.Label(self.frame, text="Usuario:")
        label_usuario.pack(pady=(20, 5))
        self.entry_usuario = ttk.Entry(self.frame)
        self.entry_usuario.pack(pady=5)

        # Etiqueta y campo de entrada para la contraseña
        label_contrasena = ttk.Label(self.frame, text="Contraseña:")
        label_contrasena.pack(pady=(10, 5))
        self.entry_contrasena = ttk.Entry(self.frame, show="*")
        self.entry_contrasena.pack(pady=5)

        # Botón de inicio de sesión
        boton_ingresar = ttk.Button(self.frame, text="Ingresar", command=self.verificar_credenciales)
        boton_ingresar.pack(pady=10)

        # Vincular tecla Enter a boton_ingresar
        self.root.bind("<Return>", lambda event: self.verificar_credenciales())

        # Botón para registrar nuevo usuario
        boton_registrar = ttk.Button(self.frame, text="Registrar nuevo usuario", command=self.registrar_nuevo_usuario)
        boton_registrar.pack(pady=10)

    def verificar_credenciales(self):
        usuario = self.entry_usuario.get()
        contrasena = self.entry_contrasena.get()
        if self.gestor_usuarios.verificar_credenciales(usuario, contrasena):
            self.controller.current_user = usuario # Almacena el usuario actual en el controlador
            self.controller.show_desktop()
        else:
            messagebox.showinfo("Error", "Credenciales incorrectas")

    def registrar_nuevo_usuario(self):
        self.ventana_registro = tk.Toplevel(self.root)
        self.ventana_registro.title("Registro de Usuario")
        self.ventana_registro.geometry("300x200")

        tk.Label(self.ventana_registro, text="Usuario:").pack(pady=(10, 0))
        self.entry_nuevo_usuario = ttk.Entry(self.ventana_registro)
        self.entry_nuevo_usuario.pack()

        tk.Label(self.ventana_registro, text="Contraseña:").pack(pady=5)
        self.entry_nueva_contrasena = ttk.Entry(self.ventana_registro, show="*")
        self.entry_nueva_contrasena.pack()

        ttk.Button(self.ventana_registro, text="Confirmar registro", command=self.confirmar_registro).pack(pady=15)

    def confirmar_registro(self):
        usuario = self.entry_nuevo_usuario.get()
        contrasena = self.entry_nueva_contrasena.get()
        if usuario and contrasena:
            if self.gestor_usuarios.registrar_usuario(usuario, contrasena):
                messagebox.showinfo("Registro exitoso", "El usuario ha sido registrado exitosamente.")
                self.crear_estructura_directorios(usuario)  # Crea la estructura de directorios para el usuario
                self.ventana_registro.destroy()
            else:
                messagebox.showerror("Error", "El nombre de usuario ya está en uso. Por favor, elige otro.")
        else:
            messagebox.showerror("Error", "El nombre de usuario y la contraseña no pueden estar vacíos.")
    def crear_estructura_directorios(self, usuario):
        # Define la ruta base donde se crearán los directorios del usuario
        ruta_base = os.path.join(os.getcwd(), "perfiles", usuario) # Se crea una carpeta con el nombre del usuario en Perfiles

        print(ruta_base)

        # Define los nombres de los directorios a crear
        directorios = ["Documentos", "Escritorio", "Descargas", "Música", "Videos"]
        # Crea cada directorio
        for directorio in directorios:
            os.makedirs(os.path.join(ruta_base, directorio), exist_ok=True)