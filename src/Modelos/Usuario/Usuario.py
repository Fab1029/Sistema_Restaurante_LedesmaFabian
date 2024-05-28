class Usuario:
    def __init__(self, cedula, nombre, email, direccion):
        self.email = email
        self.cedula = cedula
        self.nombre = nombre
        self.direccion = direccion
        self.preferencia_comida = list() #Lista de comidas


    def añadir_preferencia_comida(self):
        pass