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
SAMPLE_RATE = 10000
samples = []
counter = 0


start = time.time()

for _ in range(10*SAMPLE_RATE):
    #counter += 1
    #print(counter)
    point = ser.read(1)
    if point:
        samples.append(point[0])
    else:
        print("corrupted")
        time.sleep(0.1)

elapsed = time.time() - start
print(elapsed)
data = np.array(samples)

data = (data-data.min())/(data.max() - data.min())
data = data*255
data = data.astype(np.uint8)

print(len(data))

#for point in data:
#    print(point)

with wave.open('output.wav', 'wb') as wf:
    wf.setnchannels(1)
    wf.setsampwidth(1)
    wf.setframerate(SAMPLE_RATE)
    wf.writeframes(data.tobytes())

print("write complete")