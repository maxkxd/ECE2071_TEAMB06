import serial
import serial.tools.list_ports
import sys

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
            115200,
            timeout=1
        )
        print("Port connected...")
        #time.sleep(3)
        return ser

    except serial.serialutil.SerialException:
        print("Error: Port not found")
        sys.exit()