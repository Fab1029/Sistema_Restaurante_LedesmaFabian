import sys
from PyQt6 import QtWidgets
from src.Controladores.Usuario.ControladorInicioSesion import ControladorInicioSesion
from src.Controladores.Restaurante.ControladorRestaurante import ControladorRestaurante

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ControladorInicioSesion(ControladorRestaurante()).show()
    sys.exit(app.exec())




