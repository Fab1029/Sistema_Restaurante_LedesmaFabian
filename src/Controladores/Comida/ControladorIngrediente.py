from PyQt6 import QtWidgets
from src.Vistas.Comida.Ui_Ingrediente import Ui_Ingrediente
from src.Modelos.Comida.TiposIngredientes import TiposIngredientes
from src.Modelos.Comida.MedidaIngrediente import MedidaIngrediente
class ControladorIngrediente(QtWidgets.QWidget, Ui_Ingrediente):
    def __init__(self, controlador_anterior, seccion, parent= None):
        super(ControladorIngrediente, self).__init__(parent)
        self.setupUi(self)


        #Se manda el metodo para hacer visible el controlador anterior
        self.controlador_anterior = controlador_anterior

        self.__init__seccion(seccion)()


    def __init__seccion(self, seccion):
        def ingresar():
            self.tbIngrediente.setCurrentIndex(0)
            self.cmbTipoIngresar.clear()
            self.cmbMedidaIngresar.clear()
            self.cmbTipoIngresar.addItems(list(TiposIngredientes().tipos_ingredientes))
            self.cmbMedidaIngresar.addItems(list(MedidaIngrediente().medida_ingrediente))
        def modificar():
            self.tbIngrediente.setCurrentIndex(1)
            self.cmbTipoModificar.clear()
            self.cmbMedidaModificar.clear()
            self.cmbNombreModificar.clear()
            #Aqui falta poner los items y designarlos a la poscion que corresponden
        def eliminar():
            self.tbIngrediente.setCurrentIndex(2)
            self.cmbNombreEliminar.clear()
            #Aqui falta poner los difrentes nombre existentes

        def listar():
            self.tbIngrediente.setCurrentIndex(3)
            self.jgdIngredientes.clear()
            #Aqui falta pner columnas y los datos


        secciones = {0: ingresar, 1: modificar, 2: eliminar, 3: listar}

        return secciones[seccion]

    def closeEvent(self, event):
        self.controlador_anterior()



