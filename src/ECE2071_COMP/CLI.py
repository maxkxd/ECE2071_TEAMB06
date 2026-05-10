import utils as utils

# This file handles all CLI interactions

def fetch_record_time():
    msg = "How long to record for (seconds)?\n> "
    return utils.get_input(msg, float)


def fetch_output_formats():
    """Ask user which output formats they want. Returns a set of format strings."""
    print("\nSelect output format(s):")
    print("  1: WAV  (audio playback)")
    print("  2: PNG  (waveform plot)")
    print("  3: CSV  (raw data)")
    print("  4: FFT  (spectrum plot)")
    print("Enter numbers separated by spaces (e.g. '1 2'):")
    choices = input("> ").split()
    mapping = {'1': 'wav', '2': 'png', '3': 'csv', '4': 'fft'}
    selected = {mapping[c] for c in choices if c in mapping}
    if not selected:
        print("No valid selection — defaulting to WAV.")
        selected = {'wav'}
    return selected


def fetch_mode():
    msg = (
        "\n=== Mode Select ===\n"
        "0: Manual Recording Mode\n"
        "1: Distance Trigger Mode\n"
        "2: Exit\n"
        "3: Help\n"
        "> "
    )
    return utils.get_input(msg)


def help_window():
    msg = "Which mode do you want help with?\n0: Manual Recording\n1: Distance Trigger\n2: Exit help\n> "
    return utils.get_input(msg)


def help_standard():
    msg = (
        "Manual Recording Mode: enter a duration in seconds.\n"
        "The system records for that long, then saves your chosen formats.\n"
        "0: Back to help\n1: Back to mode select\n> "
    )
    return utils.get_input(msg)


def help_US():
    msg = (
        "Distance Trigger Mode: recording starts automatically when an object\n"
        "is detected within 10 cm and stops ~50 ms after it moves away.\n"
        "Press Ctrl-C to exit the mode early.\n"
        "0: Back to help\n1: Back to mode select\n> "
    )
    return utils.get_input(msg)


def help_proc(help):
    while True:
        if help == 0:
            help = help_standard()
            if help == 0:
                help = help_window()
            elif help == 1:
                break
        elif help == 1:
            help = help_US()
            if help == 0:
                help = help_window()
            elif help == 1:
                break
        elif help == 2:
            break
