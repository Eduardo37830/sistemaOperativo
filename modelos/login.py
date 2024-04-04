import tkinter as tk
from tkinter import ttk
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class IniciarSesion:
    def __init__(self, root):
        self.root = root
        self.root.title("Inicio de Sesión")
        self.root.geometry("400x300")

        # Fondo de bienvenida
        self.imagen_bienvenida = Image.open("../imagenes/logo.png")
        self.imagen_bienvenida = ImageTk.PhotoImage(self.imagen_bienvenida)
        self.label_bienvenida = tk.Label(self.root, image=self.imagen_bienvenida)
        self.label_bienvenida.pack(pady=(20, 0))

        # Etiqueta y campo de entrada para el nombre de usuario
        self.label_usuario = ttk.Label(self.root, text="Usuario:", font=("Helvetica", 12))
        self.label_usuario.pack(pady=(10, 5))
        self.entry_usuario = ttk.Entry(self.root, font=("Helvetica", 12))
        self.entry_usuario.pack(pady=5)

        # Etiqueta y campo de entrada para la contraseña
        self.label_contrasena = ttk.Label(self.root, text="Contraseña:", font=("Helvetica", 12))
        self.label_contrasena.pack(pady=(10, 5))
        self.entry_contrasena = ttk.Entry(self.root, show="*", font=("Helvetica", 12))
        self.entry_contrasena.pack(pady=5)

        # Botón de inicio de sesión
        self.boton_ingresar = ttk.Button(self.root, text="Ingresar", command=self.verificar_credenciales, style="Boton.TButton")
        self.boton_ingresar.pack(pady=10)

        # Estilo para el botón
        self.estilo = ttk.Style()
        self.estilo.configure("Boton.TButton", font=("Helvetica", 12))

    def verificar_credenciales(self):
        # Lógica para verificar las credenciales
        usuario = self.entry_usuario.get()
        contrasena = self.entry_contrasena.get()

        # Ejemplo básico de verificación de credenciales
        if usuario == "admin" and contrasena == "admin":
            print("Inicio de sesión exitoso")
            self.root.destroy()  # Cerrar la ventana de inicio de sesión
            # Aquí se abre la ventana del escritorio después del inicio de sesión exitoso
        else:
            print("Credenciales incorrectas")

if __name__ == "__main__":
    root = tk.Tk()
    login = IniciarSesion(root)
    root.mainloop()
