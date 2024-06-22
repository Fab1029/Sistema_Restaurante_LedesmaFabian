from PyQt6 import QtWidgets
from functools import reduce
from PyQt6.QtCore import QDate
from PyQt6.QtWidgets import QApplication
from src.Vistas.Restaurante.Ui_Reportes import Ui_Reportes
from src.Modelos.Restaurante.Restaurante import Restaurante


class ControladorReportes(QtWidgets.QWidget, Ui_Reportes):
    def __init__(self, controlador_anterior, tipo_reporte, parent= None):
        super(ControladorReportes, self).__init__(parent)
        self.setupUi(self)

        #Centrar pantalla
        self.move(QApplication.primaryScreen().availableGeometry().center() - self.rect().center())

        self.restaurante = Restaurante.getInstance()
        self.controlador_anterior = controlador_anterior

        self.init_seccion(tipo_reporte)()
        self.init_actions(tipo_reporte)


    def init_actions(self, tipo_reporte):
        self.btnObtenerReporte.clicked.connect(lambda: self.listar_reportes(tipo_reporte)() if QDate(int(self.cmbAnoInicio.currentText()), int(self.cmbMesInicio.currentText()), 1) <= QDate(int(self.cmbAnoFin.currentText()), int(self.cmbMesfin.currentText()), 1).addMonths(1).addDays(-1) else self.dialogo_informacion('Alerta', 'Fechas inválidas'))

    def init_seccion(self, tipo_reporte):
        self.cmbMesfin.addItems([str(indice) for indice in range(1,13)])
        self.cmbMesInicio.addItems([str(indice) for indice in range(1,13)])
        self.cmbAnoFin.addItems([str(indice) for indice in range(1990,QDate.currentDate().addYears(2).year())])
        self.cmbAnoInicio.addItems([str(indice) for indice in range(1990,QDate.currentDate().addYears(2).year())])

        def seccion_dinero():
            self.jgdReportes.setColumnCount(2)
            self.jgdReportes.setHorizontalHeaderLabels(['Mes-Año', 'Dinero generado'])
        def seccion_productos():
            self.jgdReportes.setColumnCount(3)
            self.jgdReportes.setHorizontalHeaderLabels(['Mes-Año', 'Producto', 'Cantidad producto'])
        def seccion_concurrencia():
            self.jgdReportes.setColumnCount(3)
            self.jgdReportes.setHorizontalHeaderLabels(['Mes-Año', 'Día', 'Cantidad reservas'])

        seccion = {'reporte_dinero': seccion_dinero, 'reporte_productos': seccion_productos,
                   'reporte_concurrencia': seccion_concurrencia}

        return seccion[tipo_reporte]


    def reportes(self, tipo_reporte):
        def reporte_dinero():
            try:
                return reduce(lambda mes_dinero, reserva: mes_dinero | {f'{QDate.fromString(reserva.fecha, 'yyyy-MM-dd').month()}-{QDate.fromString(reserva.fecha, 'yyyy-MM-dd').year()}': mes_dinero.get(f'{QDate.fromString(reserva.fecha, 'yyyy-MM-dd').month()}-{QDate.fromString(reserva.fecha, 'yyyy-MM-dd').year()}', 0) + sum([self.restaurante.productos[producto].precio * cantidad for producto, cantidad in reserva.pedidos.items() if producto in self.restaurante.productos])} if QDate(int(self.cmbAnoInicio.currentText()), int(self.cmbMesInicio.currentText()), 1) <= QDate.fromString(reserva.fecha, 'yyyy-MM-dd') <= QDate(int(self.cmbAnoFin.currentText()), int(self.cmbMesfin.currentText()), 1).addMonths(1).addDays(-1) else None, list(self.restaurante.reservas.values()),{})
            except:
                return None

        def reporte_productos():
            try:
                _ = reduce(lambda mes_producto, reserva: mes_producto | {f"{QDate.fromString(reserva.fecha, 'yyyy-MM-dd').month()}-{QDate.fromString(reserva.fecha, 'yyyy-MM-dd').year()}": {**mes_producto.get(f"{QDate.fromString(reserva.fecha, 'yyyy-MM-dd').month()}-{QDate.fromString(reserva.fecha, 'yyyy-MM-dd').year()}", {}), **{producto: mes_producto.get(f"{QDate.fromString(reserva.fecha, 'yyyy-MM-dd').month()}-{QDate.fromString(reserva.fecha, 'yyyy-MM-dd').year()}", {}).get(producto, 0) + cantidad for producto, cantidad in reserva.pedidos.items()}}} if QDate(int(self.cmbAnoInicio.currentText()), int(self.cmbMesInicio.currentText()), 1) <= QDate.fromString(reserva.fecha, 'yyyy-MM-dd') <= QDate(int(self.cmbAnoFin.currentText()), int(self.cmbMesfin.currentText()), 1).addMonths(1).addDays(-1) else mes_producto, self.restaurante.reservas.values(), {})
                return reduce(lambda mes_producto, ano_mes: mes_producto | {ano_mes: (list(_[ano_mes].keys())[list(_[ano_mes].values()).index(max(list(_[ano_mes].values())))], max(list(_[ano_mes].values()))) }, list(_.keys()), {}) if _ else None
            except:
                return None
        def reporte_concurrencia():
            try:
                _ = reduce(lambda mes_reserva, reserva: mes_reserva | {f"{QDate.fromString(reserva.fecha, 'yyyy-MM-dd').month()}-{QDate.fromString(reserva.fecha, 'yyyy-MM-dd').year()}": {QDate.fromString(reserva.fecha, 'yyyy-MM-dd').dayOfWeek(): mes_reserva.get(f"{QDate.fromString(reserva.fecha, 'yyyy-MM-dd').month()}-{QDate.fromString(reserva.fecha, 'yyyy-MM-dd').year()}", {}).get(QDate.fromString(reserva.fecha, 'yyyy-MM-dd').dayOfWeek(), 0) + 1} if f"{QDate.fromString(reserva.fecha, 'yyyy-MM-dd').month()}-{QDate.fromString(reserva.fecha, 'yyyy-MM-dd').year()}" in mes_reserva else {QDate.fromString(reserva.fecha, 'yyyy-MM-dd').dayOfWeek(): 1}} if QDate(int(self.cmbAnoInicio.currentText()), int(self.cmbMesInicio.currentText()), 1) <= QDate.fromString(reserva.fecha, 'yyyy-MM-dd') <= QDate(int(self.cmbAnoFin.currentText()), int(self.cmbMesfin.currentText()), 1).addMonths(1).addDays(-1) else mes_reserva, self.restaurante.reservas.values(), {})
                return reduce(lambda mes_reserva, ano_mes: mes_reserva | {ano_mes: (list(_[ano_mes].keys())[list(_[ano_mes].values()).index(max(list(_[ano_mes].values())))], max(list(_[ano_mes].values())))}, list(_.keys()), {}) if _ else None
            except:
                return None

        reportes = {'reporte_dinero': reporte_dinero, 'reporte_productos': reporte_productos,
                    'reporte_concurrencia': reporte_concurrencia}

        return reportes[tipo_reporte]


    def listar_reportes(self, tipo_reporte):

        def listar_reporte_dinero():
            reporte = self.reportes(tipo_reporte)()
            if reporte:
                self.jgdReportes.setRowCount(len(reporte.keys()))
                row_count = 0
                for mes_ano, monto in reporte.items():
                    self.jgdReportes.setItem(row_count, 0, QtWidgets.QTableWidgetItem(mes_ano))
                    self.jgdReportes.setItem(row_count, 1, QtWidgets.QTableWidgetItem(str(monto)))
                    row_count += 1

        def listar_reporte_productos():
            reporte = self.reportes(tipo_reporte)()
            if reporte:
                self.jgdReportes.setRowCount(len(reporte.keys()))
                row_count = 0
                for mes_ano, producto_cantidad in reporte.items():
                    self.jgdReportes.setItem(row_count, 0, QtWidgets.QTableWidgetItem(mes_ano))
                    self.jgdReportes.setItem(row_count, 1, QtWidgets.QTableWidgetItem(producto_cantidad[0]))
                    self.jgdReportes.setItem(row_count, 2, QtWidgets.QTableWidgetItem(str(producto_cantidad[1])))
                    row_count += 1

        def listar_reporte_concurrencia():
            reporte = self.reportes(tipo_reporte)()
            if reporte:
                self.jgdReportes.setRowCount(len(reporte.keys()))
                row_count = 0
                for mes_ano, reserva_cantidad in reporte.items():
                    self.jgdReportes.setItem(row_count, 0, QtWidgets.QTableWidgetItem(mes_ano))
                    self.jgdReportes.setItem(row_count, 1, QtWidgets.QTableWidgetItem(self.pesos_dias(reserva_cantidad[0])))
                    self.jgdReportes.setItem(row_count, 2, QtWidgets.QTableWidgetItem(str(reserva_cantidad[1])))
                    row_count += 1


        listar_reportes = {'reporte_dinero': listar_reporte_dinero, 'reporte_productos': listar_reporte_productos,
                           'reporte_concurrencia': listar_reporte_concurrencia}

        return listar_reportes[tipo_reporte]


    def pesos_dias(self, peso):
        pesos = {1: 'Lunes', 2: 'Martes', 3: 'Miércoles', 4:'Jueves', 5: 'Viernes', 6: 'Sábado', 7: 'Domingo'}
        return pesos[peso]
    def dialogo_informacion(self, titulo, cadena):
        QtWidgets.QMessageBox.information(self,titulo, cadena)

    def closeEvent(self, event):
        self.controlador_anterior()
