# Form implementation generated from reading ui file 'Ui_Disponibilidad.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Ui_Disponibilidad(object):
    def setupUi(self, Ui_Disponibilidad):
        Ui_Disponibilidad.setObjectName("Ui_Disponibilidad")
        Ui_Disponibilidad.resize(1090, 741)
        Ui_Disponibilidad.setStyleSheet("QWidget{\n"
"background-color:white;\n"
"}\n"
"\n"
"QLabel{\n"
"font-family:\"Sans-serif\";\n"
"font-size:14px;\n"
"padding:5px;\n"
"\n"
"}\n"
"\n"
"QDoubleSpinBox{\n"
"font-family:\"Sans-serif\";\n"
"font-size:14px;\n"
"padding:10px 10px;\n"
"border-radius:10px;\n"
"border:2px solid rgb(228, 232, 235);\n"
"}\n"
"\n"
"QSpinBox{\n"
"font-family:\"Sans-serif\";\n"
"font-size:14px;\n"
"padding:10px 10px;\n"
"border-radius:10px;\n"
"border:2px solid rgb(228, 232, 235);\n"
"}\n"
"\n"
"\n"
"QComboBox{\n"
"font-family:\"Sans-serif\";\n"
"font-size:14px;\n"
"padding:10px 10px;\n"
"border-radius:10px;\n"
"border:2px solid rgb(228, 232, 235);\n"
"}\n"
"\n"
"QLineEdit{\n"
"font-family:\"Sans-serif\";\n"
"font-size:14px;\n"
"padding:10px 10px;\n"
"border-radius:10px;\n"
"border:2px solid rgb(228, 232, 235);\n"
"}\n"
"\n"
"QPushButton{\n"
"font-family:\"Sans-serif\";\n"
"background-color: #E4E8EB;\n"
"padding: 10px 10px;\n"
"border-radius: 10px;\n"
"\n"
"}\n"
"\n"
"\n"
"QLineEdit:hover{\n"
"border:2px solid black;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:2px solid black;\n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(Ui_Disponibilidad)
        self.gridLayout.setObjectName("gridLayout")
        self.tbDisponibilidad = QtWidgets.QTabWidget(parent=Ui_Disponibilidad)
        self.tbDisponibilidad.setObjectName("tbDisponibilidad")
        self.tbIngresar = QtWidgets.QWidget()
        self.tbIngresar.setObjectName("tbIngresar")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tbIngresar)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.cmbTurnoIngresar = QtWidgets.QComboBox(parent=self.tbIngresar)
        self.cmbTurnoIngresar.setObjectName("cmbTurnoIngresar")
        self.gridLayout_2.addWidget(self.cmbTurnoIngresar, 4, 0, 1, 1)
        self.lblFechaIngresar = QtWidgets.QLabel(parent=self.tbIngresar)
        self.lblFechaIngresar.setObjectName("lblFechaIngresar")
        self.gridLayout_2.addWidget(self.lblFechaIngresar, 5, 0, 1, 1)
        self.lblTurnoIngresar = QtWidgets.QLabel(parent=self.tbIngresar)
        self.lblTurnoIngresar.setObjectName("lblTurnoIngresar")
        self.gridLayout_2.addWidget(self.lblTurnoIngresar, 3, 0, 1, 1)
        self.btnIngresarDisponibilidad = QtWidgets.QPushButton(parent=self.tbIngresar)
        self.btnIngresarDisponibilidad.setObjectName("btnIngresarDisponibilidad")
        self.gridLayout_2.addWidget(self.btnIngresarDisponibilidad, 7, 0, 1, 1)
        self.sbNumeroPlazas = QtWidgets.QSpinBox(parent=self.tbIngresar)
        self.sbNumeroPlazas.setObjectName("sbNumeroPlazas")
        self.gridLayout_2.addWidget(self.sbNumeroPlazas, 2, 0, 1, 1)
        self.dtpFechaIngresar = QtWidgets.QCalendarWidget(parent=self.tbIngresar)
        self.dtpFechaIngresar.setStyleSheet("QCalendarWidget QToolButton {\n"
"    color: black;\n"
"    background-color: #e6e6e6;\n"
"    border: none;\n"
"    margin: 5px;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QCalendarWidget QWidget#qt_calendar_navigationbar {\n"
"    background-color: #e6e6e6;\n"
"}\n"
"\n"
"QCalendarWidget QTableView {\n"
"    selection-background-color: #e6e6e6;\n"
"}\n"
"\n"
"\n"
"QCalendarWidget QMenu::item:selected {\n"
"    background-color: #e6e6e6; /* Color de fondo de la selección */\n"
"}")
        self.dtpFechaIngresar.setObjectName("dtpFechaIngresar")
        self.gridLayout_2.addWidget(self.dtpFechaIngresar, 6, 0, 1, 1)
        self.lblNumeroPlazasIngresar = QtWidgets.QLabel(parent=self.tbIngresar)
        self.lblNumeroPlazasIngresar.setObjectName("lblNumeroPlazasIngresar")
        self.gridLayout_2.addWidget(self.lblNumeroPlazasIngresar, 0, 0, 1, 1)
        self.tbDisponibilidad.addTab(self.tbIngresar, "")
        self.tbModificar = QtWidgets.QWidget()
        self.tbModificar.setObjectName("tbModificar")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tbModificar)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.cmbTurnoModificar = QtWidgets.QComboBox(parent=self.tbModificar)
        self.cmbTurnoModificar.setObjectName("cmbTurnoModificar")
        self.gridLayout_3.addWidget(self.cmbTurnoModificar, 3, 0, 1, 1)
        self.lblTurnoModificar = QtWidgets.QLabel(parent=self.tbModificar)
        self.lblTurnoModificar.setObjectName("lblTurnoModificar")
        self.gridLayout_3.addWidget(self.lblTurnoModificar, 2, 0, 1, 1)
        self.dtpFechaModificar = QtWidgets.QCalendarWidget(parent=self.tbModificar)
        self.dtpFechaModificar.setStyleSheet("QCalendarWidget QToolButton {\n"
"    color: black;\n"
"    background-color: #e6e6e6;\n"
"    border: none;\n"
"    margin: 5px;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QCalendarWidget QWidget#qt_calendar_navigationbar {\n"
"    background-color: #e6e6e6;\n"
"}\n"
"\n"
"QCalendarWidget QTableView {\n"
"    selection-background-color: #e6e6e6;\n"
"}\n"
"\n"
"\n"
"QCalendarWidget QMenu::item:selected {\n"
"    background-color: #e6e6e6; /* Color de fondo de la selección */\n"
"}")
        self.dtpFechaModificar.setObjectName("dtpFechaModificar")
        self.gridLayout_3.addWidget(self.dtpFechaModificar, 1, 0, 1, 1)
        self.lblFechaModificar = QtWidgets.QLabel(parent=self.tbModificar)
        self.lblFechaModificar.setObjectName("lblFechaModificar")
        self.gridLayout_3.addWidget(self.lblFechaModificar, 0, 0, 1, 1)
        self.sbNumeroPlazasModificar = QtWidgets.QSpinBox(parent=self.tbModificar)
        self.sbNumeroPlazasModificar.setMaximumSize(QtCore.QSize(16777215, 16777200))
        self.sbNumeroPlazasModificar.setObjectName("sbNumeroPlazasModificar")
        self.gridLayout_3.addWidget(self.sbNumeroPlazasModificar, 5, 0, 1, 1)
        self.lblNumeroPlazasModificar = QtWidgets.QLabel(parent=self.tbModificar)
        self.lblNumeroPlazasModificar.setObjectName("lblNumeroPlazasModificar")
        self.gridLayout_3.addWidget(self.lblNumeroPlazasModificar, 4, 0, 1, 1)
        self.btnGuardarCambios = QtWidgets.QPushButton(parent=self.tbModificar)
        self.btnGuardarCambios.setObjectName("btnGuardarCambios")
        self.gridLayout_3.addWidget(self.btnGuardarCambios, 6, 0, 1, 1)
        self.tbDisponibilidad.addTab(self.tbModificar, "")
        self.tbEliminar = QtWidgets.QWidget()
        self.tbEliminar.setObjectName("tbEliminar")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tbEliminar)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.lblFechaEliminar = QtWidgets.QLabel(parent=self.tbEliminar)
        self.lblFechaEliminar.setObjectName("lblFechaEliminar")
        self.gridLayout_4.addWidget(self.lblFechaEliminar, 0, 0, 1, 1)
        self.lblTurnoEliminar = QtWidgets.QLabel(parent=self.tbEliminar)
        self.lblTurnoEliminar.setObjectName("lblTurnoEliminar")
        self.gridLayout_4.addWidget(self.lblTurnoEliminar, 2, 0, 1, 1)
        self.cmbTurnoEliminar = QtWidgets.QComboBox(parent=self.tbEliminar)
        self.cmbTurnoEliminar.setObjectName("cmbTurnoEliminar")
        self.gridLayout_4.addWidget(self.cmbTurnoEliminar, 3, 0, 1, 1)
        self.txtNumeroPlazasEliminar = QtWidgets.QLineEdit(parent=self.tbEliminar)
        self.txtNumeroPlazasEliminar.setEnabled(False)
        self.txtNumeroPlazasEliminar.setObjectName("txtNumeroPlazasEliminar")
        self.gridLayout_4.addWidget(self.txtNumeroPlazasEliminar, 5, 0, 1, 1)
        self.dtpFechaEliminar = QtWidgets.QCalendarWidget(parent=self.tbEliminar)
        self.dtpFechaEliminar.setStyleSheet("QCalendarWidget QToolButton {\n"
"    color: black;\n"
"    background-color: #e6e6e6;\n"
"    border: none;\n"
"    margin: 5px;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QCalendarWidget QWidget#qt_calendar_navigationbar {\n"
"    background-color: #e6e6e6;\n"
"}\n"
"\n"
"QCalendarWidget QTableView {\n"
"    selection-background-color: #e6e6e6;\n"
"}\n"
"\n"
"\n"
"QCalendarWidget QMenu::item:selected {\n"
"    background-color: #e6e6e6; /* Color de fondo de la selección */\n"
"}")
        self.dtpFechaEliminar.setObjectName("dtpFechaEliminar")
        self.gridLayout_4.addWidget(self.dtpFechaEliminar, 1, 0, 1, 1)
        self.lblNumeroPlazasEliminar = QtWidgets.QLabel(parent=self.tbEliminar)
        self.lblNumeroPlazasEliminar.setObjectName("lblNumeroPlazasEliminar")
        self.gridLayout_4.addWidget(self.lblNumeroPlazasEliminar, 4, 0, 1, 1)
        self.btnEliminar = QtWidgets.QPushButton(parent=self.tbEliminar)
        self.btnEliminar.setObjectName("btnEliminar")
        self.gridLayout_4.addWidget(self.btnEliminar, 6, 0, 1, 1)
        self.tbDisponibilidad.addTab(self.tbEliminar, "")
        self.tbListar = QtWidgets.QWidget()
        self.tbListar.setObjectName("tbListar")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tbListar)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.jgdDisponibilidad = QtWidgets.QTableWidget(parent=self.tbListar)
        self.jgdDisponibilidad.setObjectName("jgdDisponibilidad")
        self.jgdDisponibilidad.setColumnCount(0)
        self.jgdDisponibilidad.setRowCount(0)
        self.gridLayout_5.addWidget(self.jgdDisponibilidad, 0, 0, 1, 1)
        self.tbDisponibilidad.addTab(self.tbListar, "")
        self.gridLayout.addWidget(self.tbDisponibilidad, 0, 0, 1, 1)

        self.retranslateUi(Ui_Disponibilidad)
        self.tbDisponibilidad.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Ui_Disponibilidad)

    def retranslateUi(self, Ui_Disponibilidad):
        _translate = QtCore.QCoreApplication.translate
        Ui_Disponibilidad.setWindowTitle(_translate("Ui_Disponibilidad", "Disponibilidad"))
        self.lblFechaIngresar.setText(_translate("Ui_Disponibilidad", "Seleccione fecha"))
        self.lblTurnoIngresar.setText(_translate("Ui_Disponibilidad", "Seleccione turno"))
        self.btnIngresarDisponibilidad.setText(_translate("Ui_Disponibilidad", "Ingresar disponibilidad"))
        self.lblNumeroPlazasIngresar.setText(_translate("Ui_Disponibilidad", "Número de plazas"))
        self.tbDisponibilidad.setTabText(self.tbDisponibilidad.indexOf(self.tbIngresar), _translate("Ui_Disponibilidad", "Ingresar"))
        self.lblTurnoModificar.setText(_translate("Ui_Disponibilidad", "Seleccione turno"))
        self.lblFechaModificar.setText(_translate("Ui_Disponibilidad", "Seleccione fecha"))
        self.lblNumeroPlazasModificar.setText(_translate("Ui_Disponibilidad", "Número plazas"))
        self.btnGuardarCambios.setText(_translate("Ui_Disponibilidad", "Guardar cambios"))
        self.tbDisponibilidad.setTabText(self.tbDisponibilidad.indexOf(self.tbModificar), _translate("Ui_Disponibilidad", "Modificar"))
        self.lblFechaEliminar.setText(_translate("Ui_Disponibilidad", "Seleccione fecha"))
        self.lblTurnoEliminar.setText(_translate("Ui_Disponibilidad", "Seleccione turno"))
        self.lblNumeroPlazasEliminar.setText(_translate("Ui_Disponibilidad", "Número plazas"))
        self.btnEliminar.setText(_translate("Ui_Disponibilidad", "Eliminar"))
        self.tbDisponibilidad.setTabText(self.tbDisponibilidad.indexOf(self.tbEliminar), _translate("Ui_Disponibilidad", "Eliminar"))
        self.tbDisponibilidad.setTabText(self.tbDisponibilidad.indexOf(self.tbListar), _translate("Ui_Disponibilidad", "Listar"))