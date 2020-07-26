import usb.core
import usb.util
import json

class ArduinoController:

    def __init__(self, boardName):
        self.boardName = boardName

        with open("C:\\Users\\Suheyb Aden\\Desktop\\Code\\Python\\Practice\\USB_Devices.json") as f:
            data = json.load(f)
            boardIDs = data.get("Arduino")
            for board in boardIDs:
                if board.get(boardName) != None:
                    self.boardInfo = board       

    def connectToController(self):
        boardIDs = self.boardInfo.get(self.boardName)
        dev = usb.core.find(boardIDs[0], boardIDs[1])

        # if dev == None:
        #     print("*************ERROR")
        #     raise ValueError("Device not found")

        # dev.set_configuration()

        # cfg = dev.get_active_configuration()
        # intf = cfg[(0,0)]
        
        # ep = usb.util.find_descriptor(
        #     intf,
        #     # match the first OUT endpoint
        #     custom_match = \
        #     lambda e: \
        #         usb.util.endpoint_direction(e.bEndpointAddress) == \
        #         usb.util.ENDPOINT_OUT)

        # assert ep is not None

        # # write the data
        # ep.write('test')