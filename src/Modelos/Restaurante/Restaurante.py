import pickle
from src.Datos.RutaArchivos import RutaArchivos
from src.Modelos.Usuario.Encargado import Encargado

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
        self.turnos = ('Mañana', 'Tarde', 'Noche')

        self.cartas = dict()
        self.reservas = dict()
        self.productos = dict()
        self.encargados = dict()
        self.ingredientes = dict()
        self.dias_disponibilidad = dict()

        self.cargar_restaurante()
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
