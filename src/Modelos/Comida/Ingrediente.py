class Ingrediente:
    def __init__(self, nombre, tipo, medida):
        self.tipo = tipo
        self.nombre = nombre
        self.medida = medida

    def __str__(self):
        return f'{self.nombre} es de tipo {self.tipo} y usa la medida {self.medida}'