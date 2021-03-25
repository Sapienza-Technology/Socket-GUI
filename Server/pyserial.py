# with open('/sys/class/thermal/thermal_zone0/temp') as thermalZone:
#                        sensorsData["cpuTemp"] = float(thermalZone.read()) / 1000
import sys
import threading
from time import sleep

import serial
from serial.tools.list_ports import comports as listSerialPorts


class serialConnection():
    def __init__(self):
        self.serialPort = None
        self.serialConnected = False
        self.startSerialConnection_th()
        self.serialLoopReceive_th()

    def serialLoopReceive(self):
        while True:
            if not self.serialConnected:
                sleep(2)
            else:
                response = self.serialRead()
                # receive

    def serialPrint(self, message):
        # global serialPort
        if self.serialPort is not None and self.serialPort.isOpen:
            try:
                self.serialPort.write(message.encode('utf-8'))
                self.serialPort.flush()
            except:
                print("Could not print serial message!")
        else:
            print("Serial port not initialized, attempted writing")

    def serialRead(self):
        # global serialPort
        if self.serialPort is not None and self.serialPort.isOpen:
            try:
                return self.serialPort.readline().decode("utf-8").replace("\n", "").replace("\r", "")
            except:
                print("Could not read serial message!")
                return ""
        else:
            print("Serial port not initialized, attempted reading")
            return ""

    def runSerialConnection(self):
        # global serialPort
        # global serverRunning
        while not self.serialConnected:
            try:
                print("Scanning serial ports...")
                # print(listSerialPorts())
                # for port in listSerialPorts():
                # print("Trying with " + port.name)
                for port in listSerialPorts():
                    print("Trying with " + port.name)
                    try:
                        self.serialPort = serial.Serial(port=port.device, baudrate=9600, timeout=5)
                        # rtscts=True, dsrdtr=True, exclusive=True) chiedere a Marco :)
                    except:
                        print(port.name + " unavailable.")
                        continue
                    sleep(2)
                    self.serialPrint("$W\n")
                    sleep(0.3)
                    response = self.serialRead()
                    print(response)
                    if response == "$W":
                        print(port.device + " connected.")
                        self.serialConnected = True
                        break
                    else:
                        print("No answer from " + port.name)
                        self.serialPort.close()
                        self.serialPort = None
            except:
                print("Unexpected error:", sys.exc_info())
                print("Unexpected error, Arduino and the sensors are now disconnected!")
                # addUserMessage("Server", "Errore inaspettato, sensori e Arduino si sono disconnessi!", MessageType.ERROR)
                if self.serialPort is not None:
                    self.serialPort.close()
                    self.serialPort = None
            sleep(1)
        print("Sensors-refresh thread stopped")

    def startSerialConnection_th(self):
        th_serialConn = threading.Thread(target=self.runSerialConnection, args=())
        th_serialConn.start()

    def serialLoopReceive_th(self):
        th_receive = threading.Thread(target=self.serialLoopReceive, args=())
        th_receive.start()


try:
    connection = serialConnection()
except KeyboardInterrupt:
    exit()
