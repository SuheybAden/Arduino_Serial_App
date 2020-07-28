from PyQt5 import QtCore, QtGui, QtWidgets
import sys

import LoginWindow

windows = ["login_window.ui", "main_window.ui", "settings_window.ui"]

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = LoginWindow.LoginWindow(windows)
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()