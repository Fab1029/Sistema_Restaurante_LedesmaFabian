class Reserva:
    def __init__(self, fecha, turno, numero_reserva, numero_comensales, pedidos):
        self.fecha = fecha # Debe ser un objeto tipo datetime
        self.turno = turno # Debe ser objto tipo time
        self.numero_reserva = numero_reserva
        self.numero_comensales = numero_comensales
        self.pedidos = pedidos


