class Usuario:
    def __init__(self, cedula, nombre, email, direccion):
        self.email = email
        self.cedula = cedula
        self.nombre = nombre
        self.direccion = direccion
        self.preferencia_comida = list() #Lista de comidas


    def agregar_preferencia_comida(self, comida):
        if comida not in self.preferencia_comida: self.preferencia_comida.append(comida)