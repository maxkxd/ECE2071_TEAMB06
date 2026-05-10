# I thought to add a cfg file to handle globl vars if the program expands
# ignore for now
class Config:
    # 32MHz / (0+1) / (725+1) = 44,077 Hz — closest achievable to 44.1kHz
    sample_rate = 44077
    baudrate = 921600

    # def __init__(self, baudrate=115200, port="None", ser="None"):
    #     self.__baudrate = baudrate
    #     self.__port = port
    #     self.__ser = ser
