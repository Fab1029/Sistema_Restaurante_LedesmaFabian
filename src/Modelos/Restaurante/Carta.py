class Carta:
    def __init__(self, nombre, fecha_validez):
        self.nombre = nombre
        self.productos = list()
        self.fecha_validez = fecha_validez #Tener en cuenta que paso tipo datetime object

    def agregar_producto_a_carta(self, producto):
        if producto not in self.productos: self.productos.append(producto)

    def eliminar_producto_de_carta(self, indice_producto):
        if indice_producto < len(self.productos): self.productos.pop(indice_producto)