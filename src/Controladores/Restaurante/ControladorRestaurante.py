from PyQt6 import QtWidgets
from src.Vistas.Restaurante.Ui_Main import Ui_Main
from src.Modelos.Restaurante.Restaurante import Restaurante
from src.Modelos.Usuario.GestionUsuarios import GestionUsuarios
from src.Controladores.Restaurante.ControladorCarta import ControladorCarta
from src.Controladores.Comida.ControladorProducto import ControladorProducto
from src.Controladores.Usuario.ControladorAcercaDe import ControladorAcercaDe
from src.Controladores.Restaurante.ControladorReserva import ControladorReserva
from src.Controladores.Restaurante.ControladorReportes import ControladorReportes
from src.Controladores.Comida.ControladorIngrediente import ControladorIngrediente
from src.Controladores.Usuario.ControladorGestionEncargado import ControladorGestionEncargado
from src.Controladores.Restaurante.ControladorDiaDisponibilidad import ControladorDiaDisponibilidad
from src.Controladores.Restaurante.ControladorInformacionRestaurante import ControladorInformacionRestaurante
class ControladorRestaurante(QtWidgets.QMainWindow, Ui_Main):

    def __init__(self, isAdmin, parent= None):
        super(ControladorRestaurante, self).__init__(parent)
        self.setupUi(self)

        self.init_ventana(isAdmin)
        self.init_actions()
        self.restaurante = Restaurante.getInstance()

    def init_ventana(self, isAdmin):
        if not isAdmin:
            self.jmbCarta.setEnabled(False)
            self.jmbPersonal.setEnabled(False)
            self.jmbReportes.setEnabled(False)
            self.jmbConfiguracion.setEnabled(False)

    def init_actions(self):
        self.jmbSalir.triggered.connect(self.salir)
        self.jmbCartaIngresar.triggered.connect(lambda: self.init_controlador('controlador_carta')(0))
        self.jmbReservaIngresar.triggered.connect(lambda: self.init_controlador('controlador_reserva')(0))
        self.jmbProductoIngresar.triggered.connect(lambda: self.init_controlador('controlador_producto')(0))
        self.jmbIngredienteIngresar.triggered.connect(lambda: self.init_controlador('controlador_ingrediente')(0))
        self.jmbPersonalIngresar.triggered.connect(lambda: self.init_controlador('controlador_gestion_encargado')(0))
        self.jmbDisponibilidadIngresar.triggered.connect(lambda: self.init_controlador('controlador_dia_disponibilidad')(0))

        self.jmbCartaModificar.triggered.connect(lambda: self.init_controlador('controlador_carta')(1) if self.restaurante.cartas else self.dialogo_informacion('Informacion', 'Cartas aun no ingresadas al sistema'))
        self.jmbReservaModificar.triggered.connect(lambda: self.init_controlador('controlador_reserva')(1) if self.restaurante.reservas else self.dialogo_informacion('Informacion', 'Reservas aun no ingresadas al sistema'))
        self.jmbProductoModificar.triggered.connect(lambda: self.init_controlador('controlador_producto')(1) if self.restaurante.productos else self.dialogo_informacion('Informacion', 'Productos, aun no ingresados al sistema'))
        self.jmbIngredienteModificar.triggered.connect(lambda: self.init_controlador('controlador_ingrediente')(1) if self.restaurante.ingredientes else self.dialogo_informacion('Informacion', 'Ingredientes aun no ingresados al sistema'))
        self.jmbPersonalModificar.triggered.connect(lambda: self.init_controlador('controlador_gestion_encargado')(1))
        self.jmbDisponibilidadModificar.triggered.connect(lambda: self.init_controlador('controlador_dia_disponibilidad')(1) if self.restaurante.dias_disponibilidad else self.dialogo_informacion('Informacion', 'Disponibilidad aun no ingresada al sistema'))


        self.jmbCartaEliminar.triggered.connect(lambda: self.init_controlador('controlador_carta')(2) if self.restaurante.cartas else self.dialogo_informacion('Informacion', 'Cartas aun no ingresadas al sistema'))
        self.jmbReservaEliminar.triggered.connect(lambda: self.init_controlador('controlador_reserva')(2) if self.restaurante.reservas else self.dialogo_informacion('Informacion', 'Reservas aun no ingresadas al sistema'))
        self.jmbProductoEliminar.triggered.connect(lambda: self.init_controlador('controlador_producto')(2) if self.restaurante.productos else self.dialogo_informacion('Informacion', 'Productos, aun no ingresados al sistema'))
        self.jmbIngredienteEliminar.triggered.connect(lambda: self.init_controlador('controlador_ingrediente')(2) if self.restaurante.ingredientes else self.dialogo_informacion('Informacion', 'Ingredientes aun no ingresados al sistema'))
        self.jmbPersonalEliminar.triggered.connect(lambda: self.init_controlador('controlador_gestion_encargado')(2))
        self.jmbDisponibilidadEliminar.triggered.connect(lambda: self.init_controlador('controlador_dia_disponibilidad')(2) if self.restaurante.dias_disponibilidad else self.dialogo_informacion('Informacion', 'Disponibilidad aun no ingresada al sistema'))


        self.jmbCartaListar.triggered.connect(lambda: self.init_controlador('controlador_carta')(3) if self.restaurante.cartas else self.dialogo_informacion('Informacion', 'Cartas aun no ingresadas al sistema'))
        self.jmbReservaListar.triggered.connect(lambda: self.init_controlador('controlador_reserva')(3) if self.restaurante.reservas else self.dialogo_informacion('Informacion', 'Reservas aun no ingresadas al sistema'))
        self.jmbProductoListar.triggered.connect(lambda: self.init_controlador('controlador_producto')(3) if self.restaurante.productos else self.dialogo_informacion('Informacion', 'Productos, aun no ingresados al sistema'))
        self.jmbIngredienteListar.triggered.connect(lambda: self.init_controlador('controlador_ingrediente')(3) if self.restaurante.ingredientes else self.dialogo_informacion('Informacion', 'Ingredientes aun no ingresados al sistema'))
        self.jmbPersonalListar.triggered.connect(lambda: self.init_controlador('controlador_gestion_encargado')(3))
        self.jmbDisponibilidadListar.triggered.connect(lambda: self.init_controlador('controlador_dia_disponibilidad')(3) if self.restaurante.dias_disponibilidad else self.dialogo_informacion('Informacion', 'Disponibilidad aun no ingresada al sistema'))


        self.jmbAcercaDe.triggered.connect(lambda: self.init_controlador('controlador_acerca_de')())
        self.jtbReservaIngresar.triggered.connect(lambda: self.init_controlador('controlador_reserva')(0))
        self.jmbConfiguracion.triggered.connect(lambda: self.init_controlador('controlador_configuracion')())
        self.jtbDisponibilidadIngresar.triggered.connect(lambda: self.init_controlador('controlador_dia_disponibilidad')(0))

        self.jmbReporteDinero.triggered.connect(lambda: self.init_controlador('controlador_reportes')('reporte_dinero'))
        self.jmbReporteProducto.triggered.connect(lambda: self.init_controlador('controlador_reportes')('reporte_productos'))
        self.jmbReporteConcurrencia.triggered.connect(lambda: self.init_controlador('controlador_reportes')('reporte_concurrencia'))

    def init_controlador(self, tipo_controlador):
        self.hide()
        def ingrediente(seccion):
            self.ventana = ControladorIngrediente(self.show, seccion)
            self.ventana.show()
        def producto(seccion):
            self.ventana = ControladorProducto(self.show, seccion)
            self.ventana.show()
        def carta(seccion):
            self.ventana = ControladorCarta(self.show, seccion)
            self.ventana.show()
        def dia_disponibilidad(seccion):
            self.ventana = ControladorDiaDisponibilidad(self.show, seccion)
            self.ventana.show()
        def encargado(seccion):
            self.ventana = ControladorGestionEncargado(self.show, seccion)
            self.ventana.show()
        def reserva(seccion):
            self.ventana = ControladorReserva(self.show, seccion)
            self.ventana.show()
        def configuracion():
            self.ventana = ControladorInformacionRestaurante(self.show)
            self.ventana.show()
        def acerca_de():
            self.ventana = ControladorAcercaDe(self.show)
            self.ventana.show()

        def reportes(tipo_reporte):
            self.ventana = ControladorReportes(self.show, tipo_reporte)
            self.ventana.show()


        controladores = {'controlador_ingrediente': ingrediente, 'controlador_producto': producto,
                         'controlador_carta': carta, 'controlador_dia_disponibilidad': dia_disponibilidad,
                         'controlador_gestion_encargado': encargado, 'controlador_reserva': reserva,
                         'controlador_configuracion': configuracion, 'controlador_acerca_de': acerca_de,
                         'controlador_reportes': reportes}

        return controladores[tipo_controlador]

    def dialogo_informacion(self, titulo, cadena):
        QtWidgets.QMessageBox.information(self,titulo, cadena)

    def salir(self):
        GestionUsuarios.getInstance().guardar()
        Restaurante.getInstance().guardar_restaurante()
        self.close()

    def closeEvent(self, event):
        GestionUsuarios.getInstance().guardar()
        Restaurante.getInstance().guardar_restaurante()







