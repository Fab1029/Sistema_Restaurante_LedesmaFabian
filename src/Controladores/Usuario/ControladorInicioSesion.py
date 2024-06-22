from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication
from src.Vistas.Usuario.Ui_InicioSesion import Ui_InicioSesion
from src.Modelos.Usuario.GestionUsuarios import GestionUsuarios


class ControladorInicioSesion(QtWidgets.QWidget, Ui_InicioSesion):
    def __init__(self, controlador_restaurante, parent= None):
        super(ControladorInicioSesion, self).__init__(parent)
        self.setupUi(self)

        #Centrar pantalla
        self.move(QApplication.primaryScreen().availableGeometry().center() - self.rect().center())

        self.init_componentes()

        self.init_action()
        self.controlador_restaurante = controlador_restaurante
        self.gestion_encargados = GestionUsuarios.getInstance()


    def init_componentes(self):
        self.cbxMostrarClave.setChecked(False)

    def init_action(self):
        self.btnEntrar.clicked.connect(self.entrar_action)
        self.cbxMostrarClave.checkStateChanged.connect(lambda: self.mostrar_clave_action(1)() if self.cbxMostrarClave.isChecked() else self.mostrar_clave_action(2)())

    def mostrar_clave_action(self, accion):
        def mostrar_clave():
            self.txtClave.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        def ocultar_clave():
            self.txtClave.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

        accion_mostrar_clave = {1: mostrar_clave, 2: ocultar_clave}

        return accion_mostrar_clave[accion]

    def entrar_action(self):
        if self.txtUsuario.text() and self.txtClave.text() and self.gestion_encargados.encargados.get(self.txtUsuario.text(), None) is not None and self.gestion_encargados.encargados[self.txtUsuario.text()].password == self.txtClave.text():

            self.controlador_restaurante(True).show() if self.txtUsuario.text() == 'admin' else self.controlador_restaurante(False).show()
            self.close()
        else:
            self.dialogo_informacion('Alerta', 'Usuario o contraseña no validos')

    def dialogo_informacion(self, titulo, cadena):
        QtWidgets.QMessageBox.information(self, titulo, cadena)




