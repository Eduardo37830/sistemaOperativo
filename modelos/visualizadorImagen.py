import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
import os

class VisualizadorImagenes:
    def __init__(self, master):
        self.master = master
        self.master.title("Visualizador de Imágenes")
        self.master.geometry("1280x720")
        self.master.state('zoomed')

        self.lista_imagenes = []
        self.indice_actual = 0

        self.crear_interfaz()

    def crear_interfaz(self):
        self.panel_imagen = tk.Label(self.master)
        self.panel_imagen.pack(expand=True, fill="both")
        self.panel_imagen.pack_propagate(False)  # Evitar que el panel de imagen cambie de tamaño

        boton_cargar = ttk.Button(self.master, text="Cargar Directorio", command=self.cargar_directorio)
        boton_cargar.pack(side="bottom", fill="x")

        self.boton_anterior = ttk.Button(self.master, text="<< Anterior", command=self.imagen_anterior)
        self.boton_anterior.pack(side="left", fill="y")

        self.boton_siguiente = ttk.Button(self.master, text="Siguiente >>", command=self.imagen_siguiente)
        self.boton_siguiente.pack(side="right", fill="y")

        self.actualizar_botones_estado()

    def cargar_directorio(self):
        directorio = filedialog.askdirectory()
        if directorio:
            self.lista_imagenes = [os.path.join(directorio, f) for f in os.listdir(directorio) if f.endswith(('.png', '.jpg', '.jpeg'))]
            if self.lista_imagenes:
                self.indice_actual = 0
                self.mostrar_imagen(self.indice_actual)
            self.actualizar_botones_estado()

    def mostrar_imagen(self, indice):
        imagen = Image.open(self.lista_imagenes[indice])
        self.master.update_idletasks()  # Actualiza la ventana para obtener las dimensiones correctas del panel
        max_width = self.panel_imagen.winfo_width()
        max_height = self.panel_imagen.winfo_height()
        # Redimensionar la imagen para que se ajuste al panel
        imagen = self.redimensionar_imagen(imagen, max_width, max_height)
        foto = ImageTk.PhotoImage(imagen)
        self.panel_imagen.configure(image=foto)
        self.panel_imagen.image = foto  # Guardar referencia de la imagen

    def redimensionar_imagen(self, imagen, max_width, max_height):
        ratio = min(max_width / imagen.width, max_height / imagen.height)
        new_size = (int(imagen.width * ratio), int(imagen.height * ratio))
        return imagen.resize(new_size, Image.LANCZOS)

    def imagen_siguiente(self):
        if self.lista_imagenes:
            self.indice_actual = (self.indice_actual + 1) % len(self.lista_imagenes)
            self.mostrar_imagen(self.indice_actual)
            self.actualizar_botones_estado()

    def imagen_anterior(self):
        if self.lista_imagenes:
            self.indice_actual = (self.indice_actual - 1 + len(self.lista_imagenes)) % len(self.lista_imagenes)
            self.mostrar_imagen(self.indice_actual)
            self.actualizar_botones_estado()

    def actualizar_botones_estado(self):
        estado_anterior = "normal" if self.lista_imagenes and self.indice_actual > 0 else "disabled"
        estado_siguiente = "normal" if self.lista_imagenes and self.indice_actual < len(self.lista_imagenes) - 1 else "disabled"

        self.boton_anterior["state"] = estado_anterior
        self.boton_siguiente["state"] = estado_siguiente


if __name__ == "__main__":
    root = tk.Tk()
    app = VisualizadorImagenes(root)
    root.mainloop()
