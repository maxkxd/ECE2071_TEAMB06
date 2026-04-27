import numpy as np
import wave
import serial
import serial.tools.list_ports
import sys
import time
import math

def find_port():
    """Finds the port where the STM is connected


    Returns:
        string: the location of the port
    """
   
    ports = serial.tools.list_ports.comports()


    stmManufacturer = "STMicroelectronics"
   
    for port in ports:
        # Checking manufacturer - if true then that is the port we need
        if port.manufacturer == stmManufacturer:
            return port.device
   
    print("Port not found\nExiting...")
    sys.exit()


# connecting ports
def init_port(port):
    """Initialises the port for serial communication


    Args:
        port (string): the location of the port


    Returns:
        port: Initialised port for serial communication
    """


    try:
        ser = serial.Serial(
            port,
            115200
            #dsrdtr=False # claude
        )


        print("Port connected...")
        #time.sleep(3)
        return ser
   
    except serial.serialutil.SerialException:
        print("Error: Port not found")
        sys.exit()


# polling serial devices

port = find_port()
ser = init_port(port)
print(ser)

def main():
    samples = []
    counter = 0
    #samples = list(ser.read(5000))
    start = time.time()
    try:
        while(1):
            samples.append(list(ser.read(1)))
    except KeyboardInterrupt:
        elapsed = time.time() - start
        data = np.array(samples)
        data = data.reshape(-1)

        data = (data)/(data.max())
        data = data*255
        data = data.astype(np.uint8)
        sampleRate = int(len(data)/elapsed)
        with wave.open('output.wav', 'wb') as wf:
            wf.setnchannels(1)
            wf.setsampwidth(1)
            wf.setframerate(sampleRate)
            wf.writeframes(data.tobytes())

        print(len(data))
        print("write complete")


main()