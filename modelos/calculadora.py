import tkinter as tk
from tkinter import ttk
import math

class CalculadoraCientifica:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculadora Científica")
        self.master.geometry("400x600")

        # Asegúrate de que todos los elementos en `master` usen `grid`
        self.pantalla = ttk.Entry(master, font=("Segoe UI", 18), justify="right")
        self.pantalla.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)

        self.crear_botones()

    def crear_botones(self):
        botones = [
            ('7', 1), ('8', 1), ('9', 1), ('/', 1),
            ('4', 2), ('5', 2), ('6', 2), ('*', 2),
            ('1', 3), ('2', 3), ('3', 3), ('-', 3),
            ('0', 4), ('.', 4), ('=', 4), ('+', 4),
            ('sin', 5), ('cos', 5), ('tan', 5), ('AC', 6),
            ('log', 6), ('exp', 6), ('sqrt', 6)
        ]

        for texto, fila in botones:
            boton = ttk.Button(self.master, text=texto, command=lambda t=texto: self.click_boton(t))
            boton.grid(row=fila, column=botones.index((texto, fila)) % 4, sticky="nsew", padx=5, pady=5)
            self.master.grid_columnconfigure(botones.index((texto, fila)) % 4, weight=1)

        for i in range(7):
            self.master.grid_rowconfigure(i, weight=1)

    def click_boton(self, valor):
        if valor == "=":
            try:
                resultado = eval(self.pantalla.get())
                self.pantalla.delete(0, tk.END)
                self.pantalla.insert(tk.END, str(resultado))
            except Exception as e:
                self.pantalla.delete(0, tk.END)
                self.pantalla.insert(tk.END, "Error")
        elif valor == "AC":
            self.pantalla.delete(0, tk.END)
        elif valor in ('sin', 'cos', 'tan', 'log', 'exp', 'sqrt'):
            try:
                expresion = self.pantalla.get()
                resultado = ''
                if valor == 'sin':
                    resultado = math.sin(math.radians(float(expresion)))
                elif valor == 'cos':
                    resultado = math.cos(math.radians(float(expresion)))
                elif valor == 'tan':
                    resultado = math.tan(math.radians(float(expresion)))
                elif valor == 'log':
                    resultado = math.log(float(expresion))
                elif valor == 'exp':
                    resultado = math.exp(float(expresion))
                elif valor == 'sqrt':
                    resultado = math.sqrt(float(expresion))
                self.pantalla.delete(0, tk.END)
                self.pantalla.insert(tk.END, str(resultado))
            except Exception as e:
                self.pantalla.delete(0, tk.END)
                self.pantalla.insert(tk.END, "Error")
        else:
            self.pantalla.insert(tk.END, valor)
