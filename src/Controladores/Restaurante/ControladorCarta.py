from PyQt6 import QtWidgets
from PyQt6.QtCore import QDate
from src.Modelos.Restaurante.Carta import Carta
from src.Vistas.Restaurante.Ui_Carta import Ui_Carta
from src.Modelos.Restaurante.Restaurante import Restaurante
class ControladorCarta(QtWidgets.QWidget, Ui_Carta):
    def __init__(self, controlador_anterior, seccion, parent= None):
        super(ControladorCarta, self).__init__(parent)
        self.setupUi(self)

        self.productos = []
        self.restaurante = Restaurante.getInstance()
        self.controlador_anterior = controlador_anterior

        self.verificar_pestana()
        self.init_seccion(seccion)()
        self.init_action()

    def init_action(self):
        self.btnIngresarCarta.clicked.connect(self.ingresar_carta_action)
        self.btnAgregarProductoIngresar.clicked.connect(lambda: self.agregar_producto_action(1)())
        self.btnEliminarProductoIngresar.clicked.connect(lambda: self.eliminar_producto_action(1)())

        self.btnGuardarCambios.clicked.connect(self.modificar_carta_action)
        self.btnAgregarProductoModificar.clicked.connect(lambda: self.agregar_producto_action(2)())
        self.btnEliminarProductoModificar.clicked.connect(lambda: self.eliminar_producto_action(2)())

        self.btnEliminarCarta.clicked.connect(self.eliminar_carta_action)
        self.tbCarta.currentChanged.connect(lambda: self.init_seccion(self.tbCarta.currentIndex())())


    def eliminar_producto_action(self, accion):
        def eliminar_producto_ingresar():
            if self.productos:
                self.productos.remove(self.cmbEliminarProductoIngresar.currentText())
                self.producto_action()
                self.dialogo_informacion('Exito', 'Se ha borrado producto de carta')
            else:
                self.dialogo_informacion('Alerta', 'Ingrese productos previamente')
        def eliminar_producto_modificar():
            if self.restaurante.cartas[self.cmbNombre.currentText()].productos:
                self.restaurante.cartas[self.cmbNombre.currentText()].productos.remove(self.cmbProductosEliminarModificar.currentText())
                self.nombre_modificar_action()
                self.dialogo_informacion('Exito', 'Se ha borrado producto de carta')
            else:
                self.dialogo_informacion('Alerta', 'Ingrese productos previamente')


        agregar_ingrediente = {1: eliminar_producto_ingresar, 2: eliminar_producto_modificar}

        return agregar_ingrediente[accion]


    def agregar_producto_action(self, accion):
        def agregar_producto_ingresar():
            self.productos.append(self.cmbProductosIngresar.currentText())
            self.producto_action()
            self.dialogo_informacion('Exito', 'Se ha agregado el producto exitosamente')

        def agregar_producto_modificar():
            self.restaurante.cartas[self.cmbNombre.currentText()].productos.add(self.cmbProductosModificar.currentText())
            self.nombre_modificar_action()
            self.dialogo_informacion('Exito', 'Se ha agregado el producto exitosamente')

        agregar_ingrediente = {1: agregar_producto_ingresar, 2: agregar_producto_modificar}

        return agregar_ingrediente[accion]


    def eliminar_carta_action(self):
        self.restaurante.cartas.pop(self.cmbNombre.currentText(), None)
        self.dialogo_informacion('Exito', 'Se ha eliminado la carta')
        self.init_seccion(2)()
        self.verificar_pestana()

    def ingresar_carta_action(self):

        if self.dtpFechaValidezIngresar.selectedDate() >= QDate.currentDate() and self.txtNombreIngresar.text() and self.productos:
            self.restaurante.cartas.update({self.txtNombreIngresar.text(): Carta(self.txtNombreIngresar.text(), self.dtpFechaValidezIngresar.selectedDate().toString('yyyy-MM-dd'), set(self.productos))})
            self.init_seccion(0)()
            self.verificar_pestana()
            self.dialogo_informacion('Exito', 'Se ha agregado carta')
        else:
            self.dialogo_informacion('Alerta', 'Llene todo los campos antes de ingresar')

    def modificar_carta_action(self):
        if self.dtpFechaValidezModificar.selectedDate() >= QDate.currentDate() and self.restaurante.cartas[self.cmbNombre.currentText()].productos:
            self.restaurante.cartas.update({self.cmbNombre.currentText(): Carta(self.cmbNombre.currentText(), self.dtpFechaValidezModificar.selectedDate().toString('yyyy-MM-dd'), self.restaurante.cartas[self.cmbNombre.currentText()].productos)})
            self.init_seccion(3)
            self.dialogo_informacion('Exito', 'Se ha modificado la carta')
        else:
            self.dialogo_informacion('Alerta', 'Llene todo los campos antes de modificar')
    def listar_cartas_action(self):
        self.jgdCartas.clear()
        self.jgdCartas.setColumnCount(2)
        self.jgdCartas.setRowCount(len(self.restaurante.cartas.keys()))
        self.jgdCartas.setHorizontalHeaderLabels(['Numero carta', 'Fecha validez'])
        for numero_carta, carta in enumerate(self.restaurante.cartas.values()):
            self.jgdCartas.setItem(numero_carta, 0, QtWidgets.QTableWidgetItem(carta.nombre))
            self.jgdCartas.setItem(numero_carta, 1, QtWidgets.QTableWidgetItem(carta.fecha_validez))

    def init_seccion(self, seccion):
        self.desconectar_conexion()
        def ingresar():
            self.tbCarta.setCurrentIndex(0)
            self.productos.clear()
            self.txtNombreIngresar.clear()
            self.cmbProductosIngresar.clear()
            self.cmbEliminarProductoIngresar.clear()
            self.dtpFechaValidezIngresar.setMinimumDate(QDate.currentDate())
            self.cmbProductosIngresar.addItems(list(self.restaurante.productos.keys()))
        def modificar():
            self.tbCarta.setCurrentIndex(1)
            self.cmbNombre.clear()
            self.cmbProductosModificar.clear()
            self.cmbProductosEliminarModificar.clear()
            self.cmbNombre.addItems(list(self.restaurante.cartas.keys()))
            self.cmbProductosModificar.addItems(list(self.restaurante.productos.keys()))

            #Conectar conexion
            self.conectar_conexion()
            print('entro')
            self.nombre_modificar_action()
            print('salio')

        def eliminar():
            self.tbCarta.setCurrentIndex(2)
            self.cmbNombreEliminar.clear()

            self.cmbNombreEliminar.addItems(list(self.restaurante.cartas.keys()))

        def listar():
            self.tbCarta.setCurrentIndex(3)
            self.listar_cartas_action()

        secciones = {0: ingresar, 1: modificar, 2: eliminar, 3: listar}

        return secciones[seccion]

    def dialogo_informacion(self, titulo, cadena):
        QtWidgets.QMessageBox.information(self,titulo, cadena)

    def producto_action(self):
        self.cmbEliminarProductoIngresar.clear()
        self.cmbEliminarProductoIngresar.addItems(self.productos)

    def nombre_modificar_action(self):
        self.cmbProductosEliminarModificar.clear()
        self.cmbProductosEliminarModificar.addItems(list(self.restaurante.cartas[self.cmbNombre.currentText()].productos))
        self.dtpFechaValidezModificar.setSelectedDate(QDate.fromString(self.restaurante.cartas[self.cmbNombre.currentText()].fecha_validez, 'yyyy-MM-dd'))


    def verificar_pestana(self):
        if self.restaurante.cartas:
            [self.tbCarta.setTabEnabled(indice, True) for indice in range(1,4)]
        else:
            self.tbCarta.setCurrentIndex(0)
            [self.tbCarta.setTabEnabled(indice, False) for indice in range(1,4)]

    def desconectar_conexion(self):
        try:
            self.cmbNombre.disconnect()
        except:
            pass
    def conectar_conexion(self):
        try:
            self.cmbNombre.currentIndexChanged.connect(self.nombre_modificar_action)
        except:
            pass
    def closeEvent(self, event):
        self.controlador_anterior()

