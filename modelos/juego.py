import tkinter as tk
import random
from tkinter import messagebox


class JuegoCulebrita:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.frame = tk.Frame(self.root)
        self.frame.pack(fill="both", expand=True)
        self.velocidad = 100  # Velocidad inicial de movimiento
        self.puntaje = 0
        self.setup_ui()

    def setup_ui(self):
        self.root.title("Juego de la Culebrita")
        self.root.geometry("1920x1080")
        self.root.state('zoomed')

        # Define el ancho y la altura del juego
        game_width = 800
        game_height = 600

        # Calcula las coordenadas x e y para centrar el juego en la ventana
        position_left = int(self.root.winfo_screenwidth() / 2 - game_width / 2)
        position_top = int(self.root.winfo_screenheight() / 2 - game_height / 2)

        self.marcador = tk.Label(self.frame, text="Puntaje: 0", font=("Arial", 14))
        self.marcador.place(x=position_left + 40, y=position_top - 40)  # Coloca el marcador encima del juego

        self.canvas = tk.Canvas(self.frame, bg="lightgray", width=game_width, height=game_height, bd=0, highlightthickness=0)
        self.canvas.place(x=position_left, y=position_top)  # Centra el juego en la ventana
        self.canvas.focus_set()  # El foco directamente al canvas
        self.canvas.bind("<KeyPress>", self.mover_culebra)

        self.culebra = [(100, 100), (90, 100), (80, 100)]
        self.direccion = "Right"
        self.direcciones_opuestas = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}
        self.comida = self.generar_comida()
        self.dibujar_culebra()
        self.dibujar_comida()
        self.mover()
        self.canvas.create_rectangle(0, 0, game_width, game_height, outline="blue")

        # Botón para reiniciar el juego
        boton_reiniciar = tk.Button(self.frame, text="Reiniciar", command=self.reiniciar)
        boton_reiniciar.place(x=position_left + 40, y=position_top + game_height + 20)

        # Botón para salir del juego
        boton_salir = tk.Button(self.frame, text="Salir", command=self.salir)
        boton_salir.place(x=position_left + 120, y=position_top + game_height + 20)



    def mover(self):
        cabeza_x, cabeza_y = self.culebra[0]
        movimientos = {"Up": (cabeza_x, cabeza_y - 10), "Down": (cabeza_x, cabeza_y + 10),
                       "Left": (cabeza_x - 10, cabeza_y), "Right": (cabeza_x + 10, cabeza_y)}
        nueva_cabeza = movimientos[self.direccion]

        if nueva_cabeza == self.comida:
            self.culebra.insert(0, nueva_cabeza)
            self.comida = self.generar_comida()
            self.puntaje += 1
            if self.puntaje % 5 == 0:
                self.velocidad -= 10
            self.marcador.config(text=f"Puntaje: {self.puntaje}") # Actualiza el marcador
        else:
            self.culebra.insert(0, nueva_cabeza)
            self.culebra.pop()

        self.dibujar_culebra()
        self.dibujar_comida()

        if self.colision():
            self.game_over()
        else:
            self.root.after(self.velocidad, self.mover)

    def mover_culebra(self, event):
        nueva_direccion = event.keysym
        if nueva_direccion in self.direcciones_opuestas and \
                self.direccion != self.direcciones_opuestas[nueva_direccion]:
            self.direccion = nueva_direccion

    def dibujar_culebra(self):
        self.canvas.delete("culebra")  # Elimina todas las partes anteriores de la culebra
        for x, y in self.culebra:
            self.canvas.create_rectangle(x, y, x + 10, y + 10, fill="green", tags="culebra")

    def dibujar_comida(self):
        self.canvas.delete("comida")
        x, y = self.comida
        self.canvas.create_rectangle(x, y, x + 10, y + 10, fill="red", tags="comida")

    def generar_comida(self):
        return random.randint(0, 79) * 10, random.randint(0, 59) * 10

    def colision(self):
        cabeza = self.culebra[0]
        return (
                cabeza in self.culebra[1:] or
                cabeza[0] < 0 or cabeza[0] >= 800 or
                cabeza[1] < 0 or cabeza[1] >= 600
        )

    def game_over(self):
        self.controller.show_desktop()

    def reiniciar(self):
        self.culebra = [(100, 100), (90, 100), (80, 100)]
        self.direccion = "Right"
        self.comida = self.generar_comida()
        self.dibujar_culebra()
        self.dibujar_comida()
        self.mover()

    def salir(self):
        self.frame.destroy()
        self.controller.show_desktop()

    def __del__(self):
        self.frame.destroy()
