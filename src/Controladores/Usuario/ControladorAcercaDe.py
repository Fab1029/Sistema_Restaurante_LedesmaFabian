from PyQt6 import QtWidgets
from src.Vistas.Usuario.Ui_AcercaDe import Ui_AcercaDe

class ControladorAcercaDe(QtWidgets.QWidget, Ui_AcercaDe):
    def __init__(self, controlador_anterior, parent= None):
        super(ControladorAcercaDe, self).__init__(parent)
        self.setupUi(self)

        self.controlador_anterior = controlador_anterior

    def closeEvent(self, event):
        self.controlador_anterior()