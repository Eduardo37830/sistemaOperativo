import tkinter as tk
from modelos.login import IniciarSesion
from modelos.desktop import Escritorio

class MainApp:
    def __init__(self, root):
        self.root = root
        self.current_view = None
        self.show_login()

    def show_login(self):
        if self.current_view is not None:
            self.current_view.frame.destroy()
        self.current_view = IniciarSesion(self.root, self)

    def show_desktop(self):
        if self.current_view is not None:
            self.current_view.frame.destroy()
        self.current_view = Escritorio(self.root, self)

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()