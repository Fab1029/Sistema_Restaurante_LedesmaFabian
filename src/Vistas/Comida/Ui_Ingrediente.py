# Form implementation generated from reading ui file 'Ui_Ingrediente.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Ingrediente(object):
    def setupUi(self, Ui_Ingrediente):
        Ui_Ingrediente.setObjectName("Ui_Ingrediente")
        Ui_Ingrediente.resize(906, 596)
        Ui_Ingrediente.setStyleSheet("QWidget{\n"
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
        self.gridLayout = QtWidgets.QGridLayout(Ui_Ingrediente)
        self.gridLayout.setObjectName("gridLayout")
        self.tbIngrediente = QtWidgets.QTabWidget(parent=Ui_Ingrediente)
        self.tbIngrediente.setObjectName("tbIngrediente")
        self.tbIngresar = QtWidgets.QWidget()
        self.tbIngresar.setObjectName("tbIngresar")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tbIngresar)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.cmbMedidaIngresar = QtWidgets.QComboBox(parent=self.tbIngresar)
        self.cmbMedidaIngresar.setObjectName("cmbMedidaIngresar")
        self.gridLayout_2.addWidget(self.cmbMedidaIngresar, 7, 0, 1, 1)
        self.lblMedidaIngresar = QtWidgets.QLabel(parent=self.tbIngresar)
        self.lblMedidaIngresar.setObjectName("lblMedidaIngresar")
        self.gridLayout_2.addWidget(self.lblMedidaIngresar, 6, 0, 1, 1)
        self.txtNombreIngresar = QtWidgets.QLineEdit(parent=self.tbIngresar)
        self.txtNombreIngresar.setObjectName("txtNombreIngresar")
        self.gridLayout_2.addWidget(self.txtNombreIngresar, 1, 0, 1, 1)
        self.lblNombreIngresar = QtWidgets.QLabel(parent=self.tbIngresar)
        self.lblNombreIngresar.setObjectName("lblNombreIngresar")
        self.gridLayout_2.addWidget(self.lblNombreIngresar, 0, 0, 1, 1)
        self.lblTipoIngresar = QtWidgets.QLabel(parent=self.tbIngresar)
        self.lblTipoIngresar.setObjectName("lblTipoIngresar")
        self.gridLayout_2.addWidget(self.lblTipoIngresar, 3, 0, 1, 1)
        self.cmbTipoIngresar = QtWidgets.QComboBox(parent=self.tbIngresar)
        self.cmbTipoIngresar.setObjectName("cmbTipoIngresar")
        self.gridLayout_2.addWidget(self.cmbTipoIngresar, 4, 0, 1, 1)
        self.btnIngresarIngrediente = QtWidgets.QPushButton(parent=self.tbIngresar)
        self.btnIngresarIngrediente.setObjectName("btnIngresarIngrediente")
        self.gridLayout_2.addWidget(self.btnIngresarIngrediente, 8, 0, 1, 1)
        self.tbIngrediente.addTab(self.tbIngresar, "")
        self.tbModificar = QtWidgets.QWidget()
        self.tbModificar.setObjectName("tbModificar")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tbModificar)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.cmbMedidaModificar = QtWidgets.QComboBox(parent=self.tbModificar)
        self.cmbMedidaModificar.setObjectName("cmbMedidaModificar")
        self.gridLayout_3.addWidget(self.cmbMedidaModificar, 5, 0, 1, 1)
        self.cmbTipoModificar = QtWidgets.QComboBox(parent=self.tbModificar)
        self.cmbTipoModificar.setObjectName("cmbTipoModificar")
        self.gridLayout_3.addWidget(self.cmbTipoModificar, 3, 0, 1, 1)
        self.lblMedidaModificar = QtWidgets.QLabel(parent=self.tbModificar)
        self.lblMedidaModificar.setObjectName("lblMedidaModificar")
        self.gridLayout_3.addWidget(self.lblMedidaModificar, 4, 0, 1, 1)
        self.cmbNombreModificar = QtWidgets.QComboBox(parent=self.tbModificar)
        self.cmbNombreModificar.setObjectName("cmbNombreModificar")
        self.gridLayout_3.addWidget(self.cmbNombreModificar, 1, 0, 1, 1)
        self.lblTipoModificar = QtWidgets.QLabel(parent=self.tbModificar)
        self.lblTipoModificar.setObjectName("lblTipoModificar")
        self.gridLayout_3.addWidget(self.lblTipoModificar, 2, 0, 1, 1)
        self.lblNombreModificar = QtWidgets.QLabel(parent=self.tbModificar)
        self.lblNombreModificar.setObjectName("lblNombreModificar")
        self.gridLayout_3.addWidget(self.lblNombreModificar, 0, 0, 1, 1)
        self.btnGuardarCambios = QtWidgets.QPushButton(parent=self.tbModificar)
        self.btnGuardarCambios.setObjectName("btnGuardarCambios")
        self.gridLayout_3.addWidget(self.btnGuardarCambios, 6, 0, 1, 1)
        self.tbIngrediente.addTab(self.tbModificar, "")
        self.tbEliminar = QtWidgets.QWidget()
        self.tbEliminar.setObjectName("tbEliminar")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tbEliminar)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.btnElimarIngrediente = QtWidgets.QPushButton(parent=self.tbEliminar)
        self.btnElimarIngrediente.setObjectName("btnElimarIngrediente")
        self.gridLayout_4.addWidget(self.btnElimarIngrediente, 3, 0, 1, 1)
        self.lblNombreEliminar = QtWidgets.QLabel(parent=self.tbEliminar)
        self.lblNombreEliminar.setObjectName("lblNombreEliminar")
        self.gridLayout_4.addWidget(self.lblNombreEliminar, 0, 0, 1, 1)
        self.cmbNombreEliminar = QtWidgets.QComboBox(parent=self.tbEliminar)
        self.cmbNombreEliminar.setObjectName("cmbNombreEliminar")
        self.gridLayout_4.addWidget(self.cmbNombreEliminar, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_4.addItem(spacerItem, 2, 0, 1, 1)
        self.tbIngrediente.addTab(self.tbEliminar, "")
        self.tbListar = QtWidgets.QWidget()
        self.tbListar.setObjectName("tbListar")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tbListar)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.jgdIngredientes = QtWidgets.QTableWidget(parent=self.tbListar)
        self.jgdIngredientes.setObjectName("jgdIngredientes")
        self.jgdIngredientes.setColumnCount(0)
        self.jgdIngredientes.setRowCount(0)

        self.gridLayout_5.addWidget(self.jgdIngredientes, 0, 0, 1, 1)
        self.tbIngrediente.addTab(self.tbListar, "")
        self.gridLayout.addWidget(self.tbIngrediente, 0, 0, 1, 1)

        self.retranslateUi(Ui_Ingrediente)
        self.tbIngrediente.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Ui_Ingrediente)

    def retranslateUi(self, Ui_Ingrediente):
        _translate = QtCore.QCoreApplication.translate
        Ui_Ingrediente.setWindowTitle(_translate("Ui_Ingrediente", "Ingrediente"))
        self.lblMedidaIngresar.setText(_translate("Ui_Ingrediente", "Unidad medida"))
        self.txtNombreIngresar.setPlaceholderText(_translate("Ui_Ingrediente", "Ingrese nombre ingrediente"))
        self.lblNombreIngresar.setText(_translate("Ui_Ingrediente", "Nombe ingrediente"))
        self.lblTipoIngresar.setText(_translate("Ui_Ingrediente", "Tipo"))
        self.btnIngresarIngrediente.setText(_translate("Ui_Ingrediente", "Ingresar ingrediente"))
        self.tbIngrediente.setTabText(self.tbIngrediente.indexOf(self.tbIngresar), _translate("Ui_Ingrediente", "Ingresar"))
        self.lblMedidaModificar.setText(_translate("Ui_Ingrediente", "Unidad medida"))
        self.lblTipoModificar.setText(_translate("Ui_Ingrediente", "Tipo"))
        self.lblNombreModificar.setText(_translate("Ui_Ingrediente", "Nombre ingrediente"))
        self.btnGuardarCambios.setText(_translate("Ui_Ingrediente", "Guardar cambios"))
        self.tbIngrediente.setTabText(self.tbIngrediente.indexOf(self.tbModificar), _translate("Ui_Ingrediente", "Modificar"))
        self.btnElimarIngrediente.setText(_translate("Ui_Ingrediente", "Eliminar ingrediente"))
        self.lblNombreEliminar.setText(_translate("Ui_Ingrediente", "Nombre ingrediente"))
        self.tbIngrediente.setTabText(self.tbIngrediente.indexOf(self.tbEliminar), _translate("Ui_Ingrediente", "Eliminar"))
        self.tbIngrediente.setTabText(self.tbIngrediente.indexOf(self.tbListar), _translate("Ui_Ingrediente", "Listar"))
