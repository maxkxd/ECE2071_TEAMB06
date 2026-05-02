import numpy as np
import sys
import utils as utils
import CLI as CLI
import processing as proc

def main():
    #initialising stm
    port = utils.find_port()
    ser = utils.init_port(port)


    #initialising states
    exitProgram = False
    idle = 0

    # start main loop
    while not exitProgram:

        mode = CLI.fetch_mode()

        # std recording
        if mode == 0:
            # switch stm to std recording mode
            utils.transmit_state(ser, mode+1)

            # sampling routine
            recordTime = CLI.fetch_record_time()
            elapsedTime, data = proc.collect_data(ser, recordTime)
            data = proc.normalise_data(data)
            sampleRate = int(len(data)/elapsedTime)

            # set stm back to default state
            utils.transmit_state(ser, idle)

            print(elapsedTime)
            print(len(data))
            print(sampleRate)
            
            # hardcoded -> write to .wav file
            proc.write_to_wav(data, sampleRate)

        elif mode == 1:

            utils.transmit_state(ser, mode+1)

            # keyboard interrupt used to exit us mode -> possibly fix this
            try:
                # collect data
                elapsedTime, data = proc.collect_data_us(ser)

            except KeyboardInterrupt:
                # set stm back to default state
                utils.transmit_state(ser, idle)

                data = proc.normalise_data(data)
                sampleRate = int(len(data)/elapsedTime)

                # hardcoded -> write to .wav file
                proc.write_to_wav(data, sampleRate)

                print(f"samples = {len(data)}")
                print(f"sample rate = {sampleRate}")
        
        elif mode == 2:
            exitProgram = True
            print("exiting")
            ser.close()

if __name__ == "__main__":
    main()
    sys.exit()
        