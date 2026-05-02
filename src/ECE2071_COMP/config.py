import serial
import serial.tools.list_ports
import sys
import src.ECE2071_COMP.utils as utils

# I thought to add a cfg file to handle globl vars if the program expands
# ignore for now
class Config:
    recordTime = 0
    mode = "idle"
    output = ".wav"

    def __init__(self, baudrate=115200, port="None", ser="None"):
        self.__baudrate = baudrate
        self.__port = port
        self.__ser = ser
    
    def get_port(self):
        return self.__port
    
    def get_ser(self):
        return self.__ser

    def get_port(self):
        return self.__port
    
    def get_baudrate(self):
        return self.__baudrate
