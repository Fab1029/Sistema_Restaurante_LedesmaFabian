# Form implementation generated from reading ui file 'Ui_Carta.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Carta(object):
    def setupUi(self, Ui_Carta):
        Ui_Carta.setObjectName("Ui_Carta")
        Ui_Carta.resize(1366, 768)
        Ui_Carta.setMinimumSize(QtCore.QSize(800, 600))
        Ui_Carta.setMaximumSize(QtCore.QSize(1366, 768))
        Ui_Carta.setStyleSheet("QWidget{\n"
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
        self.gridLayout = QtWidgets.QGridLayout(Ui_Carta)
        self.gridLayout.setObjectName("gridLayout")
        self.tbCarta = QtWidgets.QTabWidget(parent=Ui_Carta)
        self.tbCarta.setStyleSheet("")
        self.tbCarta.setObjectName("tbCarta")
        self.tbIngresar = QtWidgets.QWidget()
        self.tbIngresar.setObjectName("tbIngresar")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tbIngresar)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.txtNombreIngresar = QtWidgets.QLineEdit(parent=self.tbIngresar)
        self.txtNombreIngresar.setObjectName("txtNombreIngresar")
        self.gridLayout_2.addWidget(self.txtNombreIngresar, 1, 0, 1, 1)
        self.lblNombreIngresar = QtWidgets.QLabel(parent=self.tbIngresar)
        self.lblNombreIngresar.setObjectName("lblNombreIngresar")
        self.gridLayout_2.addWidget(self.lblNombreIngresar, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 18, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 13, 0, 1, 1)
        self.dtpFechaValidezIngresar = QtWidgets.QCalendarWidget(parent=self.tbIngresar)
        self.dtpFechaValidezIngresar.setStyleSheet("QCalendarWidget QToolButton {\n"
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
        self.dtpFechaValidezIngresar.setObjectName("dtpFechaValidezIngresar")
        self.gridLayout_2.addWidget(self.dtpFechaValidezIngresar, 15, 0, 1, 1)
        self.lblEliminarProductoIngresar = QtWidgets.QLabel(parent=self.tbIngresar)
        self.lblEliminarProductoIngresar.setObjectName("lblEliminarProductoIngresar")
        self.gridLayout_2.addWidget(self.lblEliminarProductoIngresar, 9, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.cmbEliminarProductoIngresar = QtWidgets.QComboBox(parent=self.tbIngresar)
        self.cmbEliminarProductoIngresar.setObjectName("cmbEliminarProductoIngresar")
        self.horizontalLayout_4.addWidget(self.cmbEliminarProductoIngresar)
        self.btnEliminarProductoIngresar = QtWidgets.QPushButton(parent=self.tbIngresar)
        self.btnEliminarProductoIngresar.setObjectName("btnEliminarProductoIngresar")
        self.horizontalLayout_4.addWidget(self.btnEliminarProductoIngresar)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 12, 0, 1, 1)
        self.lblAgregarProductoIngresar = QtWidgets.QLabel(parent=self.tbIngresar)
        self.lblAgregarProductoIngresar.setObjectName("lblAgregarProductoIngresar")
        self.gridLayout_2.addWidget(self.lblAgregarProductoIngresar, 3, 0, 1, 1)
        self.lblFechaValidezIngresar = QtWidgets.QLabel(parent=self.tbIngresar)
        self.lblFechaValidezIngresar.setObjectName("lblFechaValidezIngresar")
        self.gridLayout_2.addWidget(self.lblFechaValidezIngresar, 14, 0, 1, 1)
        self.btnIngresarCarta = QtWidgets.QPushButton(parent=self.tbIngresar)
        self.btnIngresarCarta.setObjectName("btnIngresarCarta")
        self.gridLayout_2.addWidget(self.btnIngresarCarta, 20, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cmbProductosIngresar = QtWidgets.QComboBox(parent=self.tbIngresar)
        self.cmbProductosIngresar.setObjectName("cmbProductosIngresar")
        self.horizontalLayout.addWidget(self.cmbProductosIngresar)
        self.btnAgregarProductoIngresar = QtWidgets.QPushButton(parent=self.tbIngresar)
        self.btnAgregarProductoIngresar.setObjectName("btnAgregarProductoIngresar")
        self.horizontalLayout.addWidget(self.btnAgregarProductoIngresar)
        self.gridLayout_2.addLayout(self.horizontalLayout, 6, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 2, 0, 1, 1)
        self.tbCarta.addTab(self.tbIngresar, "")
        self.tbModificar = QtWidgets.QWidget()
        self.tbModificar.setObjectName("tbModificar")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tbModificar)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lblAgregarProductoModificar = QtWidgets.QLabel(parent=self.tbModificar)
        self.lblAgregarProductoModificar.setObjectName("lblAgregarProductoModificar")
        self.gridLayout_3.addWidget(self.lblAgregarProductoModificar, 3, 0, 1, 1)
        self.lblFechaValidezModificar = QtWidgets.QLabel(parent=self.tbModificar)
        self.lblFechaValidezModificar.setObjectName("lblFechaValidezModificar")
        self.gridLayout_3.addWidget(self.lblFechaValidezModificar, 8, 0, 1, 1)
        self.lblEliminarProductoModificar = QtWidgets.QLabel(parent=self.tbModificar)
        self.lblEliminarProductoModificar.setObjectName("lblEliminarProductoModificar")
        self.gridLayout_3.addWidget(self.lblEliminarProductoModificar, 5, 0, 1, 1)
        self.cmbNombre = QtWidgets.QComboBox(parent=self.tbModificar)
        self.cmbNombre.setObjectName("cmbNombre")
        self.gridLayout_3.addWidget(self.cmbNombre, 1, 0, 1, 1)
        self.dtpFechaValidezModificar = QtWidgets.QCalendarWidget(parent=self.tbModificar)
        self.dtpFechaValidezModificar.setStyleSheet("QCalendarWidget QToolButton {\n"
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
        self.dtpFechaValidezModificar.setObjectName("dtpFechaValidezModificar")
        self.gridLayout_3.addWidget(self.dtpFechaValidezModificar, 9, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.cmbProductosModificar = QtWidgets.QComboBox(parent=self.tbModificar)
        self.cmbProductosModificar.setObjectName("cmbProductosModificar")
        self.horizontalLayout_2.addWidget(self.cmbProductosModificar)
        self.btnAgregarProductoModificar = QtWidgets.QPushButton(parent=self.tbModificar)
        self.btnAgregarProductoModificar.setObjectName("btnAgregarProductoModificar")
        self.horizontalLayout_2.addWidget(self.btnAgregarProductoModificar)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 4, 0, 1, 1)
        self.lblNombreModificar = QtWidgets.QLabel(parent=self.tbModificar)
        self.lblNombreModificar.setObjectName("lblNombreModificar")
        self.gridLayout_3.addWidget(self.lblNombreModificar, 0, 0, 1, 1)
        self.btnGuardarCambios = QtWidgets.QPushButton(parent=self.tbModificar)
        self.btnGuardarCambios.setObjectName("btnGuardarCambios")
        self.gridLayout_3.addWidget(self.btnGuardarCambios, 11, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.cmbProductosEliminarModificar = QtWidgets.QComboBox(parent=self.tbModificar)
        self.cmbProductosEliminarModificar.setObjectName("cmbProductosEliminarModificar")
        self.horizontalLayout_3.addWidget(self.cmbProductosEliminarModificar)
        self.btnEliminarProductoModificar = QtWidgets.QPushButton(parent=self.tbModificar)
        self.btnEliminarProductoModificar.setObjectName("btnEliminarProductoModificar")
        self.horizontalLayout_3.addWidget(self.btnEliminarProductoModificar)
        self.gridLayout_3.addLayout(self.horizontalLayout_3, 6, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_3.addItem(spacerItem3, 2, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_3.addItem(spacerItem4, 10, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_3.addItem(spacerItem5, 7, 0, 1, 1)
        self.tbCarta.addTab(self.tbModificar, "")
        self.tbEliminar = QtWidgets.QWidget()
        self.tbEliminar.setObjectName("tbEliminar")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tbEliminar)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.cmbNombreEliminar = QtWidgets.QComboBox(parent=self.tbEliminar)
        self.cmbNombreEliminar.setObjectName("cmbNombreEliminar")
        self.gridLayout_4.addWidget(self.cmbNombreEliminar, 1, 0, 1, 1)
        self.lblNombreEliminar = QtWidgets.QLabel(parent=self.tbEliminar)
        self.lblNombreEliminar.setObjectName("lblNombreEliminar")
        self.gridLayout_4.addWidget(self.lblNombreEliminar, 0, 0, 1, 1)
        self.btnEliminarCarta = QtWidgets.QPushButton(parent=self.tbEliminar)
        self.btnEliminarCarta.setObjectName("btnEliminarCarta")
        self.gridLayout_4.addWidget(self.btnEliminarCarta, 3, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_4.addItem(spacerItem6, 2, 0, 1, 1)
        self.tbCarta.addTab(self.tbEliminar, "")
        self.tbListar = QtWidgets.QWidget()
        self.tbListar.setObjectName("tbListar")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tbListar)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.jgdCartas = QtWidgets.QTableWidget(parent=self.tbListar)
        self.jgdCartas.setObjectName("jgdCartas")
        self.jgdCartas.setColumnCount(0)
        self.jgdCartas.setRowCount(0)
        self.jgdCartas.horizontalHeader().setCascadingSectionResizes(True)
        self.jgdCartas.horizontalHeader().setDefaultSectionSize(600)
        self.jgdCartas.horizontalHeader().setMinimumSectionSize(100)
        self.jgdCartas.verticalHeader().setCascadingSectionResizes(True)
        self.gridLayout_5.addWidget(self.jgdCartas, 0, 0, 1, 1)
        self.tbCarta.addTab(self.tbListar, "")
        self.gridLayout.addWidget(self.tbCarta, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(parent=Ui_Carta)
        self.label.setMinimumSize(QtCore.QSize(500, 750))
        self.label.setMaximumSize(QtCore.QSize(500, 750))
        self.label.setStyleSheet("")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("./Vistas/logoRestaurante.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)

        self.retranslateUi(Ui_Carta)
        self.tbCarta.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Ui_Carta)
        Ui_Carta.setTabOrder(self.tbCarta, self.txtNombreIngresar)
        Ui_Carta.setTabOrder(self.txtNombreIngresar, self.cmbProductosIngresar)
        Ui_Carta.setTabOrder(self.cmbProductosIngresar, self.btnAgregarProductoIngresar)
        Ui_Carta.setTabOrder(self.btnAgregarProductoIngresar, self.cmbEliminarProductoIngresar)
        Ui_Carta.setTabOrder(self.cmbEliminarProductoIngresar, self.btnEliminarProductoIngresar)
        Ui_Carta.setTabOrder(self.btnEliminarProductoIngresar, self.dtpFechaValidezIngresar)
        Ui_Carta.setTabOrder(self.dtpFechaValidezIngresar, self.btnIngresarCarta)
        Ui_Carta.setTabOrder(self.btnIngresarCarta, self.cmbNombre)
        Ui_Carta.setTabOrder(self.cmbNombre, self.cmbProductosModificar)
        Ui_Carta.setTabOrder(self.cmbProductosModificar, self.btnAgregarProductoModificar)
        Ui_Carta.setTabOrder(self.btnAgregarProductoModificar, self.cmbProductosEliminarModificar)
        Ui_Carta.setTabOrder(self.cmbProductosEliminarModificar, self.btnEliminarProductoModificar)
        Ui_Carta.setTabOrder(self.btnEliminarProductoModificar, self.dtpFechaValidezModificar)
        Ui_Carta.setTabOrder(self.dtpFechaValidezModificar, self.btnGuardarCambios)
        Ui_Carta.setTabOrder(self.btnGuardarCambios, self.cmbNombreEliminar)
        Ui_Carta.setTabOrder(self.cmbNombreEliminar, self.btnEliminarCarta)
        Ui_Carta.setTabOrder(self.btnEliminarCarta, self.jgdCartas)

    def retranslateUi(self, Ui_Carta):
        _translate = QtCore.QCoreApplication.translate
        Ui_Carta.setWindowTitle(_translate("Ui_Carta", "Carta"))
        self.txtNombreIngresar.setPlaceholderText(_translate("Ui_Carta", "Ingrese el nombre de la carta"))
        self.lblNombreIngresar.setText(_translate("Ui_Carta", "Nombre"))
        self.lblEliminarProductoIngresar.setText(_translate("Ui_Carta", "Eliminar producto"))
        self.btnEliminarProductoIngresar.setText(_translate("Ui_Carta", "Eliminar producto"))
        self.lblAgregarProductoIngresar.setText(_translate("Ui_Carta", "Agregar productos"))
        self.lblFechaValidezIngresar.setText(_translate("Ui_Carta", "Seleccionar fecha de validez"))
        self.btnIngresarCarta.setText(_translate("Ui_Carta", "Ingresar carta"))
        self.btnAgregarProductoIngresar.setText(_translate("Ui_Carta", "Agregar producto"))
        self.tbCarta.setTabText(self.tbCarta.indexOf(self.tbIngresar), _translate("Ui_Carta", "Ingresar"))
        self.lblAgregarProductoModificar.setText(_translate("Ui_Carta", "Agregar productos"))
        self.lblFechaValidezModificar.setText(_translate("Ui_Carta", "Modificar fecha validez"))
        self.lblEliminarProductoModificar.setText(_translate("Ui_Carta", "Eliminar producto"))
        self.btnAgregarProductoModificar.setText(_translate("Ui_Carta", "Agregar producto"))
        self.lblNombreModificar.setText(_translate("Ui_Carta", "Nombre"))
        self.btnGuardarCambios.setText(_translate("Ui_Carta", "Guardar cambios"))
        self.btnEliminarProductoModificar.setText(_translate("Ui_Carta", "Eliminar producto"))
        self.tbCarta.setTabText(self.tbCarta.indexOf(self.tbModificar), _translate("Ui_Carta", "Modificar"))
        self.lblNombreEliminar.setText(_translate("Ui_Carta", "Nombre"))
        self.btnEliminarCarta.setText(_translate("Ui_Carta", "Eliminar carta"))
        self.tbCarta.setTabText(self.tbCarta.indexOf(self.tbEliminar), _translate("Ui_Carta", "Eliminar"))
        self.tbCarta.setTabText(self.tbCarta.indexOf(self.tbListar), _translate("Ui_Carta", "Listar"))
