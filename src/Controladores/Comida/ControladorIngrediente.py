from PyQt6 import QtWidgets
from src.Modelos.Comida.Ingrediente import Ingrediente
from src.Vistas.Comida.Ui_Ingrediente import Ui_Ingrediente
from src.Modelos.Restaurante.Restaurante import Restaurante
from src.Modelos.Comida.TiposIngredientes import TiposIngredientes
from src.Modelos.Comida.MedidaIngrediente import MedidaIngrediente
class ControladorIngrediente(QtWidgets.QWidget, Ui_Ingrediente):
    def __init__(self, controlador_anterior, seccion, parent= None):
        super(ControladorIngrediente, self).__init__(parent)
        self.setupUi(self)

        #Restaurante
        self.resturante = Restaurante.getInstance()
        #Se manda el metodo para hacer visible el controlador anterior
        self.controlador_anterior = controlador_anterior

        self.__init__actions()
        self.__init__seccion(seccion)()

    def __init__actions(self):
        self.btnElimarIngrediente.clicked.connect(self.eliminar_ingrediente_action)
        self.btnGuardarCambios.clicked.connect(self.modificar_ingrediente_action)
        self.btnIngresarIngrediente.clicked.connect(self.ingresar_ingrediente_action)
        self.tbIngrediente.currentChanged.connect(lambda: self.__init__seccion(self.tbIngrediente.currentIndex())())

    def eliminar_ingrediente_action(self):
        self.resturante.ingredientes.pop(self.cmbNombreEliminar.currentText())
        self.__init__seccion(2)()
        self.verificar_pestana()
    def ingresar_ingrediente_action(self):
        self.resturante.ingredientes.update({self.txtNombreIngresar.text(): Ingrediente(self.txtNombreIngresar.text(), self.cmbTipoIngresar.currentText(), self.cmbMedidaIngresar.currentText())}) if self.txtNombreIngresar.text() else print('Ingrese nombre')
        self.__init__seccion(0)()
        self.verificar_pestana()
    def modificar_ingrediente_action(self):
        self.resturante.ingredientes.update({self.cmbNombreModificar.currentText(): Ingrediente(self.cmbNombreModificar.currentText(), self.cmbTipoModificar.currentText(), self.cmbMedidaModificar.currentText())})
    def listar_ingredientes_action(self):
        #Arreglar problemas en anadir valores a tabla
        pass
    def nombre_modificar_action(self):
        self.cmbTipoModificar.setCurrentIndex(self.cmbTipoModificar.findText(self.resturante.ingredientes[self.cmbNombreModificar.currentText()].tipo))
        self.cmbMedidaModificar.setCurrentIndex(self.cmbMedidaModificar.findText(self.resturante.ingredientes[self.cmbNombreModificar.currentText()].medida))

    def __init__seccion(self, seccion):
        self.desconectar_conexion()
        def ingresar():
            self.tbIngrediente.setCurrentIndex(0)
            self.cmbTipoIngresar.clear()
            self.cmbMedidaIngresar.clear()
            self.txtNombreIngresar.clear()
            self.cmbTipoIngresar.addItems(list(TiposIngredientes().tipos_ingredientes))
            self.cmbMedidaIngresar.addItems(list(MedidaIngrediente().medida_ingrediente))

        def modificar():
            self.tbIngrediente.setCurrentIndex(1)
            self.cmbTipoModificar.clear()
            self.cmbMedidaModificar.clear()
            self.cmbNombreModificar.clear()
            self.cmbNombreModificar.addItems(list(self.resturante.ingredientes.keys()))
            self.cmbTipoModificar.addItems(list(TiposIngredientes().tipos_ingredientes))
            self.cmbMedidaModificar.addItems(list(MedidaIngrediente().medida_ingrediente))
            self.nombre_modificar_action()

            self.conectar_conexion()

        def eliminar():
            self.tbIngrediente.setCurrentIndex(2)
            self.cmbNombreEliminar.clear()
            self.cmbNombreEliminar.addItems(list(self.resturante.ingredientes.keys()))

        def listar():
            self.tbIngrediente.setCurrentIndex(3)
            self.jgdIngredientes.clear()
            self.listar_ingredientes_action()


        secciones = {0: ingresar, 1: modificar, 2: eliminar, 3: listar}

        return secciones[seccion]

    def desconectar_conexion(self):
        try:
            self.cmbNombreModificar.disconnect()
        except:
            pass
    def conectar_conexion(self):
        try:
            self.cmbNombreModificar.currentIndexChanged.connect(self.nombre_modificar_action)
        except:
            pass

    def verificar_pestana(self):
        if self.resturante.ingredientes:
            [self.tbIngrediente.setTabEnabled(indice, True) for indice in range(1,4)]
        else:
            self.tbIngrediente.setCurrentIndex(0)
            [self.tbIngrediente.setTabEnabled(indice, False) for indice in range(1,4)]

    def closeEvent(self, event):
        self.controlador_anterior()



