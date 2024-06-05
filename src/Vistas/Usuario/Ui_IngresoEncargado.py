# Form implementation generated from reading ui file 'Ui_IngresoEncargado.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Ui_IngresoEncargado(object):
    def setupUi(self, Ui_IngresoEncargado):
        Ui_IngresoEncargado.setObjectName("Ui_IngresoEncargado")
        Ui_IngresoEncargado.resize(990, 600)
        Ui_IngresoEncargado.setStyleSheet("QWidget{\n"
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
"QLineEdit{\n"
"font-family:\"Sans-serif\";\n"
"font-size:14px;\n"
"padding:10px 10px;\n"
"border-radius:10px;\n"
"margin-left:10px;\n"
"margin-right: 10px;\n"
"border:2px solid rgb(228, 232, 235);\n"
"}\n"
"\n"
"QPushButton{\n"
"font-family:\"Sans-serif\";\n"
"background-color: #E4E8EB;\n"
"padding: 10px 10px;\n"
"border-radius: 10px;\n"
"margin-left:10px;\n"
"margin-right:10px;\n"
"}\n"
"\n"
"\n"
"QLineEdit:hover{\n"
"border:2px solid black;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:2px solid black;\n"
"}\n"
"")
        self.gridLayout = QtWidgets.QGridLayout(Ui_IngresoEncargado)
        self.gridLayout.setObjectName("gridLayout")
        self.tbEncargado = QtWidgets.QTabWidget(parent=Ui_IngresoEncargado)
        self.tbEncargado.setObjectName("tbEncargado")
        self.tbIngresar = QtWidgets.QWidget()
        self.tbIngresar.setObjectName("tbIngresar")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tbIngresar)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lblClaveIngresar = QtWidgets.QLabel(parent=self.tbIngresar)
        self.lblClaveIngresar.setObjectName("lblClaveIngresar")
        self.gridLayout_2.addWidget(self.lblClaveIngresar, 6, 0, 1, 1)
        self.txtClaveIngresar = QtWidgets.QLineEdit(parent=self.tbIngresar)
        self.txtClaveIngresar.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.txtClaveIngresar.setObjectName("txtClaveIngresar")
        self.gridLayout_2.addWidget(self.txtClaveIngresar, 7, 0, 1, 1)
        self.cbxMostrarClaveIngresar = QtWidgets.QCheckBox(parent=self.tbIngresar)
        self.cbxMostrarClaveIngresar.setObjectName("cbxMostrarClaveIngresar")
        self.gridLayout_2.addWidget(self.cbxMostrarClaveIngresar, 7, 1, 1, 1)
        self.txtCedulaIngresar = QtWidgets.QLineEdit(parent=self.tbIngresar)
        self.txtCedulaIngresar.setObjectName("txtCedulaIngresar")
        self.gridLayout_2.addWidget(self.txtCedulaIngresar, 1, 0, 1, 1)
        self.txtDireccionIngresar = QtWidgets.QLineEdit(parent=self.tbIngresar)
        self.txtDireccionIngresar.setObjectName("txtDireccionIngresar")
        self.gridLayout_2.addWidget(self.txtDireccionIngresar, 5, 0, 1, 1)
        self.lblNombreApellidoIngresar = QtWidgets.QLabel(parent=self.tbIngresar)
        self.lblNombreApellidoIngresar.setObjectName("lblNombreApellidoIngresar")
        self.gridLayout_2.addWidget(self.lblNombreApellidoIngresar, 2, 0, 1, 1)
        self.lblCedulaIngresar = QtWidgets.QLabel(parent=self.tbIngresar)
        self.lblCedulaIngresar.setObjectName("lblCedulaIngresar")
        self.gridLayout_2.addWidget(self.lblCedulaIngresar, 0, 0, 1, 1)
        self.txtNombreApellidoIngresar = QtWidgets.QLineEdit(parent=self.tbIngresar)
        self.txtNombreApellidoIngresar.setObjectName("txtNombreApellidoIngresar")
        self.gridLayout_2.addWidget(self.txtNombreApellidoIngresar, 3, 0, 1, 1)
        self.lblDireccionIngresar = QtWidgets.QLabel(parent=self.tbIngresar)
        self.lblDireccionIngresar.setObjectName("lblDireccionIngresar")
        self.gridLayout_2.addWidget(self.lblDireccionIngresar, 4, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnIngresarEncargado = QtWidgets.QPushButton(parent=self.tbIngresar)
        self.btnIngresarEncargado.setObjectName("btnIngresarEncargado")
        self.horizontalLayout.addWidget(self.btnIngresarEncargado)
        self.btnLimpiarCampos = QtWidgets.QPushButton(parent=self.tbIngresar)
        self.btnLimpiarCampos.setObjectName("btnLimpiarCampos")
        self.horizontalLayout.addWidget(self.btnLimpiarCampos)
        self.gridLayout_2.addLayout(self.horizontalLayout, 8, 0, 1, 2)
        self.tbEncargado.addTab(self.tbIngresar, "")
        self.tbModificar = QtWidgets.QWidget()
        self.tbModificar.setObjectName("tbModificar")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tbModificar)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.txtNombreApellidoModificar = QtWidgets.QLineEdit(parent=self.tbModificar)
        self.txtNombreApellidoModificar.setEnabled(False)
        self.txtNombreApellidoModificar.setObjectName("txtNombreApellidoModificar")
        self.gridLayout_3.addWidget(self.txtNombreApellidoModificar, 3, 0, 1, 1)
        self.lblNombreApellidoModificar = QtWidgets.QLabel(parent=self.tbModificar)
        self.lblNombreApellidoModificar.setObjectName("lblNombreApellidoModificar")
        self.gridLayout_3.addWidget(self.lblNombreApellidoModificar, 2, 0, 1, 1)
        self.lblDireccionModificar = QtWidgets.QLabel(parent=self.tbModificar)
        self.lblDireccionModificar.setObjectName("lblDireccionModificar")
        self.gridLayout_3.addWidget(self.lblDireccionModificar, 4, 0, 1, 1)
        self.txtDireccionModificar = QtWidgets.QLineEdit(parent=self.tbModificar)
        self.txtDireccionModificar.setEnabled(False)
        self.txtDireccionModificar.setObjectName("txtDireccionModificar")
        self.gridLayout_3.addWidget(self.txtDireccionModificar, 5, 0, 1, 1)
        self.lblClaveModificar = QtWidgets.QLabel(parent=self.tbModificar)
        self.lblClaveModificar.setObjectName("lblClaveModificar")
        self.gridLayout_3.addWidget(self.lblClaveModificar, 6, 0, 1, 1)
        self.txtClaveModificar = QtWidgets.QLineEdit(parent=self.tbModificar)
        self.txtClaveModificar.setEnabled(False)
        self.txtClaveModificar.setObjectName("txtClaveModificar")
        self.gridLayout_3.addWidget(self.txtClaveModificar, 8, 0, 1, 1)
        self.lblCedulaModificar = QtWidgets.QLabel(parent=self.tbModificar)
        self.lblCedulaModificar.setObjectName("lblCedulaModificar")
        self.gridLayout_3.addWidget(self.lblCedulaModificar, 0, 0, 1, 1)
        self.txtCedulaModificar = QtWidgets.QLineEdit(parent=self.tbModificar)
        self.txtCedulaModificar.setObjectName("txtCedulaModificar")
        self.gridLayout_3.addWidget(self.txtCedulaModificar, 1, 0, 1, 1)
        self.cbxMostrarClaveModificar = QtWidgets.QCheckBox(parent=self.tbModificar)
        self.cbxMostrarClaveModificar.setEnabled(False)
        self.cbxMostrarClaveModificar.setObjectName("cbxMostrarClaveModificar")
        self.gridLayout_3.addWidget(self.cbxMostrarClaveModificar, 8, 1, 1, 1)
        self.btnGuardarCambios = QtWidgets.QPushButton(parent=self.tbModificar)
        self.btnGuardarCambios.setObjectName("btnGuardarCambios")
        self.gridLayout_3.addWidget(self.btnGuardarCambios, 9, 0, 1, 1)
        self.tbEncargado.addTab(self.tbModificar, "")
        self.tbEliminar = QtWidgets.QWidget()
        self.tbEliminar.setObjectName("tbEliminar")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tbEliminar)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.lblDireccionEliminar = QtWidgets.QLabel(parent=self.tbEliminar)
        self.lblDireccionEliminar.setObjectName("lblDireccionEliminar")
        self.gridLayout_4.addWidget(self.lblDireccionEliminar, 4, 0, 1, 1)
        self.txtNombreApellidoEliminar = QtWidgets.QLineEdit(parent=self.tbEliminar)
        self.txtNombreApellidoEliminar.setEnabled(False)
        self.txtNombreApellidoEliminar.setObjectName("txtNombreApellidoEliminar")
        self.gridLayout_4.addWidget(self.txtNombreApellidoEliminar, 3, 0, 1, 1)
        self.txtDireccionEliminar = QtWidgets.QLineEdit(parent=self.tbEliminar)
        self.txtDireccionEliminar.setEnabled(False)
        self.txtDireccionEliminar.setObjectName("txtDireccionEliminar")
        self.gridLayout_4.addWidget(self.txtDireccionEliminar, 5, 0, 1, 1)
        self.txtCedulaEliminar = QtWidgets.QLineEdit(parent=self.tbEliminar)
        self.txtCedulaEliminar.setObjectName("txtCedulaEliminar")
        self.gridLayout_4.addWidget(self.txtCedulaEliminar, 1, 0, 1, 1)
        self.lblNombreApellidoEliminar = QtWidgets.QLabel(parent=self.tbEliminar)
        self.lblNombreApellidoEliminar.setObjectName("lblNombreApellidoEliminar")
        self.gridLayout_4.addWidget(self.lblNombreApellidoEliminar, 2, 0, 1, 1)
        self.lblCedulaEliminar = QtWidgets.QLabel(parent=self.tbEliminar)
        self.lblCedulaEliminar.setObjectName("lblCedulaEliminar")
        self.gridLayout_4.addWidget(self.lblCedulaEliminar, 0, 0, 1, 1)
        self.btnEliminar = QtWidgets.QPushButton(parent=self.tbEliminar)
        self.btnEliminar.setObjectName("btnEliminar")
        self.gridLayout_4.addWidget(self.btnEliminar, 6, 0, 1, 1)
        self.tbEncargado.addTab(self.tbEliminar, "")
        self.tbListar = QtWidgets.QWidget()
        self.tbListar.setObjectName("tbListar")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tbListar)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.jgdListaEncargados = QtWidgets.QTableWidget(parent=self.tbListar)
        self.jgdListaEncargados.setObjectName("jgdListaEncargados")
        self.jgdListaEncargados.setColumnCount(0)
        self.jgdListaEncargados.setRowCount(0)
        self.gridLayout_5.addWidget(self.jgdListaEncargados, 0, 0, 1, 1)
        self.tbEncargado.addTab(self.tbListar, "")
        self.gridLayout.addWidget(self.tbEncargado, 0, 0, 1, 1)

        self.retranslateUi(Ui_IngresoEncargado)
        self.tbEncargado.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Ui_IngresoEncargado)

    def retranslateUi(self, Ui_IngresoEncargado):
        _translate = QtCore.QCoreApplication.translate
        Ui_IngresoEncargado.setWindowTitle(_translate("Ui_IngresoEncargado", "Encargado"))
        self.lblClaveIngresar.setText(_translate("Ui_IngresoEncargado", "Contraseña"))
        self.txtClaveIngresar.setPlaceholderText(_translate("Ui_IngresoEncargado", "Ingrese constraseña"))
        self.cbxMostrarClaveIngresar.setText(_translate("Ui_IngresoEncargado", "Mostrar contraseña"))
        self.txtCedulaIngresar.setPlaceholderText(_translate("Ui_IngresoEncargado", "Ingrese cédula"))
        self.txtDireccionIngresar.setPlaceholderText(_translate("Ui_IngresoEncargado", "Ingrese dirección"))
        self.lblNombreApellidoIngresar.setText(_translate("Ui_IngresoEncargado", "Nombre y Apellido"))
        self.lblCedulaIngresar.setText(_translate("Ui_IngresoEncargado", "Cédula"))
        self.txtNombreApellidoIngresar.setPlaceholderText(_translate("Ui_IngresoEncargado", "Ingrese nombre y apellido"))
        self.lblDireccionIngresar.setText(_translate("Ui_IngresoEncargado", "Dirección"))
        self.btnIngresarEncargado.setText(_translate("Ui_IngresoEncargado", "Ingresar encargado"))
        self.btnLimpiarCampos.setText(_translate("Ui_IngresoEncargado", "Limpiar campos"))
        self.tbEncargado.setTabText(self.tbEncargado.indexOf(self.tbIngresar), _translate("Ui_IngresoEncargado", "Ingresar"))
        self.lblNombreApellidoModificar.setText(_translate("Ui_IngresoEncargado", "Nombre y Apellido"))
        self.lblDireccionModificar.setText(_translate("Ui_IngresoEncargado", "Dirección"))
        self.lblClaveModificar.setText(_translate("Ui_IngresoEncargado", "Contraseña"))
        self.lblCedulaModificar.setText(_translate("Ui_IngresoEncargado", "Cédula"))
        self.txtCedulaModificar.setPlaceholderText(_translate("Ui_IngresoEncargado", "Ingrese cédula"))
        self.cbxMostrarClaveModificar.setText(_translate("Ui_IngresoEncargado", "Mostrar contraseña"))
        self.btnGuardarCambios.setText(_translate("Ui_IngresoEncargado", "Guardar cambios"))
        self.tbEncargado.setTabText(self.tbEncargado.indexOf(self.tbModificar), _translate("Ui_IngresoEncargado", "Modificar"))
        self.lblDireccionEliminar.setText(_translate("Ui_IngresoEncargado", "Dirección"))
        self.txtCedulaEliminar.setPlaceholderText(_translate("Ui_IngresoEncargado", "Ingrese cédula"))
        self.lblNombreApellidoEliminar.setText(_translate("Ui_IngresoEncargado", "Nombre y Apellido"))
        self.lblCedulaEliminar.setText(_translate("Ui_IngresoEncargado", "Cédula"))
        self.btnEliminar.setText(_translate("Ui_IngresoEncargado", "Eliminar encargado"))
        self.tbEncargado.setTabText(self.tbEncargado.indexOf(self.tbEliminar), _translate("Ui_IngresoEncargado", "Eliminar"))
        self.tbEncargado.setTabText(self.tbEncargado.indexOf(self.tbListar), _translate("Ui_IngresoEncargado", "Listar"))
