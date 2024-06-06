from PyQt6 import QtWidgets
from src.Modelos.Comida.Producto import Producto
from src.Vistas.Comida.Ui_Producto import Ui_Producto
from src.Modelos.Restaurante.Restaurante import Restaurante

class ControladorProducto(QtWidgets.QWidget, Ui_Producto):
    def __init__(self, controlador_anterior, seccion, parent= None):
        super(ControladorProducto, self).__init__(parent)
        self.setupUi(self)

        self.ingredientes = []
        self.resturante = Restaurante.getInstance()
        self.controlador_anterior = controlador_anterior

        self.verificar_pestana()

        self.__init__action()
        self.__init__seccion(seccion)()


    def __init__action(self):
        self.btnGuardarCambios.clicked.connect(self.modificar_producto_action)
        self.btnIngresarProducto.clicked.connect(self.ingresar_producto_action)
        self.btnEliminarProducto.clicked.connect(self.eliminar_producto_action)
        self.btnEliminarIngrediente.clicked.connect(self.eliminar_ingrediente_action)
        self.btnAgregarIngredienteIngresar.clicked.connect(lambda: self.agregar_ingrediente_action(1)())
        self.btnAgregarIngredienteModificar.clicked.connect(lambda: self.agregar_ingrediente_action(2)())
        self.tbProducto.currentChanged.connect(lambda: self.__init__seccion(self.tbProducto.currentIndex())())


    def nombre_modificar_action(self):
        self.cmbIngredienteModificar.clear()

        self.dsbPrecioModificar.setValue(self.resturante.productos[self.cmbNombreModificar.currentText()].precio)
        self.txtDescripcionModificar.setText(self.resturante.productos[self.cmbNombreModificar.currentText()].descripcion)
        self.cmbIngredienteModificar.addItems(list(self.resturante.productos[self.cmbNombreModificar.currentText()].ingredientes))

    def eliminar_ingrediente_action(self):
        self.resturante.productos[self.cmbNombreModificar.currentText()].ingredientes.discard(self.cmbIngredienteModificar.currentText())

        self.cmbIngredienteModificar.clear()
        self.cmbIngredienteModificar.addItems(list(self.resturante.productos[self.cmbNombreModificar.currentText()].ingredientes))


    def agregar_ingrediente_action(self, accion):
        def agregar_ingrediente_ingresar():
            self.ingredientes.append(self.cmbIngredienteIngresar.currentText())
        def agregar_ingrediente_modificar():
            self.resturante.productos[self.cmbNombreModificar.currentText()].ingredientes.add(self.cmbAgregarIngredienteModificar.currentText())
            self.cmbIngredienteModificar.clear()
            self.cmbIngredienteModificar.addItems(list(self.resturante.productos[self.cmbNombreModificar.currentText()].ingredientes))

        agregar_ingrediente = {1: agregar_ingrediente_ingresar, 2: agregar_ingrediente_modificar}

        return agregar_ingrediente[accion]


    def eliminar_producto_action(self):
        self.resturante.productos.pop(self.cmbNombreEliminar.currentText(), None)
        self.__init__seccion(2)()
        self.verificar_pestana()

    def ingresar_producto_action(self):
        self.resturante.productos.update({self.txtNombreIngresar.text(): Producto(self.txtNombreIngresar.text(), self.txtDescripcionIngresar.text(), self.dsbPrecioIngresar.value(), set(self.ingredientes))}) if self.txtNombreIngresar.text() and self.txtDescripcionIngresar.text() and self.ingredientes else print('Faltan campos')
        self.__init__seccion(0)()
        self.verificar_pestana()
    def modificar_producto_action(self):
        self.resturante.productos.update({self.cmbNombreModificar.currentText(): Producto(self.cmbNombreModificar.currentText(), self.txtDescripcionModificar.text(), self.dsbPrecioModificar.value(), self.resturante.productos[self.cmbNombreModificar.currentText()].ingredientes)}) if self.txtDescripcionModificar.text() and self.resturante.productos[self.cmbNombreModificar.currentText()].ingredientes else print('Faltan campos')
        self.__init__seccion(3)
    def listar_productos_action(self):
        pass

    def __init__seccion(self, seccion):
        self.desconectar_conexion()

        def ingresar():
            self.tbProducto.setCurrentIndex(0)
            self.ingredientes.clear()
            self.txtNombreIngresar.clear()
            self.dsbPrecioIngresar.clear()
            self.cmbIngredienteIngresar.clear()
            self.txtDescripcionIngresar.clear()
            self.cmbIngredienteIngresar.addItems((self.resturante.ingredientes.keys()))

        def modificar():
            self.tbProducto.setCurrentIndex(1)
            self.cmbNombreModificar.clear()
            self.cmbAgregarIngredienteModificar.clear()
            self.cmbNombreModificar.addItems(list(self.resturante.productos.keys()))

            #Conectar conexion
            self.conectar_conexion()

            self.nombre_modificar_action()
            self.cmbAgregarIngredienteModificar.addItems(list(self.resturante.ingredientes.keys()))

        def eliminar():
            self.tbProducto.setCurrentIndex(2)
            self.cmbNombreEliminar.clear()
            self.cmbNombreEliminar.addItems(list(self.resturante.productos.keys()))

        def listar():
            self.tbProducto.setCurrentIndex(3)
            self.jgdProductos.clear()
            self.listar_productos_action()


        secciones = {0: ingresar, 1: modificar, 2: eliminar, 3: listar}

        return secciones[seccion]

    def verificar_pestana(self):
        if self.resturante.productos:
            [self.tbProducto.setTabEnabled(indice, True) for indice in range(1,4)]
        else:
            self.tbProducto.setCurrentIndex(0)
            [self.tbProducto.setTabEnabled(indice, False) for indice in range(1,4)]

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
    def closeEvent(self, event):
        self.controlador_anterior()




