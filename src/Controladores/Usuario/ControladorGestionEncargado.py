from PyQt6 import QtWidgets
from PyQt6.QtCore import QRegularExpression
from PyQt6.QtGui import QRegularExpressionValidator
from src.Modelos.Usuario.Encargado import Encargado
from src.Modelos.Usuario.GestionUsuarios import GestionUsuarios
from src.Vistas.Usuario.Ui_GestionEncargado import Ui_GestionEncargado
class ControladorGestionEncargado(QtWidgets.QWidget, Ui_GestionEncargado):
    def __init__(self, controlador_anterior, seccion, parent= None):
        super(ControladorGestionEncargado, self).__init__(parent)
        self.setupUi(self)

        self.controlador_anterior = controlador_anterior
        self.gestion_usuarios = GestionUsuarios.getInstance()

        self.init_action()
        self.verificar_pestana()
        self.init_seccion(seccion)()

    def init_action(self):
        self.btnEliminar.clicked.connect(self.eliminar_encargado_action)
        self.btnLimpiarCampos.clicked.connect(lambda: self.init_seccion(0)())
        self.btnIngresarEncargado.clicked.connect(self.ingresar_encargado_action)
        self.tbEncargado.currentChanged.connect(lambda: self.init_seccion(self.tbEncargado.currentIndex())())

    def validar_cedula_ecuatoriana(self, cedula):
        return (lambda verificador: verificador == 0 and verificador == cedula[-1] or 10 - verificador == cedula[-1])(sum(list(map(lambda x: x - 9 if x > 9 else x, [valor_cedula * valor_mascara for valor_cedula, valor_mascara in zip(cedula, [2,1,2,1,2,1,2,1,2,1])]))[:9]) % 10)

    def eliminar_encargado_action(self):
        if self.txtCedulaEliminar.text() and self.gestion_usuarios.encargados.get(self.txtCedulaEliminar.text(), None) is not None:
            self.gestion_usuarios.encargados.pop(self.txtCedulaEliminar.text())
            self.dialogo_informacion('Exito', 'Eliminacion exitosa')
            self.init_seccion(2)()
            self.verificar_pestana()
        else:
            self.dialogo_informacion('Alerta', 'No se realizo la eliminacion')

    def ingresar_encargado_action(self):
        if self.txtCedulaIngresar.text() and self.txtNombreApellidoIngresar.text() and self.txtDireccionIngresar.text() and self.txtClaveIngresar.text() and self.validar_cedula_ecuatoriana(list(map(int, self.txtCedulaIngresar.text()))):
            self.gestion_usuarios.encargados[self.txtCedulaIngresar.text()] = Encargado(self.txtCedulaIngresar.text(), self.txtNombreApellidoIngresar.text(), self.txtDireccionIngresar.text(), self.txtClaveIngresar.text())
            self.dialogo_informacion('Exito', 'Ingreso exitoso')
            self.init_seccion(0)()
            self.verificar_pestana()

        else:
            self.dialogo_informacion('Alerta', 'Campos no validos')
    def modificar_encargado_action(self):
        if self.txtCedulaModificar.text() and self.txtNombreApellidoModificar.text() and self.txtDireccionModificar.text() and self.txtClaveModificar.text():
            self.gestion_usuarios.encargados[self.txtCedulaModificar.text()] = Encargado(self.txtCedulaModificar.text(), self.txtNombreApellidoModificar.text(), self.txtDireccionModificar.text(), self.txtClaveModificar.text())
            self.dialogo_informacion('Exito', 'Se han guardado los cambios')
            self.init_seccion(1)()
            self.verificar_pestana()
        else:
            self.dialogo_informacion('Alerta', 'Ingrese todos los campos')
    def listar_encargados_action(self):
        pass

    def init_seccion(self, seccion):
        self.desconectar_conexion()
        def ingresar():
            self.tbEncargado.setCurrentIndex(0)
            self.set_default_value(1)()
            self.txtCedulaIngresar.setValidator(QRegularExpressionValidator(QRegularExpression("[0-9]+"), self))
            self.conectar_conexion('password_ingresar')()
        def modificar():
            self.tbEncargado.setCurrentIndex(1)
            self.txtCedulaModificar.clear()
            self.set_default_value(2)()
            self.txtCedulaModificar.setValidator(QRegularExpressionValidator(QRegularExpression("[0-9]+"), self))

            self.conectar_conexion('cedula_modificar')()
            self.conectar_conexion('password_modificar')()

        def eliminar():
            self.tbEncargado.setCurrentIndex(2)
            self.txtCedulaEliminar.clear()
            self.set_default_value(3)()
            self.txtCedulaEliminar.setValidator(QRegularExpressionValidator(QRegularExpression("[0-9]+"), self))

            self.conectar_conexion('cedula_eliminar')()

        def listar():
            self.tbEncargado.setCurrentIndex(3)

        secciones = {0: ingresar, 1: modificar, 2: eliminar, 3: listar}

        return secciones[seccion]

    def set_default_value(self, accion):
        def ingresar():
            self.txtClaveIngresar.clear()
            self.txtCedulaIngresar.clear()
            self.txtDireccionIngresar.clear()
            self.txtNombreApellidoIngresar.clear()
            self.cbxMostrarClaveIngresar.setChecked(False)
        def modificar():
            self.txtClaveModificar.clear()
            self.txtDireccionModificar.clear()
            self.txtNombreApellidoModificar.clear()
            self.cbxMostrarClaveModificar.setChecked(False)
        def eliminar():
            self.txtDireccionEliminar.clear()
            self.txtNombreApellidoEliminar.clear()

        default = {1: ingresar, 2: modificar, 3: eliminar}

        return default[accion]



    def busqueda_cedula_action(self, accion):
        def cedula_modificar():
            if self.txtCedulaModificar.text() in self.gestion_usuarios.encargados:
                encargado = self.gestion_usuarios.encargados.get(self.txtCedulaModificar.text())
                self.txtNombreApellidoModificar.setText(encargado.nombre)
                self.txtDireccionModificar.setText(encargado.direccion)
                self.txtClaveModificar.setText(encargado.password)

        def cedula_eliminar():
            if self.txtCedulaEliminar.text() in self.gestion_usuarios.encargados:
                encargado = self.gestion_usuarios.encargados.get(self.txtCedulaEliminar.text())
                self.txtNombreApellidoEliminar.setText(encargado.nombre)
                self.txtDireccionEliminar.setText(encargado.direccion)


        busqueda = {1: cedula_modificar, 2: cedula_eliminar}
        return busqueda[accion]


    def dialogo_informacion(self, titulo, cadena):
        QtWidgets.QMessageBox.information(self,titulo, cadena)

    def verificar_pestana(self):
        if self.gestion_usuarios.encargados:
            [self.tbEncargado.setTabEnabled(indice, True) for indice in range(1,4)]
        else:
            self.tbEncargado.setCurrentIndex(0)
            [self.tbEncargado.setTabEnabled(indice, False) for indice in range(1,4)]

    def desconectar_conexion(self):
        try:
            self.cbxMostrarClaveIngresar.disconnect()
            self.cbxMostrarClaveModificar.disconnect()
            self.txtCedulaIngresar.textEdited.disconnect()
            self.txtCedulaModificar.textEdited.disconnect()
        except:
            pass

    def conectar_conexion(self, accion):
        def cedula_modificar():
            try:
                self.txtCedulaModificar.textEdited.connect(lambda: self.busqueda_cedula_action(1)() if len(self.txtCedulaModificar.text()) == 10 else self.set_default_value(2)())
            except:
                pass
        def cedula_eliminar():
            try:
                self.txtCedulaEliminar.textEdited.connect(lambda: self.busqueda_cedula_action(2)() if len(self.txtCedulaEliminar.text()) == 10 else self.set_default_value(3)())
            except:
                pass
        def password_ingresar():
            try:
                self.cbxMostrarClaveIngresar.checkStateChanged.connect(lambda: self.txtClaveIngresar.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal) if self.cbxMostrarClaveIngresar.isChecked() else self.txtClaveIngresar.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password))
            except:
                pass
        def password_modificar():
            try:
                self.cbxMostrarClaveModificar.checkStateChanged.connect(lambda: self.txtClaveModificar.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal) if self.cbxMostrarClaveModificar.isChecked() else self.txtClaveModificar.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password))
            except:
                pass

        conectar = {'cedula_modificar': cedula_modificar, 'cedula_eliminar': cedula_eliminar,
                    'password_ingresar': password_ingresar, 'password_modificar': password_modificar}

        return conectar[accion]

    def closeEvent(self, event):
        self.controlador_anterior()