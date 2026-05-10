import sys
import utils
import CLI
import processing as proc

IDLE = 0
STD  = 1
USTRG = 2

def main():
    port = utils.find_port()
    ser  = utils.init_port(port)

    while True:
        mode = CLI.fetch_mode()

        if mode == 0:
            # Manual Recording Mode
            utils.transmit_state(ser, STD)
            record_time = CLI.fetch_record_time()
            output_flags = CLI.fetch_output_formats()

            raw = proc.collect_data(ser, record_time)
            utils.transmit_state(ser, IDLE)

            data = proc.normalise_data(raw)
            proc.save_outputs(data, output_flags)

        elif mode == 1:
            # Distance Trigger Mode
            utils.transmit_state(ser, USTRG)
            output_flags = CLI.fetch_output_formats()

            raw = proc.collect_data_us(ser)
            utils.transmit_state(ser, IDLE)

            data = proc.normalise_data(raw)
            proc.save_outputs(data, output_flags)

        elif mode == 2:
            print("Exiting.")
            ser.close()
            break

        elif mode == 3:
            help_sel = CLI.help_window()
            CLI.help_proc(help_sel)


if __name__ == "__main__":
    main()
    sys.exit()
        