import numpy as np
import wave
import serial
import serial.tools.list_ports
import sys
import time
import init as init
import CLI as CLI
import processing as proc

if __name__ == "__main__":
    try:
        # initialising stm
        port = init.find_port()
        ser = init.init_port(port)
        
        # set mode and record time
        #mode = CLI.fetch_mode()
        #recordTime = CLI.fetch_record_time()

        # collect input data
        elapsedTime, data = proc.collect_data(ser, 10)
        data = proc.normalise_data(data)

        # writing to .wav for now
        sampleRate = int(len(data)/elapsedTime)
        print(len(data))
        proc.write_to_wav(data, sampleRate)

    except KeyboardInterrupt:
        print("exiting")
        ser.close()
        sys.exit()
        