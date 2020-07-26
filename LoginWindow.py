from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
import sys

class LoginWindow(QtWidgets.QMainWindow):

	# Constructor
	def __init__(self, windows):
		super().__init__()

		self.windows = windows
		self.current_window = 0

		self.load_ui()
		self.connect_all()

		self.show()

	# Loads widgets from the QDesigner .ui file
	def load_ui(self):
		uic.loadUi("ui\\" + self.windows[self.current_window], self)

	# Connects all ui widgets to respective handlers
	def connect_all(self):
		self.btn_login.clicked.connect(self.btn_login_handler)


	def changeWindow(self):
		uic.loadUi(self.windows[self.current_window],self)

	def btn_login_handler(self):
		if(self.check_user_credentials()):
			print("Moving to the next screen")

	# Checks if the credentials are correct and logs in the user
	# TODO
	# In the future, this method should compare the credentials to info in a database
	def check_user_credentials(self):
		username = self.lineEdit_user
		password = self.lineEdit_pass

		return True