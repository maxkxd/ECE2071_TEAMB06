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
            timeout=2
        )
        print("Port connected...")
        #time.sleep(3)
        return ser

    except serial.serialutil.SerialException:
        print("Error: Port not found")
        sys.exit()

def transmit_state(ser, state):
    ser.write(bytes([state]))

def get_input(msg, type = int):

    value = 0
    invalidInput = True

    while (invalidInput):
        response = input(f"{msg}")

        try:
            value = type(response)
            invalidInput = False
        except ValueError:
            print("Invalid input\n")

    return value