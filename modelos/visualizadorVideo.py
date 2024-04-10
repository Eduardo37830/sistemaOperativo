import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
import cv2
import threading
import time  # Importa time para manejar pausas

class VisualizadorVideos:
    def __init__(self, master):
        self.master = master
        self.master.title("Visualizador de Videos")
        self.master.geometry("1280x720")

        self.captura = None
        self.frame = None
        self.hilo_video = None
        self.reproduciendo = False
        self.pausado = False  # Añadir un nuevo estado para manejar la pausa

        self.crear_interfaz()

    def crear_interfaz(self):
        self.panel_video = tk.Label(self.master)
        self.panel_video.pack()

        # Barra de opciones
        self.barra_opciones = tk.Frame(self.master, bg="#0078D7", height=40)
        self.barra_opciones.pack(side="bottom", fill="x", padx=10, pady=(0, 10))

        # Centrar botones horizontalmente
        self.barra_opciones.place(relx=0.5, rely=1, anchor="s")


        self.boton_cargar = ttk.Button(self.barra_opciones, text="Cargar Video", command=self.cargar_video)
        self.boton_cargar.pack(pady=5, padx=10, side="left")

        self.boton_reproducir = ttk.Button(self.barra_opciones, text="Reproducir", command=self.iniciar_reproduccion)
        self.boton_reproducir.pack(pady=5, padx=10, side="left")

        self.boton_pausar = ttk.Button(self.barra_opciones, text="Pausa", command=self.pausar_reproduccion, state='disabled')  # Botón para pausar/reanudar
        self.boton_pausar.pack(pady=5, padx=10, side="left")

        self.boton_detener = ttk.Button(self.barra_opciones, text="Detener", command=self.detener_reproduccion, state='disabled')
        self.boton_detener.pack(pady=5, padx=10, side="left")

    def cargar_video(self):
        ruta_video = filedialog.askopenfilename(filetypes=[("Archivos de video", "*.mp4;*.avi;*.mov")])
        if ruta_video:
            self.captura = cv2.VideoCapture(ruta_video)
            self.boton_reproducir["state"] = "normal"
            self.boton_pausar["state"] = "normal"
            self.boton_detener["state"] = "disabled"

    def actualizar_frame(self):
        while self.reproduciendo:
            if self.pausado:  # Si el video está pausado, espera
                continue
            ret, frame = self.captura.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                im = Image.fromarray(frame)
                img = ImageTk.PhotoImage(image=im)
                self.panel_video.configure(image=img)
                self.panel_video.image = img
                time.sleep(0.03)  # Ajusta este valor si es necesario
            else:
                self.detener_reproduccion()
                break

    def iniciar_reproduccion(self):
        if not self.reproduciendo:
            self.reproduciendo = True
            self.pausado = False
            self.hilo_video = threading.Thread(target=self.actualizar_frame)
            self.hilo_video.start()
            self.boton_detener["state"] = "normal"
            self.boton_pausar["state"] = "normal"
            self.boton_reproducir["state"] = "disabled"

    def pausar_reproduccion(self):
        if self.pausado:  # Si ya está pausado, reanudar
            self.pausado = False
            self.boton_pausar["text"] = "Pausa"
        else:  # Si no está pausado, pausar
            self.pausado = True
            self.boton_pausar["text"] = "Reanudar"

    def detener_reproduccion(self):
        self.reproduciendo = False
        self.pausado = False  # Restablece el estado de pausa
        if self.captura is not None:
            self.captura.release()
        self.captura = None
        self.boton_reproducir["state"] = "normal"
        self.boton_pausar["state"] = "disabled"
        self.boton_detener["state"] = "disabled"
