import serial
import serial.tools.list_ports_windows
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

    def connectToController(self):
        # Gets a list of all serial ports
        ports = list(serial.tools.list_ports_windows.comports())
        targetPID = int(list(self.boardInfo.values())[0][1],16)

        # Searches for a serial device with the PID of the target arduino board
        for port in ports:
            if(port.pid == targetPID):
                print("Found {} board".format(list(self.boardInfo.keys())[0]))
                self.arduino = serial.Serial(port=port.name, baudrate=9600, timeout=.1)

        # Notifies user if no board was found
        if not hasattr(self,'arduino'):
            print("No board found")

    def readFromArduino(self):
        data = self.arduino.readLine()[:2]
        if data:
            print(data)

board = ArduinoController("uno")
board.connectToController()