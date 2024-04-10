import pygame
import tkinter as tk
from tkinter import ttk, filedialog

class ReproductorAudio:
    def __init__(self, master):
        self.master = master
        self.master.title("Reproductor de Audio")
        self.master.geometry("300x100")

        pygame.mixer.init()  # Inicializa el módulo mixer de pygame

        self.estado_reproduccion = "stopped"

        self.crear_interfaz()

    def crear_interfaz(self):
        ttk.Button(self.master, text="Cargar Audio", command=self.cargar_audio).pack()
        ttk.Button(self.master, text="Play", command=self.play_audio).pack()
        ttk.Button(self.master, text="Pausa", command=self.pausar_audio).pack()
        ttk.Button(self.master, text="Detener", command=self.detener_audio).pack()

    def cargar_audio(self):
        ruta_audio = filedialog.askopenfilename(filetypes=[("Archivos de audio", "*.mp3;*.wav")])
        if ruta_audio:
            pygame.mixer.music.load(ruta_audio)
            self.estado_reproduccion = "paused"

    def play_audio(self):
        if self.estado_reproduccion != "playing":
            pygame.mixer.music.play()
            self.estado_reproduccion = "playing"

    def pausar_audio(self):
        if self.estado_reproduccion == "playing":
            pygame.mixer.music.pause()
            self.estado_reproduccion = "paused"
        elif self.estado_reproduccion == "paused":
            pygame.mixer.music.unpause()
            self.estado_reproduccion = "playing"

    def detener_audio(self):
        pygame.mixer.music.stop()
        self.estado_reproduccion = "stopped"
