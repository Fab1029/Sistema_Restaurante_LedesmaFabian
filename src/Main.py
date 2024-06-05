import sys

from PyQt6 import QtWidgets
from src.Controladores.Restaurante.ControladorMain import ControladorMain

if __name__ == '__main__':
    aplicacion = QtWidgets.QApplication(sys.argv)
    aplicacion_restaurante = ControladorMain()
    aplicacion_restaurante.show()
    aplicacion.exec()