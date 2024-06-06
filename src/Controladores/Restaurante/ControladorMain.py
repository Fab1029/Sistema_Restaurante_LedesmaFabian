from PyQt6 import QtWidgets
from src.Vistas.Restaurante.Ui_Main import Ui_Main
from src.Modelos.Restaurante.Restaurante import Restaurante
from src.Controladores.Comida.ControladorProducto import ControladorProducto
from src.Controladores.Comida.ControladorIngrediente import ControladorIngrediente

class ControladorMain(QtWidgets.QMainWindow, Ui_Main):
    def __init__(self, parent= None):
        super(ControladorMain, self).__init__(parent)
        self.setupUi(self)

        Restaurante.getInstance().cargar_restaurante()

        self.__init__actions()



    def __init__actions(self):
        self.jmbProductoIngresar.triggered.connect(lambda: self.__init__controlador('controlador_producto')(0))
        self.jmbIngredienteIngresar.triggered.connect(lambda: self.__init__controlador('controlador_ingrediente')(0))

    def __init__controlador(self, tipo_controlador):
        self.hide()
        def ingrediente(seccion):
            self.ventana = ControladorIngrediente(self.show, seccion)
            self.ventana.show()
        def producto(seccion):
            self.ventana = ControladorProducto(self.show, seccion)
            self.ventana.show()


        controladores = {'controlador_ingrediente': ingrediente, 'controlador_producto': producto}

        return controladores[tipo_controlador]

    def closeEvent(self, event):
        Restaurante.getInstance().guardar_restaurante()





