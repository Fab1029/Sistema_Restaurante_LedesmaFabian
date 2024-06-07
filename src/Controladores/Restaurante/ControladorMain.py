from PyQt6 import QtWidgets
from src.Vistas.Restaurante.Ui_Main import Ui_Main
from src.Modelos.Restaurante.Restaurante import Restaurante
from src.Controladores.Restaurante.ControladorCarta import ControladorCarta
from src.Controladores.Comida.ControladorProducto import ControladorProducto
from src.Controladores.Comida.ControladorIngrediente import ControladorIngrediente
from src.Controladores.Restaurante.ControladorDiaDisponibilidad import ControladorDiaDisponibilidad

class ControladorMain(QtWidgets.QMainWindow, Ui_Main):
    def __init__(self, parent= None):
        super(ControladorMain, self).__init__(parent)
        self.setupUi(self)

        Restaurante.getInstance().cargar_restaurante()


        self.__init__actions()



    def __init__actions(self):
        self.jmbCartaIngresar.triggered.connect(lambda: self.__init__controlador('controlador_carta')(0))
        self.jmbProductoIngresar.triggered.connect(lambda: self.__init__controlador('controlador_producto')(0))
        self.jmbIngredienteIngresar.triggered.connect(lambda: self.__init__controlador('controlador_ingrediente')(0))
        self.jmbDisponibilidadIngresar.triggered.connect(lambda: self.__init__controlador('controlador_dia_disponibilidad')(0))


    def __init__controlador(self, tipo_controlador):
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


        controladores = {'controlador_ingrediente': ingrediente, 'controlador_producto': producto,
                         'controlador_carta': carta, 'controlador_dia_disponibilidad': dia_disponibilidad}

        return controladores[tipo_controlador]

    def closeEvent(self, event):
        Restaurante.getInstance().guardar_restaurante()





