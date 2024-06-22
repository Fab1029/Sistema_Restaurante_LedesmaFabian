import random
import string
from PyQt6 import QtWidgets
from PyQt6.QtCore import QDate
from PyQt6.QtWidgets import QApplication
from src.Modelos.Restaurante.Reserva import Reserva
from src.Vistas.Restaurante.Ui_Reserva import Ui_Reserva
from src.Modelos.Restaurante.Restaurante import Restaurante
class ControladorReserva(QtWidgets.QWidget, Ui_Reserva):
    def __init__(self, controlador_anterior, seccion, parent = None):
        super(ControladorReserva, self).__init__(parent)
        self.setupUi(self)

        #Centrar pantalla
        self.move(QApplication.primaryScreen().availableGeometry().center() - self.rect().center())

        self.pedido = dict()
        self.restaurante = Restaurante.getInstance()
        self.codigo_reserva = self.generar_codigo()
        self.controlador_anterior = controlador_anterior

        self.verificar_pestana()
        self.init_seccion(seccion)()
        self.init_action()


    def init_action(self):
        self.btnReservar.clicked.connect(self.ingresar_reserva_action)
        self.btnGuardarCambios.clicked.connect(self.modificar_reserva_action)
        self.btnEliminarPedidoIngresar.clicked.connect(lambda: self.pedido_action(2)())
        self.btnEliminarPedidoModificar.clicked.connect(lambda: self.pedido_action(4)())
        self.btnGuardarCambiosPedidoIngresar.clicked.connect(lambda: self.pedido_action(1)())
        self.btnGuardarCambiosPedidoModificar.clicked.connect(lambda: self.pedido_action(3)())
        self.tbReserva.currentChanged.connect(lambda: self.init_seccion(self.tbReserva.currentIndex())())
        self.btnAgregarProductoIngresar.clicked.connect(lambda: self.agregar_producto_a_pedido_action(1)())
        self.btnAgregarProductoModificar.clicked.connect(lambda: self.agregar_producto_a_pedido_action(2)())

        self.btnEliminarReserva.clicked.connect(lambda: self.eliminar_reserva_action())


    def agregar_producto_a_pedido_action(self, accion):
        def ingresar():
            #Ya esta revisada esta funcionalidad
            if self.cmbAgregarProductosIngresar.currentText():
                self.pedido.update({self.cmbAgregarProductosIngresar.currentText(): self.sbCantidadProductoIngresar.value()})
                self.cmbPedidoIngresar.clear()
                self.sbCantidadProductoIngresar.setValue(0)
                self.cmbPedidoIngresar.addItems(list(self.pedido.keys()))
                self.sbCantidadPedidoIngresar.setValue(self.pedido[self.cmbPedidoIngresar.currentText()])
                self.dialogo_informacion('Exito', 'Se agrego producto a pedido')
            else:
                self.dialogo_informacion('Alerta', 'No se agrego producto a pedido')
        #Acabado pero revisar
        def modificar():
            if self.cmbAgregarProductoModificar.currentText():
                self.pedido.update({self.cmbAgregarProductoModificar.currentText(): self.sbCantidadProductoModificar.value()})
                self.cmbPedidoModificar.blockSignals(True)
                self.cmbPedidoModificar.clear()
                self.sbCantidadProductoModificar.setValue(0)
                self.cmbPedidoModificar.addItems(list(self.pedido.keys()))
                self.sbCantidadPedidoModificar.setValue(self.pedido[self.cmbPedidoModificar.currentText()])
                self.dialogo_informacion('Exito', 'Se agrego producto a pedido')
                self.cmbPedidoModificar.blockSignals(False)
            else:
                self.dialogo_informacion('Alerta', 'No se agrego producto a pedido')


        producto_a_pedido = {1: ingresar, 2: modificar}

        return producto_a_pedido[accion]

    def pedido_action(self, accion):
        #Ya se corregio esta funcionalidad
        def guardar_cambios_pedido_ingresar():
            if self.cmbPedidoIngresar.currentText():
                self.pedido.update({self.cmbPedidoIngresar.currentText() : self.sbCantidadPedidoIngresar.value()})
                self.cmbPedidoIngresar.blockSignals(True)
                self.cmbPedidoIngresar.clear()
                self.cmbPedidoIngresar.addItems(list(self.pedido.keys()))
                self.sbCantidadPedidoIngresar.setValue(self.pedido[self.cmbPedidoIngresar.currentText()])
                self.dialogo_informacion('Exito', 'Cambio guardado')
                self.cmbPedidoIngresar.blockSignals(False)
            else:
                self.dialogo_informacion('Alerta', 'No se ha podido realizar el cambio')

        #Ya se verifico esta funcionalidad
        def eliminar_pedido_ingresar():
            if self.cmbPedidoIngresar.currentText():
                self.pedido.pop(self.cmbPedidoIngresar.currentText())
                self.cmbPedidoIngresar.blockSignals(True)
                self.cmbPedidoIngresar.clear()
                self.cmbPedidoIngresar.addItems(list(self.pedido.keys()))
                self.sbCantidadPedidoIngresar.setValue(self.pedido[self.cmbPedidoIngresar.currentText()] if self.pedido else 0)
                self.dialogo_informacion('Exito', 'Producto eliminado')
                self.cmbPedidoIngresar.blockSignals(False)
            else:
                self.dialogo_informacion('Alerta', 'No se ha eliminado producto')
        #VERIFICAR FUNCIONALIDAD
        def guardar_cambios_modificar():
            if self.cmbPedidoModificar.currentText():
                self.pedido.update({self.cmbPedidoModificar.currentText(): self.sbCantidadPedidoModificar.value()})
                self.cmbPedidoModificar.blockSignals(True)
                self.cmbPedidoModificar.clear()
                self.cmbPedidoModificar.addItems(list(self.pedido.keys()))
                self.sbCantidadPedidoModificar.setValue(self.pedido[self.cmbPedidoModificar.currentText()])
                self.dialogo_informacion('Exito', 'Cambio guardado')
                self.cmbPedidoModificar.blockSignals(False)
            else:
                self.dialogo_informacion('Alerta', 'No se ha podido realizar el cambio')
        #VERIFICAR FUNCIONALIDAD
        def eliminar_pedido_modificar():
            if self.cmbPedidoModificar.currentText():
                self.pedido.pop(self.cmbPedidoModificar.currentText())
                self.cmbPedidoModificar.blockSignals(True)
                self.cmbPedidoModificar.clear()
                self.cmbPedidoModificar.addItems(list(self.pedido.keys()))
                self.sbCantidadPedidoModificar.setValue(self.pedido[self.cmbPedidoModificar.currentText()] if self.pedido else 0)
                self.dialogo_informacion('Exito', 'Producto eliminado')
                self.cmbPedidoModificar.blockSignals(False)
            else:
                self.dialogo_informacion('Alerta', 'No se ha eliminado producto')

        pedido = {1: guardar_cambios_pedido_ingresar, 2: eliminar_pedido_ingresar, 3: guardar_cambios_modificar, 4: eliminar_pedido_modificar}

        return pedido[accion]

    def cambio_fecha_action(self, accion):
        #Ya se verifico esta funcionalidad
        def cambio_fecha_ingresar():
            self.pedido.clear()
            self.cmbPedidoIngresar.blockSignals(True)
            self.cmbAgregarProductosIngresar.blockSignals(True)
            self.cmbTurnoIngresar.clear()
            self.cmbPedidoIngresar.clear()
            self.cmbAgregarProductosIngresar.clear()
            self.sbCantidadPedidoIngresar.setValue(0)
            self.sbNumeroComensalesIngresar.setValue(0)
            self.sbCantidadProductoIngresar.setValue(0)
            self.cmbTurnoIngresar.addItems(list(filter(lambda disponibilidad: self.restaurante.dias_disponibilidad[self.dtpFechaIngresar.selectedDate().toString('yyyy-MM-dd')][disponibilidad].turno if self.restaurante.dias_disponibilidad[self.dtpFechaIngresar.selectedDate().toString('yyyy-MM-dd')][disponibilidad].numero_plazas > 0 else None, self.restaurante.dias_disponibilidad[self.dtpFechaIngresar.selectedDate().toString('yyyy-MM-dd')].keys()))
                                           if self.restaurante.dias_disponibilidad.get(self.dtpFechaIngresar.selectedDate().toString('yyyy-MM-dd'), None) is not None and self.restaurante.dias_disponibilidad[self.dtpFechaIngresar.selectedDate().toString('yyyy-MM-dd')] else [])
            self.cmbAgregarProductosIngresar.addItems(list(self.obtener_carta_actual().productos) if self.obtener_carta_actual() is not None else [])
            self.cmbPedidoIngresar.blockSignals(False)
            self.cmbAgregarProductosIngresar.blockSignals(False)


        def cambio_fecha_modificar():
            self.pedido.clear()
            self.cmbPedidoModificar.blockSignals(True)
            self.cmbAgregarProductoModificar.blockSignals(True)
            self.cmbTurnoModificar.clear()
            self.cmbPedidoModificar.clear()
            self.cmbAgregarProductoModificar.clear()
            self.sbCantidadPedidoModificar.setValue(0)
            self.sbCantidadProductoModificar.setValue(0)
            self.cmbTurnoModificar.addItems(list(filter(lambda disponibilidad: self.restaurante.dias_disponibilidad[self.dtpFechaModificar.selectedDate().toString('yyyy-MM-dd')][disponibilidad].turno if self.restaurante.dias_disponibilidad[self.dtpFechaModificar.selectedDate().toString('yyyy-MM-dd')][disponibilidad].numero_plazas > 0 else None, self.restaurante.dias_disponibilidad[self.dtpFechaModificar.selectedDate().toString('yyyy-MM-dd')].keys()))
                                            if self.restaurante.dias_disponibilidad.get(self.dtpFechaModificar.selectedDate().toString('yyyy-MM-dd'), None) is not None and self.restaurante.dias_disponibilidad[self.dtpFechaModificar.selectedDate().toString('yyyy-MM-dd')] else [])
            self.cmbAgregarProductoModificar.addItems(list(self.obtener_carta_actual().productos) if self.obtener_carta_actual() is not None else [])
            self.cmbPedidoModificar.blockSignals(False)
            self.cmbAgregarProductoModificar.blockSignals(False)

        cambio_fecha = {1: cambio_fecha_ingresar, 2: cambio_fecha_modificar}

        return cambio_fecha[accion]

    def eliminar_reserva_action(self):
        if self.restaurante.reservas.pop(self.cmbNumeroReservaEliminar.currentText(), None) is not None:
            self.init_seccion(2)()
            self.verificar_pestana()
            self.dialogo_informacion('Exito', 'Se ha eliminado reserva')
        else:
            self.dialogo_informacion('Alerta', 'No se ha podido eliminar reserva')


    def ingresar_reserva_action(self):
        #Ya se verifico esta funcionalidad
        if self.dtpFechaIngresar.selectedDate() >= QDate.currentDate() and self.cmbTurnoIngresar.currentText() and self.pedido:
            self.restaurante.reservas.update({self.txtNumeroReservaIngresar.text(): Reserva(self.dtpFechaIngresar.selectedDate().toString('yyyy-MM-dd'), self.cmbTurnoIngresar.currentText(), self.txtNumeroReservaIngresar.text(), self.sbNumeroComensalesIngresar.value(), dict(self.pedido))})
            self.restaurante.dias_disponibilidad[self.dtpFechaIngresar.selectedDate().toString('yyyy-MM-dd')][self.cmbTurnoIngresar.currentText()].numero_plazas -= 1
            self.codigo_reserva = self.generar_codigo()
            self.init_seccion(0)()
            self.verificar_pestana()
            self.dialogo_informacion('Exito', 'Ingreso correcto')

        else:
            self.dialogo_informacion('Alerta', 'No se pudo realizar la reserva')

    def modificar_reserva_action(self):
        if self.dtpFechaModificar.selectedDate() >= QDate.currentDate() and self.cmbTurnoModificar.currentText() and self.restaurante.reservas[self.cmbNumeroReservaModificar.currentText()].pedidos:
            self.restaurante.reservas.update({self.cmbNumeroReservaModificar.currentText(): Reserva(self.dtpFechaModificar.selectedDate().toString('yyyy-MM-dd'), self.cmbTurnoModificar.currentText(), self.cmbNumeroReservaModificar.currentText(), self.sbNumeroComensalesModificar.value(), dict(self.pedido))})
            self.init_seccion(1)()
            self.verificar_pestana()
            self.dialogo_informacion('Exito', 'Cambios guardados')
        else:
            self.dialogo_informacion('Alerta', 'No se realizaron los cambios')

    def listar_reserva_action(self):
        self.jgdReservas.clear()
        self.jgdReservas.setColumnCount(4)
        self.jgdReservas.setRowCount(len(self.restaurante.reservas.keys()))
        self.jgdReservas.setHorizontalHeaderLabels(['Numero reserva', 'Fecha', 'Turno', 'Numero comensales'])
        for numero_reserva, reserva in enumerate(self.restaurante.reservas.values()):
            self.jgdReservas.setItem(numero_reserva, 0, QtWidgets.QTableWidgetItem(reserva.numero_reserva))
            self.jgdReservas.setItem(numero_reserva, 1, QtWidgets.QTableWidgetItem(reserva.fecha))
            self.jgdReservas.setItem(numero_reserva, 2, QtWidgets.QTableWidgetItem(reserva.turno))
            self.jgdReservas.setItem(numero_reserva, 3, QtWidgets.QTableWidgetItem(str(reserva.numero_comensales)))

    def obtener_carta_actual(self):
        cartas_validas = sorted(list(filter(lambda carta: QDate.fromString(carta.fecha_validez, 'yyyy-MM-dd') >= QDate.currentDate(), self.restaurante.cartas.values())), key=lambda carta: QDate.fromString(carta.fecha_validez, 'yyyy-MM-dd'), reverse=True)
        return cartas_validas[0] if cartas_validas else None


    def init_seccion(self, seccion):
        self.desconectar_conexion()
        def ingresar():
            self.tbReserva.setCurrentIndex(0)
            self.txtNumeroReservaIngresar.setText(self.codigo_reserva)
            self.dtpFechaIngresar.setMinimumDate(QDate.currentDate())
            #Conectar conexion
            self.cambio_fecha_action(1)()
            self.conectar_conexion(1)()

        def modificar():
            self.tbReserva.setCurrentIndex(1)
            self.cmbNumeroReservaModificar.blockSignals(True)
            self.cmbNumeroReservaModificar.clear()
            self.dtpFechaModificar.setMinimumDate(QDate.currentDate())
            self.cmbNumeroReservaModificar.addItems(list(filter(lambda reserva: reserva if QDate.fromString(self.restaurante.reservas[reserva].fecha, 'yyyy-MM-dd') >= QDate.currentDate() else None, self.restaurante.reservas.keys())))
            self.cmbNumeroReservaModificar.blockSignals(False)

            #Conectar conexion
            self.conectar_conexion(2)()
            self.numero_reserva_action(1)()

        def eliminar():
            self.tbReserva.setCurrentIndex(2)
            self.numero_reserva_action(2)()

        def listar():
            self.tbReserva.setCurrentIndex(3)
            self.listar_reserva_action()

        secciones = {0: ingresar, 1: modificar, 2: eliminar, 3: listar}

        return secciones[seccion]

    def dialogo_informacion(self, titulo, cadena):
        QtWidgets.QMessageBox.information(self,titulo, cadena)

    def verificar_pestana(self):
        if self.restaurante.reservas:
            [self.tbReserva.setTabEnabled(indice, True) for indice in range(1,4)]
            if list(filter(lambda reserva: reserva if QDate.fromString(self.restaurante.reservas[reserva].fecha, 'yyyy-MM-dd') >= QDate.currentDate() else None, self.restaurante.reservas.keys())):
                self.tbReserva.setTabEnabled(1, True)
            else:
                self.tbReserva.setTabEnabled(1, False)
        else:
            self.tbReserva.setCurrentIndex(0)
            [self.tbReserva.setTabEnabled(indice, False) for indice in range(1,4)]

    def numero_reserva_action(self, accion):
        def modificar():
            self.cmbPedidoModificar.blockSignals(True)
            self.cmbAgregarProductoModificar.blockSignals(True)
            self.dtpFechaModificar.blockSignals(True)

            self.cmbTurnoModificar.clear()
            self.cmbPedidoModificar.clear()
            self.cmbAgregarProductoModificar.clear()
            self.sbCantidadProductoModificar.setValue(0)
            self.pedido = dict(self.restaurante.reservas[self.cmbNumeroReservaModificar.currentText()].pedidos)

            self.cmbPedidoModificar.addItems(list(self.pedido.keys()))
            self.sbNumeroComensalesModificar.setValue(self.restaurante.reservas[self.cmbNumeroReservaModificar.currentText()].numero_comensales)
            self.dtpFechaModificar.setSelectedDate(QDate.fromString(self.restaurante.reservas[self.cmbNumeroReservaModificar.currentText()].fecha, 'yyyy-MM-dd'))
            self.sbCantidadPedidoModificar.setValue(self.pedido[self.cmbPedidoModificar.currentText()])
            self.cmbTurnoModificar.addItems(list(filter(lambda disponibilidad: self.restaurante.dias_disponibilidad[self.dtpFechaModificar.selectedDate().toString('yyyy-MM-dd')][disponibilidad].turno if self.restaurante.dias_disponibilidad[self.dtpFechaModificar.selectedDate().toString('yyyy-MM-dd')][disponibilidad].numero_plazas > 0 else None, self.restaurante.dias_disponibilidad[self.dtpFechaModificar.selectedDate().toString('yyyy-MM-dd')].keys()))
                                            if self.restaurante.dias_disponibilidad.get(self.dtpFechaModificar.selectedDate().toString('yyyy-MM-dd'), None) is not None and self.restaurante.dias_disponibilidad[self.dtpFechaModificar.selectedDate().toString('yyyy-MM-dd')] else [])
            self.cmbTurnoModificar.setCurrentIndex(self.cmbTurnoModificar.findText(self.restaurante.reservas[self.cmbNumeroReservaModificar.currentText()].turno))
            self.cmbAgregarProductoModificar.addItems(list(self.obtener_carta_actual().productos) if self.obtener_carta_actual() is not None else [])

            self.cmbPedidoModificar.blockSignals(False)
            self.cmbAgregarProductoModificar.blockSignals(False)
            self.dtpFechaModificar.blockSignals(False)
        def eliminar():
            self.cmbNumeroReservaEliminar.clear()
            self.cmbNumeroReservaEliminar.addItems(list(self.restaurante.reservas.keys()))

        numero_reserva = {1: modificar, 2: eliminar}

        return numero_reserva[accion]


    def generar_codigo(self, longitud = 8):
        return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(longitud))

    def obtener_codigo_reserva(self):
        codigo = self.generar_codigo()

        while codigo in list(self.restaurante.reservas.keys()):
            codigo = self.generar_codigo()

        return codigo

    def desconectar_conexion(self):
        try:
            self.dtpFechaIngresar.disconnect()
            self.cmbPedidoIngresar.disconnect()

            self.cmbPedidoModificar.disconnect()
            self.cmbNumeroReservaModificar.disconnect()
            self.cmbAgregarProductoModificar.disconnect()
            self.cmbAgregarProductosIngresar.disconnect()

            self.dtpFechaModificar.disconnect()
        except:
            pass

    def conectar_conexion(self, accion):
        def conectar_ingreso():
            try:
                self.dtpFechaIngresar.selectionChanged.connect(lambda: self.cambio_fecha_action(1)())
                self.cmbAgregarProductosIngresar.currentIndexChanged.connect(lambda: self.sbCantidadProductoIngresar.setValue(0))
                self.cmbPedidoIngresar.currentIndexChanged.connect(lambda: self.sbCantidadPedidoIngresar.setValue(self.pedido[self.cmbPedidoIngresar.currentText()]))
            except:
                pass
        def conectar_modificar():
            try:
                self.dtpFechaModificar.selectionChanged.connect(lambda: self.cambio_fecha_action(2)())
                self.cmbNumeroReservaModificar.currentIndexChanged.connect(lambda: self.numero_reserva_action(1)())
                self.cmbAgregarProductoModificar.currentIndexChanged.connect(lambda: self.sbCantidadProductoModificar.setValue(0))
                self.cmbPedidoModificar.currentIndexChanged.connect(lambda: self.sbCantidadPedidoModificar.setValue(self.pedido[self.cmbPedidoModificar.currentText()]))
            except Exception as e:
                print(str(e))

        conectar = {1: conectar_ingreso, 2: conectar_modificar}

        return conectar[accion]

    def closeEvent(self, event):
        self.controlador_anterior()
