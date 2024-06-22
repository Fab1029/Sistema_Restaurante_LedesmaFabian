from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication
from src.Vistas.Usuario.Ui_AcercaDe import Ui_AcercaDe

class ControladorAcercaDe(QtWidgets.QWidget, Ui_AcercaDe):
    def __init__(self, controlador_anterior, parent= None):
        super(ControladorAcercaDe, self).__init__(parent)
        self.setupUi(self)

        #Centrar pantalla
        self.move(QApplication.primaryScreen().availableGeometry().center() - self.rect().center())

        self.controlador_anterior = controlador_anterior

    def closeEvent(self, event):
        self.controlador_anterior()