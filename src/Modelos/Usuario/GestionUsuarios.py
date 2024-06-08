import pickle

from src.Datos.RutaArchivos import RutaArchivos
from src.Modelos.Usuario.Encargado import Encargado
class GestionUsuarios:
    __instance = None
    @staticmethod
    def getInstance() -> 'GestionUsuarios':
        if GestionUsuarios.__instance is None:
            GestionUsuarios()
        return GestionUsuarios.__instance
    def __init__(self):
        GestionUsuarios.__instance = self

        self.encargados = dict()
        self.cargar()
        self.cargar_admin()

    def cargar_admin(self):
        self.encargados['0000000000'] = Encargado('0000000000', 'admin', 'admin', 'admin')

    def cargar(self):
        self.cargar_datos_usuarios(1)(RutaArchivos().rutas[-1][0], self.encargados, RutaArchivos().rutas[-1][1])

    def guardar(self):
        self.guardar_datos_usuarios(1)(RutaArchivos().rutas[-1][0], self.encargados, RutaArchivos().rutas[-1][1])

    def cargar_datos_usuarios(self, carga):
        def cargar_datos_encargados(path, atributo, cadena):
            try:
                with open(path, 'rb') as file:
                    atributo.update(pickle.load(file))
            except:
                print(cadena)

        cargar_datos = {1: cargar_datos_encargados}

        return cargar_datos[carga]
    def guardar_datos_usuarios(self, carga):
        def guardar_datos_encargados(path, atributo, cadena):
            try:
                with open(path, 'wb') as file:
                    pickle.dump(atributo, file, pickle.HIGHEST_PROTOCOL)
            except:
                print(cadena)

        guardar_datos = {1: guardar_datos_encargados}

        return guardar_datos[carga]