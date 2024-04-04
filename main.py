#Sistemas Operativos, escritorio con tkinter
#Autor: Eduardo Villamil


import tkinter as tk
from modelos.login import IniciarSesion

if __name__ == "__main__":
    root = tk.Tk()
    login = IniciarSesion(root)
    root.mainloop()