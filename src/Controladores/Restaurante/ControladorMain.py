from PyQt6 import QtWidgets
from src.Vistas.Restaurante.Ui_Main import Ui_Main
from src.Controladores.Comida.ControladorIngrediente import ControladorIngrediente

class ControladorMain(QtWidgets.QMainWindow, Ui_Main):
    def __init__(self, parent= None):
        super(ControladorMain, self).__init__(parent)
        self.setupUi(self)

        self.jmbIngredienteIngresar.triggered.connect(lambda: self.__init__controlador('controlador_ingrediente')(0))


    def __init__controlador(self, tipo_controlador):
        self.hide()
        def ingrediente(seccion):
            self.ventana = ControladorIngrediente(self.show, seccion)
            self.ventana.show()


        controladores = {'controlador_ingrediente': ingrediente}

        return controladores[tipo_controlador]


