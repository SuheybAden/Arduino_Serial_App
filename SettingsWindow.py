from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic

class SettingsWindow(QtWidgets.QDialog):
	
	# Constructor
	def __init__(self, windows):
		super().__init__()
		self.windows = windows
		self.load_ui()
		self.show()

	# Sets up the ui
	def load_ui(self):
		uic.loadUi("ui\\" + self.windows[1], self)
		self.connect_all()

	# Connects all ui widgets to respective handlers
	def connect_all(self):
		pass
