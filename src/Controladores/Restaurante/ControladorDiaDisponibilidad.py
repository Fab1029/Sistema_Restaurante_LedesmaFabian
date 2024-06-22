from PyQt6 import QtWidgets
from PyQt6.QtCore import QDate
from PyQt6.QtWidgets import QApplication
from src.Modelos.Restaurante.Restaurante import Restaurante
from src.Vistas.Restaurante.Ui_Disponibilidad import Ui_Disponibilidad
from src.Modelos.Restaurante.DiaDisponibilidad import DiaDisponibilidad

class ControladorDiaDisponibilidad(QtWidgets.QWidget, Ui_Disponibilidad):
    def __init__(self, controlador_anterior, seccion, parent= None):
        super(ControladorDiaDisponibilidad, self).__init__(parent)
        self.setupUi(self)

        #Centrar pantalla
        self.move(QApplication.primaryScreen().availableGeometry().center() - self.rect().center())

        self.restaurante = Restaurante.getInstance()
        self.controlador_anterior = controlador_anterior

        self.verificar_pestana()
        self.init_seccion(seccion)()
        self.init_action()


    def init_action(self):
        self.btnEliminar.clicked.connect(self.eliminar_dia_disponibilidad_action)
        self.btnGuardarCambios.clicked.connect(self.modificar_dia_disponibilidad_action)
        self.btnIngresarDisponibilidad.clicked.connect(self.ingresar_dia_disponibilidad_action)
        self.tbDisponibilidad.currentChanged.connect(lambda: self.init_seccion(self.tbDisponibilidad.currentIndex())())


    def cambio_fecha_action(self, accion):
        def cambio_fecha_ingresar():
            self.sbNumeroPlazas.setValue(0)
        def cambio_fecha_modificar():
            if self.dtpFechaModificar.selectedDate().toString('yyyy-MM-dd') in self.restaurante.dias_disponibilidad and self.restaurante.dias_disponibilidad[self.dtpFechaModificar.selectedDate().toString('yyyy-MM-dd')].get(self.cmbTurnoModificar.currentText(), None) is not None:
                self.sbNumeroPlazasModificar.setValue(self.restaurante.dias_disponibilidad[self.dtpFechaModificar.selectedDate().toString('yyyy-MM-dd')][self.cmbTurnoModificar.currentText()].numero_plazas)
            else:
                self.sbNumeroPlazasModificar.setValue(0)

        def cambio_fecha_eliminar():
            if self.dtpFechaEliminar.selectedDate().toString('yyyy-MM-dd') in self.restaurante.dias_disponibilidad and self.restaurante.dias_disponibilidad[self.dtpFechaEliminar.selectedDate().toString('yyyy-MM-dd')].get(self.cmbTurnoEliminar.currentText(), None) is not None:
                self.txtNumeroPlazasEliminar.setText(str(self.restaurante.dias_disponibilidad[self.dtpFechaEliminar.selectedDate().toString('yyyy-MM-dd')][self.cmbTurnoEliminar.currentText()].numero_plazas))
            else:
                self.txtNumeroPlazasEliminar.setText('No se tiene informacion sobre este dia')

        cambio_fecha = {1: cambio_fecha_ingresar, 2: cambio_fecha_modificar, 3: cambio_fecha_eliminar}

        return cambio_fecha[accion]

    def eliminar_dia_disponibilidad_action(self):
        if self.restaurante.dias_disponibilidad[self.dtpFechaEliminar.selectedDate().toString('yyyy-MM-dd')].pop(self.cmbTurnoEliminar.currentText(), None) is not None:
            self.init_seccion(2)()
            self.verificar_pestana()
            self.dialogo_informacion('Exitoso', 'Eliminacion exitosa')
        else:
            self.dialogo_informacion('Alerta', 'No existe informacion de disponibilidad')

    def ingresar_dia_disponibilidad_action(self):
        if self.dtpFechaIngresar.selectedDate().toString('yyyy-MM-dd') not in self.restaurante.dias_disponibilidad:
            self.restaurante.dias_disponibilidad[self.dtpFechaIngresar.selectedDate().toString('yyyy-MM-dd')] = {}

        self.restaurante.dias_disponibilidad[self.dtpFechaIngresar.selectedDate().toString('yyyy-MM-dd')][self.cmbTurnoIngresar.currentText()] = DiaDisponibilidad(self.dtpFechaIngresar.selectedDate().toString('yyyy-MM-dd'), self.cmbTurnoIngresar.currentText(), self.sbNumeroPlazas.value())
        self.init_seccion(0)()
        self.verificar_pestana()
        self.dialogo_informacion('Exitoso', 'Ingreso de disponibilidad exitoso')

    def modificar_dia_disponibilidad_action(self):

        if self.restaurante.dias_disponibilidad.get(self.dtpFechaModificar.selectedDate().toString('yyyy-MM-dd'), None) is not None and self.restaurante.dias_disponibilidad[self.dtpFechaModificar.selectedDate().toString('yyyy-MM-dd')].get(self.cmbTurnoModificar.currentText(), None) is not None:
            self.restaurante.dias_disponibilidad[self.dtpFechaModificar.selectedDate().toString('yyyy-MM-dd')][self.cmbTurnoModificar.currentText()] = DiaDisponibilidad(self.dtpFechaModificar.selectedDate().toString('yyyy-MM-dd'), self.cmbTurnoModificar.currentText(), self.sbNumeroPlazasModificar.value())
            self.init_seccion(1)()
            self.verificar_pestana()
            self.dialogo_informacion('Exito', 'Se ha modficado la disponibilidad del dia')
        else:
            self.dialogo_informacion('Alerta', 'No existe informacion de disponibilidad para este dia')

    def listar_dia_disponibilidad_action(self):
        self.jgdDisponibilidad.clear()
        self.jgdDisponibilidad.setColumnCount(3)
        self.jgdDisponibilidad.setRowCount(sum([len(self.restaurante.dias_disponibilidad[fecha].values()) for fecha in self.restaurante.dias_disponibilidad.keys()]))
        self.jgdDisponibilidad.setHorizontalHeaderLabels(['Fecha', 'Turno', 'Numero plazas'])
        row_count = 0
        for fecha in self.restaurante.dias_disponibilidad.keys():
            for turno in self.restaurante.dias_disponibilidad[fecha].keys():
                self.jgdDisponibilidad.setItem(row_count, 0, QtWidgets.QTableWidgetItem(self.restaurante.dias_disponibilidad[fecha][turno].fecha))
                self.jgdDisponibilidad.setItem(row_count, 1, QtWidgets.QTableWidgetItem(self.restaurante.dias_disponibilidad[fecha][turno].turno))
                self.jgdDisponibilidad.setItem(row_count, 2, QtWidgets.QTableWidgetItem(str(self.restaurante.dias_disponibilidad[fecha][turno].numero_plazas)))
            row_count += 1


    def init_seccion(self, seccion):
        self.desconectar_conexion()
        def ingresar():
            self.tbDisponibilidad.setCurrentIndex(0)
            self.cmbTurnoIngresar.clear()
            self.sbNumeroPlazas.setValue(0)
            self.dtpFechaIngresar.setMinimumDate(QDate.currentDate())
            self.cmbTurnoIngresar.addItems(list(self.restaurante.turnos))

            #Conectar conexion
            self.conectar_conexion(1)()
            self.cambio_fecha_action(1)()

        def modificar():
            self.tbDisponibilidad.setCurrentIndex(1)
            self.cmbTurnoModificar.clear()
            self.sbNumeroPlazasModificar.setValue(0)

            self.cmbTurnoModificar.addItems(list(self.restaurante.turnos))
            self.dtpFechaModificar.setMinimumDate(QDate.currentDate())

            #Conectar conexion
            self.conectar_conexion(2)()
            self.cambio_fecha_action(2)()

        def eliminar():
            self.tbDisponibilidad.setCurrentIndex(2)
            self.cmbTurnoEliminar.clear()
            self.cmbTurnoEliminar.addItems(list(self.restaurante.turnos))

            #Conectar conexion
            self.conectar_conexion(3)()
            self.cambio_fecha_action(3)()

        def listar():
            self.tbDisponibilidad.setCurrentIndex(3)
            self.listar_dia_disponibilidad_action()

        secciones = {0: ingresar, 1: modificar, 2: eliminar, 3: listar}

        return secciones[seccion]

    def dialogo_informacion(self, titulo, cadena):
        QtWidgets.QMessageBox.information(self,titulo, cadena)

    def verificar_pestana(self):
        if self.restaurante.dias_disponibilidad:
            [self.tbDisponibilidad.setTabEnabled(indice, True) for indice in range(1,4)]
        else:
            self.tbDisponibilidad.setCurrentIndex(0)
            [self.tbDisponibilidad.setTabEnabled(indice, False) for indice in range(1,4)]

    def desconectar_conexion(self):
        try:
            self.dtpFechaIngresar.disconnect()
            self.dtpFechaEliminar.disconnect()
            self.dtpFechaModificar.disconnect()
        except:
            pass

    def conectar_conexion(self, accion):
        def conectar_ingreso():
            try:
                self.dtpFechaIngresar.selectionChanged.connect(lambda: self.cambio_fecha_action(1)())
            except:
                pass
        def conectar_modificar():
            try:
                self.dtpFechaModificar.selectionChanged.connect(lambda: self.cambio_fecha_action(2)())
            except:
                pass
        def conectar_eliminar():
            try:
                self.dtpFechaEliminar.selectionChanged.connect(lambda: self.cambio_fecha_action(3)())
            except:
                pass

        conectar = {1: conectar_ingreso, 2: conectar_modificar, 3: conectar_eliminar}

        return conectar[accion]



    def closeEvent(self, event):
        self.controlador_anterior()
