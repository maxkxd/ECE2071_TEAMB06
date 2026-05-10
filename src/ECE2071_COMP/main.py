import numpy as np
import sys
import utils as utils
import CLI as CLI
import processing as proc
import config

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
        outputType = CLI.fetch_output()

        # std recording
        if mode == 0:
            # switch stm to std recording mode
            utils.transmit_state(ser, mode+1)

            # sampling routine
            recordTime = CLI.fetch_record_time()
            elapsedTime, samples = proc.collect_data(ser, recordTime)
            data = np.array(samples)
            data = proc.normalise_data(data)
            #sampleRate = int(len(data)/elapsedTime)

            # set stm back to default state
            utils.transmit_state(ser, idle)
            
            # write to certain data type
            if outputType == 0:
                proc.write_to_wav(data, 21770)
            elif outputType == 1:
                proc.write_to_csv(data, 21770)
            elif outputType == 2:
                proc.write_to_png(data, 21770)
            elif outputType == 3:
                continue
                

        elif mode == 1:

            utils.transmit_state(ser, mode+1)

            #collect data
            samples = proc.collect_data_us(ser)

            # set stm back to default state
            utils.transmit_state(ser, idle)

            # convert to np array
            data = np.array(samples)

            data = proc.normalise_data(data)
            #sampleRate = int(len(data)/elapsedTime)

            # write to certain data type
            if outputType == 0:
                proc.write_to_wav(data, 9140)
            elif outputType == 1:
                proc.write_to_csv(data, 9140)
            elif outputType == 2:
                proc.write_to_png(data, 9140)
            elif outputType == 3:
                continue
        
        elif mode == 2:
            exitProgram = True
            print("exiting")
            ser.close()

        elif mode == 3:

            help = CLI.help_window()
            CLI.help_proc(help)


if __name__ == "__main__":
    main()
    sys.exit()
        