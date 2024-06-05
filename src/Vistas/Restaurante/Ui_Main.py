# Form implementation generated from reading ui file 'Ui_Main.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Main(object):
    def setupUi(self, Ui_Main):
        Ui_Main.setObjectName("Ui_Main")
        Ui_Main.resize(3373, 1838)
        Ui_Main.setStyleSheet("QMainWindow{\n"
"    background-color: white;\n"
"}\n"
"\n"
"/* QToolBar */\n"
"QToolBar{\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QToolButton{\n"
"    font-family: \"Sans-serif\";\n"
"    font-size: 14px;\n"
"    padding: 10px;\n"
"    margin: 5px;\n"
"    border-radius: 10px;\n"
"\n"
"}\n"
"\n"
"QToolButton:hover{\n"
"    background-color:#E4E8EB;\n"
"}\n"
"\n"
"/* QMenuBar */\n"
"QMenuBar{\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QMenuBar::item{\n"
"    font-family: \"Sans-serif\";\n"
"    font-size: 14px;\n"
"    padding: 5px 10px;\n"
"    background: transparent;\n"
"}\n"
"\n"
"QMenuBar::item:selected{\n"
"    background: #E4E8EB;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"/* QMenu */\n"
"QMenu{\n"
"    background-color: white;\n"
"    border: 2px solid rgb(228, 232, 235);\n"
"}\n"
"\n"
"QMenu::item{\n"
"    font-family: \"Sans-serif\";\n"
"    font-size: 14px;\n"
"    padding: 5px 10px;\n"
"}\n"
"\n"
"QMenu::item:selected{\n"
"    background-color: #E4E8EB;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QLabel{\n"
"font-family:\"Sans-serif\";\n"
"font-size:25px;\n"
"padding:5px;\n"
"\n"
"}")
        self.centralwidget = QtWidgets.QWidget(parent=Ui_Main)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 5, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 4, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.lblLogoRestaurante = QtWidgets.QLabel(parent=self.centralwidget)
        self.lblLogoRestaurante.setText("")
        self.lblLogoRestaurante.setPixmap(QtGui.QPixmap("./Vistas/logoRestaurante.jpg"))
        self.lblLogoRestaurante.setScaledContents(True)
        self.lblLogoRestaurante.setObjectName("label_7")
        self.lblLogoRestaurante.setMaximumSize(600, 600)
        self.gridLayout.addWidget(self.lblLogoRestaurante, 0, 1, 1, 1)
        Ui_Main.setCentralWidget(self.centralwidget)
        self.jmbMenu = QtWidgets.QMenuBar(parent=Ui_Main)
        self.jmbMenu.setGeometry(QtCore.QRect(0, 0, 3373, 41))
        self.jmbMenu.setObjectName("jmbMenu")
        self.menuMenu = QtWidgets.QMenu(parent=self.jmbMenu)
        self.menuMenu.setObjectName("menuMenu")
        self.jmbReserva = QtWidgets.QMenu(parent=self.menuMenu)
        self.jmbReserva.setObjectName("jmbReserva")
        self.jmbDisponibilidad = QtWidgets.QMenu(parent=self.menuMenu)
        self.jmbDisponibilidad.setObjectName("jmbDisponibilidad")
        self.jmbCarta = QtWidgets.QMenu(parent=self.menuMenu)
        self.jmbCarta.setObjectName("jmbCarta")
        self.jmbProducto = QtWidgets.QMenu(parent=self.menuMenu)
        self.jmbProducto.setObjectName("jmbProducto")
        self.jmbIngrediente = QtWidgets.QMenu(parent=self.menuMenu)
        self.jmbIngrediente.setObjectName("jmbIngrediente")
        self.jmbPersonal = QtWidgets.QMenu(parent=self.menuMenu)
        self.jmbPersonal.setObjectName("jmbPersonal")
        self.jmbAcercaDe = QtWidgets.QMenu(parent=self.jmbMenu)
        self.jmbAcercaDe.setObjectName("jmbAcercaDe")
        Ui_Main.setMenuBar(self.jmbMenu)
        self.statusbar = QtWidgets.QStatusBar(parent=Ui_Main)
        self.statusbar.setObjectName("statusbar")
        Ui_Main.setStatusBar(self.statusbar)
        self.jtbAccesosRapidos = QtWidgets.QToolBar(parent=Ui_Main)
        self.jtbAccesosRapidos.setObjectName("jtbAccesosRapidos")
        Ui_Main.addToolBar(QtCore.Qt.ToolBarArea.TopToolBarArea, self.jtbAccesosRapidos)
        self.jmbReservaIngresar = QtGui.QAction(parent=Ui_Main)
        self.jmbReservaIngresar.setObjectName("jmbReservaIngresar")
        self.jmbReservaModificar = QtGui.QAction(parent=Ui_Main)
        self.jmbReservaModificar.setObjectName("jmbReservaModificar")
        self.jmbReservaEliminar = QtGui.QAction(parent=Ui_Main)
        self.jmbReservaEliminar.setObjectName("jmbReservaEliminar")
        self.jmbReservaListar = QtGui.QAction(parent=Ui_Main)
        self.jmbReservaListar.setObjectName("jmbReservaListar")
        self.jmbDisponibilidadIngresar = QtGui.QAction(parent=Ui_Main)
        self.jmbDisponibilidadIngresar.setObjectName("jmbDisponibilidadIngresar")
        self.jmbDisponibilidadModificar = QtGui.QAction(parent=Ui_Main)
        self.jmbDisponibilidadModificar.setObjectName("jmbDisponibilidadModificar")
        self.jmbDisponibilidadEliminar = QtGui.QAction(parent=Ui_Main)
        self.jmbDisponibilidadEliminar.setObjectName("jmbDisponibilidadEliminar")
        self.jmbDisponibilidadListar = QtGui.QAction(parent=Ui_Main)
        self.jmbDisponibilidadListar.setObjectName("jmbDisponibilidadListar")
        self.jmbCartaIngresar = QtGui.QAction(parent=Ui_Main)
        self.jmbCartaIngresar.setObjectName("jmbCartaIngresar")
        self.jmbCartaModificar = QtGui.QAction(parent=Ui_Main)
        self.jmbCartaModificar.setObjectName("jmbCartaModificar")
        self.jmbCartaEliminar = QtGui.QAction(parent=Ui_Main)
        self.jmbCartaEliminar.setObjectName("jmbCartaEliminar")
        self.jmbCartaListar = QtGui.QAction(parent=Ui_Main)
        self.jmbCartaListar.setObjectName("jmbCartaListar")
        self.jmbProductoIngresar = QtGui.QAction(parent=Ui_Main)
        self.jmbProductoIngresar.setObjectName("jmbProductoIngresar")
        self.jmbProductoModificar = QtGui.QAction(parent=Ui_Main)
        self.jmbProductoModificar.setObjectName("jmbProductoModificar")
        self.jmbProductoEliminar = QtGui.QAction(parent=Ui_Main)
        self.jmbProductoEliminar.setObjectName("jmbProductoEliminar")
        self.jmbProductoListar = QtGui.QAction(parent=Ui_Main)
        self.jmbProductoListar.setObjectName("jmbProductoListar")
        self.jmbIngredienteIngresar = QtGui.QAction(parent=Ui_Main)
        self.jmbIngredienteIngresar.setObjectName("jmbIngredienteIngresar")
        self.jmbIngredienteModificar = QtGui.QAction(parent=Ui_Main)
        self.jmbIngredienteModificar.setObjectName("jmbIngredienteModificar")
        self.jmbIngredienteEliminar = QtGui.QAction(parent=Ui_Main)
        self.jmbIngredienteEliminar.setObjectName("jmbIngredienteEliminar")
        self.jmbIngredienteListar = QtGui.QAction(parent=Ui_Main)
        self.jmbIngredienteListar.setObjectName("jmbIngredienteListar")
        self.jmbPersonalIngresar = QtGui.QAction(parent=Ui_Main)
        self.jmbPersonalIngresar.setObjectName("jmbPersonalIngresar")
        self.jmbPersonalModificar = QtGui.QAction(parent=Ui_Main)
        self.jmbPersonalModificar.setObjectName("jmbPersonalModificar")
        self.jmbPersonalEliminar = QtGui.QAction(parent=Ui_Main)
        self.jmbPersonalEliminar.setObjectName("jmbPersonalEliminar")
        self.jmbPersonalListar = QtGui.QAction(parent=Ui_Main)
        self.jmbPersonalListar.setObjectName("jmbPersonalListar")
        self.jmbConfiguracion = QtGui.QAction(parent=Ui_Main)
        self.jmbConfiguracion.setObjectName("jmbConfiguracion")
        self.jmbSalir = QtGui.QAction(parent=Ui_Main)
        self.jmbSalir.setObjectName("jmbSalir")
        self.jtbReservaIngresar = QtGui.QAction(parent=Ui_Main)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./Vistas/reserva.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.jtbReservaIngresar.setIcon(icon)
        self.jtbReservaIngresar.setObjectName("jtbReservaIngresar")
        self.jtbDisponibilidadIngresar = QtGui.QAction(parent=Ui_Main)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./Vistas/disponibilidad.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.jtbDisponibilidadIngresar.setIcon(icon1)
        self.jtbDisponibilidadIngresar.setObjectName("jtbDisponibilidadIngresar")
        self.jmbReserva.addAction(self.jmbReservaIngresar)
        self.jmbReserva.addAction(self.jmbReservaModificar)
        self.jmbReserva.addAction(self.jmbReservaEliminar)
        self.jmbReserva.addAction(self.jmbReservaListar)
        self.jmbDisponibilidad.addAction(self.jmbDisponibilidadIngresar)
        self.jmbDisponibilidad.addAction(self.jmbDisponibilidadModificar)
        self.jmbDisponibilidad.addAction(self.jmbDisponibilidadEliminar)
        self.jmbDisponibilidad.addAction(self.jmbDisponibilidadListar)
        self.jmbCarta.addAction(self.jmbCartaIngresar)
        self.jmbCarta.addAction(self.jmbCartaModificar)
        self.jmbCarta.addAction(self.jmbCartaEliminar)
        self.jmbCarta.addAction(self.jmbCartaListar)
        self.jmbProducto.addAction(self.jmbProductoIngresar)
        self.jmbProducto.addAction(self.jmbProductoModificar)
        self.jmbProducto.addAction(self.jmbProductoEliminar)
        self.jmbProducto.addAction(self.jmbProductoListar)
        self.jmbIngrediente.addAction(self.jmbIngredienteIngresar)
        self.jmbIngrediente.addAction(self.jmbIngredienteModificar)
        self.jmbIngrediente.addAction(self.jmbIngredienteEliminar)
        self.jmbIngrediente.addAction(self.jmbIngredienteListar)
        self.jmbPersonal.addAction(self.jmbPersonalIngresar)
        self.jmbPersonal.addAction(self.jmbPersonalModificar)
        self.jmbPersonal.addAction(self.jmbPersonalEliminar)
        self.jmbPersonal.addAction(self.jmbPersonalListar)
        self.menuMenu.addAction(self.jmbReserva.menuAction())
        self.menuMenu.addAction(self.jmbDisponibilidad.menuAction())
        self.menuMenu.addAction(self.jmbCarta.menuAction())
        self.menuMenu.addAction(self.jmbProducto.menuAction())
        self.menuMenu.addAction(self.jmbIngrediente.menuAction())
        self.menuMenu.addAction(self.jmbPersonal.menuAction())
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.jmbConfiguracion)
        self.menuMenu.addAction(self.jmbSalir)
        self.jmbMenu.addAction(self.menuMenu.menuAction())
        self.jmbMenu.addAction(self.jmbAcercaDe.menuAction())
        self.jtbAccesosRapidos.addAction(self.jtbReservaIngresar)
        self.jtbAccesosRapidos.addAction(self.jtbDisponibilidadIngresar)

        self.retranslateUi(Ui_Main)
        QtCore.QMetaObject.connectSlotsByName(Ui_Main)

    def retranslateUi(self, Ui_Main):
        _translate = QtCore.QCoreApplication.translate
        Ui_Main.setWindowTitle(_translate("Ui_Main", "Restaurante"))
        self.label_6.setText(_translate("Ui_Main", "<html><head/><body><p align=\"justify\"><span style=\" font-size:15pt;\">No compartir información confidencial con terceros sin autorización</span></p></body></html>"))
        self.label_4.setText(_translate("Ui_Main", "<html><head/><body><p align=\"justify\"><span style=\" font-size:15pt;\">Actualizar el inventario de ingredientes regularmente</span><br/></p></body></html>"))
        self.label_5.setText(_translate("Ui_Main", "<html><head/><body><p align=\"justify\"><span style=\" font-size:15pt;\">Proteger la información de encargados</span></p></body></html>"))
        self.label_3.setText(_translate("Ui_Main", "<html><head/><body><p align=\"justify\"><span style=\" font-size:15pt;\">Registrar todas las reservas en la aplicación de manera oportuna</span></p></body></html>"))
        self.label_2.setText(_translate("Ui_Main", "<html><head/><body><p align=\"justify\"><span style=\" font-size:15pt;\">Mantener la información de cartas, productos y reservas actualizada</span></p></body></html>"))
        self.label.setText(_translate("Ui_Main", "Normas de uso"))
        self.menuMenu.setTitle(_translate("Ui_Main", "Menu"))
        self.jmbReserva.setTitle(_translate("Ui_Main", "Reserva"))
        self.jmbDisponibilidad.setTitle(_translate("Ui_Main", "Disponibilidad"))
        self.jmbCarta.setTitle(_translate("Ui_Main", "Carta"))
        self.jmbProducto.setTitle(_translate("Ui_Main", "Producto"))
        self.jmbIngrediente.setTitle(_translate("Ui_Main", "Ingrediente"))
        self.jmbPersonal.setTitle(_translate("Ui_Main", "Personal"))
        self.jmbAcercaDe.setTitle(_translate("Ui_Main", "Acerca de"))
        self.jtbAccesosRapidos.setWindowTitle(_translate("Ui_Main", "toolBar"))
        self.jmbReservaIngresar.setText(_translate("Ui_Main", "Ingresar"))
        self.jmbReservaModificar.setText(_translate("Ui_Main", "Modificar"))
        self.jmbReservaEliminar.setText(_translate("Ui_Main", "Eliminar"))
        self.jmbReservaListar.setText(_translate("Ui_Main", "Listar"))
        self.jmbDisponibilidadIngresar.setText(_translate("Ui_Main", "Ingresar"))
        self.jmbDisponibilidadModificar.setText(_translate("Ui_Main", "Modificar"))
        self.jmbDisponibilidadEliminar.setText(_translate("Ui_Main", "Eliminar"))
        self.jmbDisponibilidadListar.setText(_translate("Ui_Main", "Listar"))
        self.jmbCartaIngresar.setText(_translate("Ui_Main", "Ingresar"))
        self.jmbCartaModificar.setText(_translate("Ui_Main", "Modificar"))
        self.jmbCartaEliminar.setText(_translate("Ui_Main", "Eliminar"))
        self.jmbCartaListar.setText(_translate("Ui_Main", "Listar"))
        self.jmbProductoIngresar.setText(_translate("Ui_Main", "Ingresar"))
        self.jmbProductoModificar.setText(_translate("Ui_Main", "Modificar"))
        self.jmbProductoEliminar.setText(_translate("Ui_Main", "Eliminar"))
        self.jmbProductoListar.setText(_translate("Ui_Main", "Listar"))
        self.jmbIngredienteIngresar.setText(_translate("Ui_Main", "Ingresar"))
        self.jmbIngredienteModificar.setText(_translate("Ui_Main", "Modificar"))
        self.jmbIngredienteEliminar.setText(_translate("Ui_Main", "Eliminar"))
        self.jmbIngredienteListar.setText(_translate("Ui_Main", "Listar"))
        self.jmbPersonalIngresar.setText(_translate("Ui_Main", "Ingresar"))
        self.jmbPersonalModificar.setText(_translate("Ui_Main", "Modificar"))
        self.jmbPersonalEliminar.setText(_translate("Ui_Main", "Eliminar"))
        self.jmbPersonalListar.setText(_translate("Ui_Main", "Listar"))
        self.jmbConfiguracion.setText(_translate("Ui_Main", "Configuración"))
        self.jmbSalir.setText(_translate("Ui_Main", "Salir"))
        self.jtbReservaIngresar.setText(_translate("Ui_Main", "Ingresar reserva"))
        self.jtbDisponibilidadIngresar.setText(_translate("Ui_Main", "Ingresar disponibilidad"))
