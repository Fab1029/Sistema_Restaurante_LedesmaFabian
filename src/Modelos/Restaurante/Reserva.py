class Reserva:
    def __init__(self, fecha, hora, numero_reserva, numero_comensales):
        self.fecha = fecha # Debe ser un objeto tipo datetime
        self.hora = hora # Debe ser objto tipo time
        self.numero_reserva = numero_reserva
        self.numero_comensales = numero_comensales
        self.pedidos = dict()


    def agregar_pedido_a_reserva(self, pedido):
        if pedido.numero_pedido not in self.pedidos: self.pedidos[pedido.numero_pedido] = pedido

    def eliminar_pedido_de_reserva(self, numero_pedido):
        if numero_pedido in self.pedidos: self.pedidos.pop(numero_pedido)