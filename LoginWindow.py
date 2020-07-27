from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic

import MainWindow

class LoginWindow(QtWidgets.QMainWindow):

	# Constructor
	def __init__(self, windows):
		super().__init__()

		self.windows = windows

		self.load_ui()

		self.show()

	# Sets up the ui
	def load_ui(self):
		uic.loadUi("ui\\" + self.windows[0], self)
		self.connect_all()

	# Connects all ui widgets to respective handlers
	def connect_all(self):
		self.btn_login.clicked.connect(self.btn_login_handler)

	def btn_login_handler(self):
		if(self.check_user_credentials()):
			self.windows.pop(0)
			self.mainWindow = MainWindow.MainWindow(self.windows)
			self.close()

	# Checks if the credentials are correct and logs in the user
	# TODO
	# In the future, this method should compare the credentials to info in a database
	def check_user_credentials(self):
		username = self.lineEdit_user.text()
		password = self.lineEdit_pass.text()

		return True
	
