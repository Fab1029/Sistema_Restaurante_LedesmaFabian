class Pedido:
    def __init__(self, numero_pedido, producto, cantidad):
        self.producto = producto
        self.cantidad = cantidad
        self.numero_pedido = numero_pedido

    def modificar_pedido(self, producto, cantidad):
        self.cantidad = cantidad
        self.producto = producto

    def __str__(self):
        return f'El producto es: {self.producto} y su cantidad: {self.cantidad}'