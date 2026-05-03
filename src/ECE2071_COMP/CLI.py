import utils as utils

# This file handles all CLI interactions
def fetch_record_time():
    msg = "How long to record for?\n> "

    time = utils.get_input(msg, float)

    return time

def fetch_output():
    output = input("How would you like to save the recording?\n> ")

    print("saving...")

    return output

def fetch_mode():
    msg = "How would you like to record?\n0: Standard\n1: US triggered\n2: Exit\n3: Help\n> "

    mode = utils.get_input(msg)

    return mode

def help_window():
    msg = "Which mode do you want help with?\n0: Standard\n1: US triggered\n2: Exit help\n>"

    help = utils.get_input(msg)

    return help

def help_standard():
    msg = "The standard mode will ask you to specify how long you would like to record for\n0:Back to help\n1:Back to mode select\n>"

    help = utils.get_input(msg)

    return help

def help_US():
    msg = "The US triggered mode will record as long as the ultrasonic sensor detects something within 10cm\n0:Back to help\n1:Back to mode select\n>"

    help = utils.get_input()

    return help

def help_proc(help):
    #help loop
    while True:
        #help standard mode
        if help == 0:
            help = help_standard()
            if help == 0:
                continue
            elif help == 1:
                break
        #help US triggered mode
        elif help == 1:
            help = help_US()
            if help == 0:
                continue
            elif help == 1:
                break
        #return to mode select
        elif help == 2:
            break
