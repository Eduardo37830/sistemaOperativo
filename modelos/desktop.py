import time
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
import datetime
import psutil
import threading

from modelos.calculadora import CalculadoraCientifica
from modelos.administradorArchivos import AdministradorArchivos
from modelos.visualizadorImagen import VisualizadorImagenes
from modelos.visualizadorVideo import VisualizadorVideos
from modelos.reproductorAudio import ReproductorAudio
from modelos.editorTexto import EditorTexto


class Escritorio:
    def __init__(self, root):
        self.root = root
        self.root.title("Escritorio")
        self.root.geometry("1920x1080")
        self.root.state('zoomed')

        # Estilos
        self.estilo = ttk.Style()
        self.estilo.configure("Titulo.TLabel", font=("Segoe UI", 24), foreground="#FFFFFF")
        self.estilo.configure("Boton.TButton", font=("Segoe UI", 10))

        # Área de trabajo
        self.area_trabajo = tk.Frame(self.root)
        self.area_trabajo.pack(expand=True, fill="both")

        # Configurar el fondo de pantalla inicial
        self.fondo = Image.open("imagenes/fondoRedimensionado.jpg")
        self.fondo = ImageTk.PhotoImage(self.fondo)
        self.label_fondo = tk.Label(self.area_trabajo, image=self.fondo)
        self.label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

        # Barra de tareas
        self.barra_tareas = tk.Frame(self.root, bg="#0078D7", height=40)
        self.barra_tareas.pack(side="bottom", fill="x", padx=10, pady=(0, 10))

        # Centrar la barra de tareas horizontalmente
        self.barra_tareas.place(relx=0.5, rely=1, anchor="s")

        # Botón de inicio con el logo redimensionado
        self.icono_inicio = self.resize_image("imagenes/logo.png")
        self.boton_inicio = ttk.Button(self.barra_tareas, image=self.icono_inicio, command=self.volver_inicio, style="Boton.TButton")
        self.boton_inicio.pack(pady=5, padx=10, side="left")

        # Botón para seleccionar fondo de pantalla
        self.icono_fondo = self.resize_image("imagenes/icono_añadir-imagen.png")
        self.boton_fondo = ttk.Button(self.barra_tareas, image=self.icono_fondo, command=self.seleccionar_fondo, style="Boton.TButton")
        self.boton_fondo.pack(pady=5, padx=10, side="left")

        # Botón para administrar archivos
        self.icono_carpeta = self.resize_image("imagenes/icono_carpeta.png")
        self.boton_carpeta = ttk.Button(self.barra_tareas, image=self.icono_carpeta, command=self.abrir_administrador_archivos, style="Boton.TButton")
        self.boton_carpeta.pack(pady=5, padx=10, side="left")

        # Botón para visualizar imágenes
        self.icono_imagen = self.resize_image("imagenes/icono_imagen.png")
        self.boton_imagen = ttk.Button(self.barra_tareas, image=self.icono_imagen, command=self.abrir_imagen, style="Boton.TButton")
        self.boton_imagen.pack(pady=5, padx=10, side="left")

        # Botón para visualizar videos
        self.icono_video = self.resize_image("imagenes/icono_video.png")
        self.boton_video = ttk.Button(self.barra_tareas, image=self.icono_video, command=self.abrir_video, style="Boton.TButton")
        self.boton_video.pack(pady=5, padx=10, side="left")

        # Botón para reproducir audio
        self.icono_audio = self.resize_image("imagenes/icono_musica.png")
        self.boton_audio = ttk.Button(self.barra_tareas, image=self.icono_audio, command=self.abrir_audio, style="Boton.TButton")
        self.boton_audio.pack(pady=5, padx=10, side="left")

        # Botón para editar texto
        self.icono_texto = self.resize_image("imagenes/icono_texto.png")
        self.boton_texto = ttk.Button(self.barra_tareas, image=self.icono_texto, command=self.abrir_texto, style="Boton.TButton")
        self.boton_texto.pack(pady=5, padx=10, side="left")

        # Botón para salir
        self.icono_salir = self.resize_image("imagenes/icono_salir.png")
        self.boton_salir = ttk.Button(self.barra_tareas, text="Salir", image=self.icono_salir, command=root.quit, style="Boton.TButton")
        self.boton_salir.pack(pady=5, padx=10, side="right")
        self.root.bind("<Escape>", lambda event: self.root.quit())

        # Fecha y hora
        self.label_hora = tk.Label(self.barra_tareas, text="", fg="black", bg="white", pady=10)
        self.label_hora.pack(side="right", padx=10)
        # Iniciar actualización de la hora en un hilo separado con threading
        self.hilo_hora = threading.Thread(target=self.actualizar_hora)
        self.hilo_hora.daemon = True  # El hilo daemon se cierra automáticamente cuando se cierra la aplicación
        self.hilo_hora.start()

        # Calculadora científica
        self.icono_calculadora = self.resize_image("imagenes/icono_calculadora.png")
        self.boton_calculadora = ttk.Button(self.barra_tareas, text="Calcular", image=self.icono_calculadora,
                                            command=self.abrir_calculadora, style="Boton.TButton")
        self.boton_calculadora.pack(pady=5, padx=10, side="right")
        # Información del sistema
        self.icono_info_sistema = self.resize_image("imagenes/interrogatorio.png")
        self.boton_info_sistema = ttk.Button(self.barra_tareas, image=self.icono_info_sistema, command=self.mostrar_info_sistema, style="Boton.TButton")
        self.boton_info_sistema.pack(pady=5, padx=10, side="left")



    def seleccionar_fondo(self):
        filename = filedialog.askopenfilename(filetypes=[("Archivos de imagen", "*.png;*.jpg;*.jpeg")])
        if filename:
            self.fondo = Image.open(filename)
            self.fondo = ImageTk.PhotoImage(self.fondo)
            self.label_fondo.configure(image=self.fondo)


    #Ir a la pantalla de inicio
    def volver_inicio(self):
        self.root.destroy()
        root = tk.Tk()
        from modelos.login import IniciarSesion  # Importar aquí para evitar la importación circular
        IniciarSesion(root)
        root.mainloop()
    #Cambiar el mataño de un ícono
    def resize_image(self, ruta):
        return ImageTk.PhotoImage(Image.open(ruta).resize((30, 30)))

    #Cambiar la hora
    def actualizar_hora(self):
        while True:
            ahora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.label_hora.config(text=ahora)
            self.label_hora.update_idletasks()  # Se asegura de que los cambios se muestren en la interfaz
            time.sleep(1)  # Pausa de 1 segundo entre actualizaciones


    #Abrir calculadora científica
    def abrir_calculadora(self):
        # Crea una nueva ventana Toplevel para la calculadora científica
        ventana_calculadora = tk.Toplevel(self.root)
        # Instancia la calculadora científica pasando la nueva ventana como master
        calculadora = CalculadoraCientifica(ventana_calculadora)

    def abrir_administrador_archivos(self):
        # Crea una nueva ventana Toplevel para el administrador de archivos
        ventana_administrador = tk.Toplevel(self.root)
        # Instancia el administrador de archivos pasando la nueva ventana como master
        administrador = AdministradorArchivos(ventana_administrador)

    def abrir_imagen(self):
        # Crea una nueva ventana Toplevel para el visualizador de imágenes
        ventana_imagen = tk.Toplevel(self.root)
        # Instancia el visualizador de imagen pasando la nueva ventana como master
        VisualizadorImagenes(ventana_imagen)

    def abrir_video(self):
        # Crea una nueva ventana Toplevel para el visualizador de videos
        ventana_video = tk.Toplevel(self.root)
        # Instancia el visualizador de video pasando la nueva ventana como master
        VisualizadorVideos(ventana_video)

    def abrir_audio(self):
        # Crea una nueva ventana Toplevel para el visualizador de videos
        ventana_audio = tk.Toplevel(self.root)
        # Instancia el reproductor de audio pasando la nueva ventana como master
        ReproductorAudio(ventana_audio)

    def abrir_texto(self):
        # Crea una nueva ventana Toplevel para el editor de textos
        ventana_texto = tk.Toplevel(self.root)
        # Instancia el visualizador de video pasando la nueva ventana como master
        EditorTexto(ventana_texto)

    def mostrar_info_sistema(self):
        # Crear una nueva ventana de nivel superior
        self.ventana_info_sistema = tk.Toplevel(self.root)
        self.ventana_info_sistema.title("Información del Sistema")

        # Crear una etiqueta para mostrar la información del sistema
        self.label_info_sistema = tk.Label(self.ventana_info_sistema, text="", justify="left")
        self.label_info_sistema.pack()

        # Crear e iniciar el hilo aquí
        self.hilo_info_sistema = threading.Thread(target=self.actualizar_info_sistema)
        self.hilo_info_sistema.daemon = True
        self.hilo_info_sistema.start()

    def actualizar_info_sistema(self):
        while True:
            # Información de la batería
            if hasattr(psutil, "sensors_battery"):  # Verificar si el sistema soporta información de la batería
                info_bateria = psutil.sensors_battery()
                if info_bateria:
                    porcentaje_bateria = f"Batería: {info_bateria.percent}%"
                else:
                    porcentaje_bateria = "Batería: No disponible"
            else:
                porcentaje_bateria = "Batería: No soportado"

            # Uso de RAM
            uso_ram = psutil.virtual_memory()
            porcentaje_ram = f"RAM: {uso_ram.percent}% usado"

            # Uso de CPU
            porcentaje_cpu = f"CPU: {psutil.cpu_percent()}% usado"

            # Uso de GPU
            porcentaje_gpu = f"GPU: {psutil.cpu_percent(interval=1)}% usado"

            # Mostrar la información
            mensaje = f"{porcentaje_bateria}\n{porcentaje_ram}\n{porcentaje_cpu}\n{porcentaje_gpu}"
            self.label_info_sistema.config(text=mensaje)

            time.sleep(1)  # Actualizar la información cada segundo