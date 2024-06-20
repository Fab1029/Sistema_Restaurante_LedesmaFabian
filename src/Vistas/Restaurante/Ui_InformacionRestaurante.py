# Form implementation generated from reading ui file 'Ui_InformacionRestaurante.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_InformacionRestaurante(object):
    def setupUi(self, Ui_InformacionRestaurante):
        Ui_InformacionRestaurante.setObjectName("Ui_InformacionRestaurante")
        Ui_InformacionRestaurante.resize(1355, 768)
        Ui_InformacionRestaurante.setMinimumSize(QtCore.QSize(800, 600))
        Ui_InformacionRestaurante.setMaximumSize(QtCore.QSize(1366, 768))
        Ui_InformacionRestaurante.setStyleSheet("QWidget{\n"
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
"}")
        self.gridLayout = QtWidgets.QGridLayout(Ui_InformacionRestaurante)
        self.gridLayout.setObjectName("gridLayout")
        self.txtEmail = QtWidgets.QLineEdit(parent=Ui_InformacionRestaurante)
        self.txtEmail.setObjectName("txtEmail")
        self.gridLayout.addWidget(self.txtEmail, 16, 0, 1, 1)
        self.lblDireccion = QtWidgets.QLabel(parent=Ui_InformacionRestaurante)
        self.lblDireccion.setObjectName("lblDireccion")
        self.gridLayout.addWidget(self.lblDireccion, 13, 0, 1, 1)
        self.lblEmail = QtWidgets.QLabel(parent=Ui_InformacionRestaurante)
        self.lblEmail.setObjectName("lblEmail")
        self.gridLayout.addWidget(self.lblEmail, 15, 0, 1, 1)
        self.txtNombreRestaurante = QtWidgets.QLineEdit(parent=Ui_InformacionRestaurante)
        self.txtNombreRestaurante.setObjectName("txtNombreRestaurante")
        self.gridLayout.addWidget(self.txtNombreRestaurante, 3, 0, 1, 1)
        self.lblNombreRestaurante = QtWidgets.QLabel(parent=Ui_InformacionRestaurante)
        self.lblNombreRestaurante.setObjectName("lblNombreRestaurante")
        self.gridLayout.addWidget(self.lblNombreRestaurante, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(parent=Ui_InformacionRestaurante)
        self.label.setMinimumSize(QtCore.QSize(400, 700))
        self.label.setMaximumSize(QtCore.QSize(400, 700))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("./Vistas/logoRestaurante.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.txtTelefono = QtWidgets.QLineEdit(parent=Ui_InformacionRestaurante)
        self.txtTelefono.setMaxLength(10)
        self.txtTelefono.setObjectName("txtTelefono")
        self.gridLayout.addWidget(self.txtTelefono, 18, 0, 1, 1)
        self.txtDireccion = QtWidgets.QLineEdit(parent=Ui_InformacionRestaurante)
        self.txtDireccion.setObjectName("txtDireccion")
        self.gridLayout.addWidget(self.txtDireccion, 14, 0, 1, 1)
        self.btnGuardarCambios = QtWidgets.QPushButton(parent=Ui_InformacionRestaurante)
        self.btnGuardarCambios.setObjectName("btnGuardarCambios")
        self.gridLayout.addWidget(self.btnGuardarCambios, 20, 0, 1, 1)
        self.lblRuc = QtWidgets.QLabel(parent=Ui_InformacionRestaurante)
        self.lblRuc.setObjectName("lblRuc")
        self.gridLayout.addWidget(self.lblRuc, 4, 0, 1, 1)
        self.lblTelefono = QtWidgets.QLabel(parent=Ui_InformacionRestaurante)
        self.lblTelefono.setObjectName("lblTelefono")
        self.gridLayout.addWidget(self.lblTelefono, 17, 0, 1, 1)
        self.txtRazonSocial = QtWidgets.QLineEdit(parent=Ui_InformacionRestaurante)
        self.txtRazonSocial.setObjectName("txtRazonSocial")
        self.gridLayout.addWidget(self.txtRazonSocial, 12, 0, 1, 1)
        self.txtRuc = QtWidgets.QLineEdit(parent=Ui_InformacionRestaurante)
        self.txtRuc.setObjectName("txtRuc")
        self.gridLayout.addWidget(self.txtRuc, 10, 0, 1, 1)
        self.lblRazonSocial = QtWidgets.QLabel(parent=Ui_InformacionRestaurante)
        self.lblRazonSocial.setObjectName("lblRazonSocial")
        self.gridLayout.addWidget(self.lblRazonSocial, 11, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem, 19, 0, 1, 1)

        self.retranslateUi(Ui_InformacionRestaurante)
        QtCore.QMetaObject.connectSlotsByName(Ui_InformacionRestaurante)

    def retranslateUi(self, Ui_InformacionRestaurante):
        _translate = QtCore.QCoreApplication.translate
        Ui_InformacionRestaurante.setWindowTitle(_translate("Ui_InformacionRestaurante", "Información restaurante"))
        self.txtEmail.setPlaceholderText(_translate("Ui_InformacionRestaurante", "Ingrese email"))
        self.lblDireccion.setText(_translate("Ui_InformacionRestaurante", "Dirección"))
        self.lblEmail.setText(_translate("Ui_InformacionRestaurante", "Email"))
        self.txtNombreRestaurante.setPlaceholderText(_translate("Ui_InformacionRestaurante", "Ingrese nombre restaurante"))
        self.lblNombreRestaurante.setText(_translate("Ui_InformacionRestaurante", "Nombre del restaurante"))
        self.txtTelefono.setPlaceholderText(_translate("Ui_InformacionRestaurante", "Ingrese teléfono"))
        self.txtDireccion.setPlaceholderText(_translate("Ui_InformacionRestaurante", "Ingrese dirección restaurante"))
        self.btnGuardarCambios.setText(_translate("Ui_InformacionRestaurante", "Guardar cambios"))
        self.lblRuc.setText(_translate("Ui_InformacionRestaurante", "Ruc"))
        self.lblTelefono.setText(_translate("Ui_InformacionRestaurante", "Teléfono"))
        self.txtRazonSocial.setPlaceholderText(_translate("Ui_InformacionRestaurante", "Ingrese razón social"))
        self.txtRuc.setPlaceholderText(_translate("Ui_InformacionRestaurante", "Ingrese ruc"))
        self.lblRazonSocial.setText(_translate("Ui_InformacionRestaurante", "Razón social"))
