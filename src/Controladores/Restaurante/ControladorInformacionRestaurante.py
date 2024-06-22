from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QRegularExpression
from PyQt6.QtGui import QRegularExpressionValidator
from src.Modelos.Restaurante.Restaurante import Restaurante
from src.Vistas.Restaurante.Ui_InformacionRestaurante import Ui_InformacionRestaurante
class ControladorInformacionRestaurante(QtWidgets.QWidget, Ui_InformacionRestaurante):
    def __init__(self, controlador_anterior, parent = None):
        super(ControladorInformacionRestaurante, self).__init__(parent)
        self.setupUi(self)

        #Centrar pantalla
        self.move(QApplication.primaryScreen().availableGeometry().center() - self.rect().center())

        self.restaurante = Restaurante.getInstance()
        self.init_seccion()
        self.init_action()
        self.controlador_anterior = controlador_anterior


    def init_seccion(self):
        self.txtRuc.setText(self.restaurante.ruc)
        self.txtEmail.setText(self.restaurante.email)
        self.txtTelefono.setText(self.restaurante.telefono)
        self.txtDireccion.setText(self.restaurante.ubicacion)
        self.txtNombreRestaurante.setText(self.restaurante.nombre)
        self.txtRazonSocial.setText(self.restaurante.razon_social)
        self.txtTelefono.setValidator(QRegularExpressionValidator(QRegularExpression("[0-9]+"), self))

    def init_action(self):
        self.btnGuardarCambios.clicked.connect(self.guardar_cambios_action)

    def guardar_cambios_action(self):
        if self.txtNombreRestaurante.text() and self.txtRuc.text() and self.txtRazonSocial.text() and self.txtDireccion.text() and self.txtEmail.text() and self.txtTelefono.text():
            self.restaurante.ruc = self.txtRuc.text()
            self.restaurante.email = self.txtEmail.text()
            self.restaurante.telefono = self.txtTelefono.text()
            self.restaurante.ubicacion = self.txtDireccion.text()
            self.restaurante.nombre = self.txtNombreRestaurante.text()
            self.restaurante.razon_social = self.txtRazonSocial.text()
            self.dialogo_informacion('Éxito', 'Cambios guardados')
        else:
            self.dialogo_informacion('Alerta', 'No se realizaron los cambios')


    def dialogo_informacion(self, titulo, cadena):
        QtWidgets.QMessageBox.information(self,titulo, cadena)

    def closeEvent(self, event):
        self.controlador_anterior()
