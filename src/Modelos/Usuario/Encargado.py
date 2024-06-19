from src.Modelos.Usuario.Usuario import Usuario
class Encargado(Usuario):
    def __init__(self, cedula, nombre, direccion, password):
        super().__init__(cedula, nombre, direccion)
        self.password = password
