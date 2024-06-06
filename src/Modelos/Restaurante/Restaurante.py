import pickle
from src.Datos.RutaArchivos import RutaArchivos
class Restaurante:
    __instance = None
    @staticmethod
    def getInstance() -> 'Restaurante':
        if Restaurante.__instance is None:
            Restaurante()
        return Restaurante.__instance

    def __init__(self):
        Restaurante.__instance = self

        self.ruc = ''
        self.email = ''
        self.nombre = ''
        self.telefono = ''
        self.ubicacion = ''
        self. razon_social = ''

        self.cartas = dict()
        self.reservas = dict()
        self.productos = dict()
        self.ingredientes = dict()
        self.dias_disponibilidad = dict()

        self.cargar_restaurante()

    def agregar_carta_a_restaurante(self, carta):
        if carta.fecha_validez not in self.cartas:
            self.cartas[carta.fecha_validez] = {}
        self.cartas[carta.fecha_validez][carta.nombre] = carta

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

    def cargar_restaurante(self):
        [self.cargar_datos_restaurante(1)(path[0], atributo, path[1]) for path, atributo in zip(RutaArchivos().rutas, [self.cartas, self.reservas, self.productos, self.ingredientes, self.dias_disponibilidad])]
        self.cargar_datos_restaurante(2)()

    def guardar_restaurante(self):
        [self.guardar_datos_restaurante(1)(path[0], atributo, path[1]) for path, atributo in zip(RutaArchivos().rutas, [self.cartas, self.reservas, self.productos, self.ingredientes, self.dias_disponibilidad])]
        self.guardar_datos_restaurante(2)()

    def cargar_datos_restaurante(self, carga):
        def cargar_datos_generales(path, atributo, cadena):
            try:
                with open(path, 'rb') as file:
                    atributo.update(pickle.load(file))
            except:
                print(cadena)

        def cargar_informacion_restaurante():
            try:
                with open('./Datos/InformacionRestaurante.dat', 'rb') as file:
                    self.ruc = pickle.load(file)
                    self.email = pickle.load(file)
                    self.nombre = pickle.load(file)
                    self.telefono = pickle.load(file)
                    self.ubicacion = pickle.load(file)
                    self. razon_social = pickle.load(file)

            except Exception as e:
                print(e)

        cargar_datos = {1: cargar_datos_generales,
                        2: cargar_informacion_restaurante}

        return cargar_datos[carga]
    def guardar_datos_restaurante(self, carga):
        def guardar_datos_generales(path, atributo, cadena):
            try:
                with open(path, 'wb') as file:
                    pickle.dump(atributo, file, pickle.HIGHEST_PROTOCOL)
            except:
                print(cadena)
        def guardar_informacion_restaurante():
            try:
                with open('./Datos/InformacionRestaurante.dat', 'wb') as file:
                    pickle.dump(self.ruc, file, pickle.HIGHEST_PROTOCOL)
                    pickle.dump(self.email, file, pickle.HIGHEST_PROTOCOL)
                    pickle.dump(self.nombre, file, pickle.HIGHEST_PROTOCOL)
                    pickle.dump(self.telefono, file, pickle.HIGHEST_PROTOCOL)
                    pickle.dump(self.ubicacion, file, pickle.HIGHEST_PROTOCOL)
                    pickle.dump(self.razon_social, file, pickle.HIGHEST_PROTOCOL)
            except Exception as e:
                print(e)

        guardar_datos = {1: guardar_datos_generales,
                        2: guardar_informacion_restaurante}

        return guardar_datos[carga]
