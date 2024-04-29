import json
import os
from hashlib import sha256

class GestorUsuarios:
    def __init__(self, archivo_usuarios='usuarios.json'):
        self.archivo_usuarios = archivo_usuarios
        self.usuarios = self.cargar_usuarios()

    def cargar_usuarios(self):
        if not os.path.exists(self.archivo_usuarios):
            return {}
        with open(self.archivo_usuarios, 'r') as file:
            return json.load(file)

    def guardar_usuarios(self):
        with open(self.archivo_usuarios, 'w') as file:
            json.dump(self.usuarios, file, indent=4)

    def registrar_usuario(self, usuario, contrasena):
        if usuario in self.usuarios:
            return False  # Usuario ya existe
        hash_contrasena = sha256(contrasena.encode()).hexdigest()
        self.usuarios[usuario] = hash_contrasena
        self.guardar_usuarios()
        return True

    def verificar_credenciales(self, usuario, contrasena):
        hash_contrasena = sha256(contrasena.encode()).hexdigest()
        return self.usuarios.get(usuario) == hash_contrasena