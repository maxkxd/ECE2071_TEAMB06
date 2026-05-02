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
    msg = "How would you like to record?\n0: Standard\n1: US triggered\n2: Exit\n> "

    mode = utils.get_input(msg)

    return mode