from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic

import SettingsWindow
import ArduinoController as ard

class MainWindow(QtWidgets.QMainWindow):
	def __init__(self, windows):
		super().__init__()

		self.windows = windows
		self.currentWindow = 0

		self.load_ui()

		self.show()

	def load_ui(self):
		uic.loadUi("ui\\" + self.windows[self.currentWindow],self)
		self.connect_all()

	def connect_all(self):
		self.btn_connect.clicked.connect(self.btn_connect_handler)
		self.btn_send.clicked.connect(self.btn_send_handler)
		
		self.action_settings.triggered.connect(self.action_settings_handler)
	
	# ------------- HANDLERS --------------------- #
	def btn_connect_handler(self):
		print("Connecting to board")
		self.arduino = ard.ArduinoController("uno")
		self.arduino.connect()
		print("Connected to board")

	def btn_send_handler(self):
		print("Sending Message...")
		message = QtWidgets
		self.txt_ardMsg.setPlainText(self.arduino.read())
		print("Message Received")


	def action_settings_handler(self):
		self.settings_window = SettingsWindow.SettingsWindow(self.windows)