from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QTableWidgetItem
from src.Modelos.Comida.Ingrediente import Ingrediente
from src.Vistas.Comida.Ui_Ingrediente import Ui_Ingrediente
from src.Modelos.Restaurante.Restaurante import Restaurante
from src.Modelos.Comida.TiposIngredientes import TiposIngredientes
from src.Modelos.Comida.MedidaIngrediente import MedidaIngrediente


class ControladorIngrediente(QtWidgets.QWidget, Ui_Ingrediente):
    def __init__(self, controlador_anterior, seccion, parent= None):
        super(ControladorIngrediente, self).__init__(parent)
        self.setupUi(self)

        #Centrar pantalla
        self.move(QApplication.primaryScreen().availableGeometry().center() - self.rect().center())

        #Restaurante
        self.resturante = Restaurante.getInstance()
        #Se manda el metodo para hacer visible el controlador anterior
        self.controlador_anterior = controlador_anterior

        self.verificar_pestana()
        self.init_seccion(seccion)()
        self.init_actions()

    def init_actions(self):
        self.btnElimarIngrediente.clicked.connect(self.eliminar_ingrediente_action)
        self.btnGuardarCambios.clicked.connect(self.modificar_ingrediente_action)
        self.btnIngresarIngrediente.clicked.connect(self.ingresar_ingrediente_action)
        self.tbIngrediente.currentChanged.connect(lambda: self.init_seccion(self.tbIngrediente.currentIndex())())

    def eliminar_ingrediente_action(self):
        self.resturante.ingredientes.pop(self.cmbNombreEliminar.currentText())
        self.init_seccion(2)()
        self.verificar_pestana()
        self.dialogo_informacion('Éxito', 'Ingrediente eliminado exitosamente')
    def ingresar_ingrediente_action(self):
        if self.txtNombreIngresar.text():
            self.resturante.ingredientes.update({self.txtNombreIngresar.text(): Ingrediente(self.txtNombreIngresar.text(), self.cmbTipoIngresar.currentText(), self.cmbMedidaIngresar.currentText())})
            self.init_seccion(0)()
            self.verificar_pestana()
            self.dialogo_informacion('Éxito', 'Ingreso de ingrediente exitoso')
        else:
            self.dialogo_informacion('Alerta', 'Ingrese el nombre del ingrediente')
    def modificar_ingrediente_action(self):
        self.resturante.ingredientes.update({self.cmbNombreModificar.currentText(): Ingrediente(self.cmbNombreModificar.currentText(), self.cmbTipoModificar.currentText(), self.cmbMedidaModificar.currentText())})
        self.dialogo_informacion('Éxito', 'Ingrediente modificado exitosamente')

    def listar_ingredientes_action(self):
        self.jgdIngredientes.clear()
        self.jgdIngredientes.setColumnCount(3)
        self.jgdIngredientes.setRowCount(len(self.resturante.ingredientes.keys()))
        self.jgdIngredientes.setHorizontalHeaderLabels(['Nombre', 'Tipo', 'Medida'])
        for numero_ingrediente, ingrediente in enumerate(self.resturante.ingredientes.values()):
            self.jgdIngredientes.setItem(numero_ingrediente, 0, QTableWidgetItem(ingrediente.nombre))
            self.jgdIngredientes.setItem(numero_ingrediente, 1, QTableWidgetItem(ingrediente.tipo))
            self.jgdIngredientes.setItem(numero_ingrediente, 2, QTableWidgetItem(ingrediente.medida))

    def nombre_modificar_action(self):
        self.cmbTipoModificar.setCurrentIndex(self.cmbTipoModificar.findText(self.resturante.ingredientes[self.cmbNombreModificar.currentText()].tipo))
        self.cmbMedidaModificar.setCurrentIndex(self.cmbMedidaModificar.findText(self.resturante.ingredientes[self.cmbNombreModificar.currentText()].medida))

    def init_seccion(self, seccion):
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
            self.listar_ingredientes_action()


        secciones = {0: ingresar, 1: modificar, 2: eliminar, 3: listar}

        return secciones[seccion]

    def dialogo_informacion(self, titulo, cadena):
        QtWidgets.QMessageBox.information(self,titulo, cadena)

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



