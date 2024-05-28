class Ubicacion:
    def __init__(self, latitud, longitud, direccion):
        self.latitud = latitud
        self.longitud = longitud
        self.direccion = direccion

    def __str__(self):
        return f'El restaunate se encuentra en la direccion: {self.direccion}, en las coordenadas longitud: {self.longitud}, latitud: {self.latitud}'