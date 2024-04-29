import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
from modelos.desktop import Escritorio
from modelos.gestionUsuarios import GestorUsuarios
class IniciarSesion:
    def __init__(self, root):
        self.root = root
        self.gestor_usuarios = GestorUsuarios()
        self.root.title("Inicio de Sesión")
        self.root.geometry("1920x1080")
        self.root.state('zoomed')

        # Fondo de bienvenida
        self.imagen_bienvenida = Image.open("imagenes/logo.png")
        self.imagen_bienvenida = ImageTk.PhotoImage(self.imagen_bienvenida)
        self.label_bienvenida = tk.Label(self.root, image=self.imagen_bienvenida)
        self.label_bienvenida.pack(pady=(20, 0))

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

        # Vincular tecla Enter a boton_ingresar
        self.root.bind("<Return>", lambda event: self.verificar_credenciales())

        # Botón para registrar nuevo usuario
        self.boton_registrar = ttk.Button(self.root, text="Registrar nuevo usuario", command=self.registrar_nuevo_usuario)
        self.boton_registrar.pack(pady=10)

    def verificar_credenciales(self):
        usuario = self.entry_usuario.get()
        contrasena = self.entry_contrasena.get()
        if self.gestor_usuarios.verificar_credenciales(usuario, contrasena):
            print("Inicio de sesión exitoso")
            self.root.destroy()
            self.mostrar_escritorio()
        else:
            tk.messagebox.showinfo("Error", "Credenciales incorrectas")

    def registrar_nuevo_usuario(self):
        # Crear una nueva ventana Toplevel
        self.ventana_registro = tk.Toplevel(self.root)
        self.ventana_registro.title("Registro de Usuario")
        self.ventana_registro.geometry("300x200")

        # Etiquetas y campos de entrada para usuario y contraseña
        tk.Label(self.ventana_registro, text="Usuario:").pack(pady=(10, 0))
        self.entry_nuevo_usuario = ttk.Entry(self.ventana_registro)
        self.entry_nuevo_usuario.pack()

        tk.Label(self.ventana_registro, text="Contraseña:").pack(pady=5)
        self.entry_nueva_contrasena = ttk.Entry(self.ventana_registro, show="*")
        self.entry_nueva_contrasena.pack()

        # Botón para confirmar el registro
        ttk.Button(self.ventana_registro, text="Confirmar registro", command=self.confirmar_registro).pack(pady=15)

    def confirmar_registro(self):
        usuario = self.entry_nuevo_usuario.get()
        contrasena = self.entry_nueva_contrasena.get()
        print(usuario, contrasena)
        if usuario and contrasena:
            if self.gestor_usuarios.registrar_usuario(usuario, contrasena):
                tk.messagebox.showinfo("Registro exitoso", "El usuario ha sido registrado exitosamente.")
                self.ventana_registro.destroy()
            else:
                tk.messagebox.showerror("Error", "El nombre de usuario ya está en uso. Por favor, elige otro.")
        else:
            tk.messagebox.showerror("Error", "El nombre de usuario y la contraseña no pueden estar vacíos.")

    def mostrar_escritorio(self):
        root = tk.Tk()
        root.config(bg="#EDEDED")
        Escritorio(root)
        root.mainloop()