import ArduinoController
import sys
import LoginWindow
from PyQt5 import QtCore, QtGui, QtWidgets

vendorID = None
productID = None

controller = ArduinoController.ArduinoController("Nano")

windows = ["login_window.ui", "main_window.ui", "settings_window.ui"]

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = LoginWindow.LoginWindow(windows)
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()