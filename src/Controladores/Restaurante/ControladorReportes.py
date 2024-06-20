from PyQt6 import QtWidgets
from functools import reduce
from PyQt6.QtCore import QDate
from src.Vistas.Restaurante.Ui_Reportes import Ui_Reportes
from src.Modelos.Restaurante.Restaurante import Restaurante


class ControladorReportes(QtWidgets.QWidget, Ui_Reportes):
    def __init__(self, controlador_anterior, tipo_reporte, parent= None):
        super(ControladorReportes, self).__init__(parent)
        self.setupUi(self)

        self.restaurante = Restaurante.getInstance()
        self.controlador_anterior = controlador_anterior

        self.init_seccion(tipo_reporte)()
        self.init_actions(tipo_reporte)


    def init_actions(self, tipo_reporte):
        self.btnObtenerReporte.clicked.connect(lambda: self.listar_reportes(tipo_reporte)())

    def init_seccion(self, tipo_reporte):
        self.cmbMesfin.addItems([str(indice) for indice in range(1,13)])
        self.cmbMesInicio.addItems([str(indice) for indice in range(1,13)])
        self.cmbAnoFin.addItems([str(indice) for indice in range(1990,QDate.currentDate().addYears(2).year())])
        self.cmbAnoInicio.addItems([str(indice) for indice in range(1990,QDate.currentDate().addYears(2).year())])

        def seccion_dinero():
            self.jgdReportes.setColumnCount(2)
            self.jgdReportes.setHorizontalHeaderLabels(['Mes-Año', 'Dinero generado'])
        def seccion_productos():
            pass
        def seccion_concurrencia():
            pass

        seccion = {'reporte_dinero': seccion_dinero, 'reporte_productos': seccion_productos,
                   'reporte_concurrencia': seccion_concurrencia}

        return seccion[tipo_reporte]


    def reportes(self, tipo_reporte):
        def reporte_dinero():
            return reduce(lambda mes_dinero, reserva: mes_dinero | {f'{QDate.fromString(reserva.fecha, 'yyyy-MM-dd').month()}-{QDate.fromString(reserva.fecha, 'yyyy-MM-dd').year()}': mes_dinero.get(f'{QDate.fromString(reserva.fecha, 'yyyy-MM-dd').month()}-{QDate.fromString(reserva.fecha, 'yyyy-MM-dd').year()}', 0) + sum([self.restaurante.productos[producto].precio * cantidad for producto, cantidad in reserva.pedidos.items() if producto in self.restaurante.productos])}
                   if QDate(int(self.cmbAnoInicio.currentText()), int(self.cmbMesInicio.currentText()), 1) <= QDate.fromString(reserva.fecha, 'yyyy-MM-dd') <= QDate(int(self.cmbAnoFin.currentText()), int(self.cmbMesfin.currentText()), 1).addMonths(1).addDays(-1) else None,
                   list(self.restaurante.reservas.values()),{})

        reportes = {'reporte_dinero': reporte_dinero}

        return reportes[tipo_reporte]


    def listar_reportes(self, tipo_reporte):

        def listar_reporte_dinero():
            reporte = self.reportes(tipo_reporte)()
            self.jgdReportes.setRowCount(len(reporte.keys()))
            row_count = 0
            for mes_ano, monto in reporte.items():
                self.jgdReportes.setItem(row_count, 0, QtWidgets.QTableWidgetItem(mes_ano))
                self.jgdReportes.setItem(row_count, 1, QtWidgets.QTableWidgetItem(str(monto)))
                row_count += 1

        listar_reportes = {'reporte_dinero': listar_reporte_dinero}

        return listar_reportes[tipo_reporte]

    def closeEvent(self, event):
        self.controlador_anterior()
