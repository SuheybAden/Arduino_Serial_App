import serial
import serial.tools.list_ports_windows
import io

import json

class ArduinoController:

	def __init__(self, boardName):
		self.boardName = boardName.lower()

		with open("C:\\Users\\Suheyb Aden\\Desktop\\Code\\Python\\Practice\\USB_Devices.json") as f:
			data = json.load(f)
			boardIDs = data.get("arduino")
			for board in boardIDs:
				if board.get(boardName) != None:
					self.boardInfo = board

	def connect(self):
		# Gets a list of all serial ports
		ports = list(serial.tools.list_ports_windows.comports())
		targetPID = int(list(self.boardInfo.values())[0][1],16)

		# Searches for a serial device with the PID of the target arduino board
		for port in ports:
			if(port.pid == targetPID):
				print("Found {} board".format(list(self.boardInfo.keys())[0]))
				self.arduino = serial.Serial(port=port.device, baudrate=9600, timeout=.1)
				self.sio = io.TextIOWrapper(io.BufferedRWPair(self.arduino,self.arduino))

		# Notifies user if no board was found
		if not hasattr(self,'arduino'):
			print("No board found")

	def disconnect(self):
		pass

	def changeBoardType(self):
		pass

	# Reads string input from the com port
	def read(self, continuousRead=False):
		if continuousRead:
			self.sio.readline()
		elif serial.in_waiting:
			return self.sio.readline()

	# Reads binary input from the com port
	def readBytes(self, numBytes=0):
		if(numBytes):
			return self.arduino.read()

	def write(self):
		pass

	# Gets whether the board has been connected to or not yet
	def exists(self) -> bool:
		return hasattr(self, 'arduino')
		