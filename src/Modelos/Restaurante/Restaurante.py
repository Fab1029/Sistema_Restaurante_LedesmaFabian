class Restaurante:
    def __init__(self, ruc, email, nombre, telefono, razon_social, ubicacion):
        self.ruc = ruc
        self.email = email
        self.nombre = nombre
        self.telefono = telefono
        self. razon_social = razon_social
        self.ubicacion = ubicacion

        self.cartas = dict()
        self.reservas = dict()
        self.productos = dict()
        self.ingredientes = dict()
        self.dias_disponibilidad = dict()

    def agregar_carta_a_restaurante(self, carta):
        self.cartas[carta.fecha_validez][carta.nombre] = carta if carta.fecha_validez in self.cartas and carta.nombre not in self.cartas[carta.fecha_validez] else self.cartas[carta.fecha_validez] = {carta.nombre: carta} if carta.fecha_validez not in self.cartas else None

    def eliminar_carta_de_restaurante(self, fecha, nombre):
        if fecha in self.cartas and nombre in self.cartas[fecha]: self.cartas[fecha].pop(nombre)

    def agregar_alimento_a_restaurante(self, ingrediente):
        if ingrediente.nombre not in self.ingredientes: self.ingredientes[ingrediente.nombre] = ingrediente

    def eliminar_alimento_de_restaurante(self, nombre):
        if nombre in self.ingredientes: self.ingredientes.pop(nombre)

    def agregar_producto_a_restaurante(self, producto):
        if producto.nombre not in self.productos: self.productos[producto.nombre] = producto

    def eliminar_producto_de_restaurante(self, nombre):
        if nombre in self.productos: self.productos.pop(nombre)

    def agregar_reserva_a_restaurante(self, reserva):
        if reserva.numero_reserva not in self.reservas: self.reservas[reserva.numero_reserva] = reserva

    def eliminar_reserva_de_restaurante(self, numero_reserva):
        if numero_reserva in self.reservas: self.reservas.pop(numero_reserva)

    def verificar_disponibilidad(self, fecha, hora):
        pass