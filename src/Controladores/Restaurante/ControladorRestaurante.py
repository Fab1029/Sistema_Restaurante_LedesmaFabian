from PyQt6 import QtWidgets
from src.Vistas.Restaurante.Ui_Main import Ui_Main
from src.Modelos.Restaurante.Restaurante import Restaurante
from src.Modelos.Usuario.GestionUsuarios import GestionUsuarios
from src.Controladores.Restaurante.ControladorCarta import ControladorCarta
from src.Controladores.Comida.ControladorProducto import ControladorProducto
from src.Controladores.Comida.ControladorIngrediente import ControladorIngrediente
from src.Controladores.Usuario.ControladorGestionEncargado import ControladorGestionEncargado
from src.Controladores.Restaurante.ControladorDiaDisponibilidad import ControladorDiaDisponibilidad

class ControladorRestaurante(QtWidgets.QMainWindow, Ui_Main):

    def __init__(self, parent= None):
        super(ControladorRestaurante, self).__init__(parent)
        self.setupUi(self)

        self.init_actions()
        self.restaurante = Restaurante.getInstance().cargar_restaurante()


    def init_actions(self):
        self.jmbSalir.triggered.connect(self.salir)
        self.jmbCartaIngresar.triggered.connect(lambda: self.init_controlador('controlador_carta')(0))
        self.jmbProductoIngresar.triggered.connect(lambda: self.init_controlador('controlador_producto')(0))
        self.jmbIngredienteIngresar.triggered.connect(lambda: self.init_controlador('controlador_ingrediente')(0))
        self.jmbPersonalIngresar.triggered.connect(lambda: self.init_controlador('controlador_gestion_encargado')(0))
        self.jmbDisponibilidadIngresar.triggered.connect(lambda: self.init_controlador('controlador_dia_disponibilidad')(0))

    def init_controlador(self, tipo_controlador):
        self.hide()
        def ingrediente(seccion):
            self.ventana = ControladorIngrediente(self.show, seccion)
            self.ventana.show()
        def producto(seccion):
            self.ventana = ControladorProducto(self.show, seccion)
            self.ventana.show()
        def carta(seccion):
            self.ventana = ControladorCarta(self.show, seccion)
            self.ventana.show()
        def dia_disponibilidad(seccion):
            self.ventana = ControladorDiaDisponibilidad(self.show, seccion)
            self.ventana.show()
        def encargado(seccion):
            self.ventana = ControladorGestionEncargado(self.show, seccion)
            self.ventana.show()


        controladores = {'controlador_ingrediente': ingrediente, 'controlador_producto': producto,
                         'controlador_carta': carta, 'controlador_dia_disponibilidad': dia_disponibilidad,
                         'controlador_gestion_encargado': encargado}

        return controladores[tipo_controlador]

    def salir(self):
        GestionUsuarios.getInstance().guardar()
        Restaurante.getInstance().guardar_restaurante()
        self.close()

    def closeEvent(self, event):
        GestionUsuarios.getInstance().guardar()
        Restaurante.getInstance().guardar_restaurante()







