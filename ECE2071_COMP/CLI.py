
# This file handles all CLI interactions
def fetch_record_time():
    validInput = False
    time = 0.0
    while not validInput:
        timeStr = input("How long to record for?\n> ")
        try:
            time = float(timeStr)
            validInput = True
        except ValueError:
            print("Invalid input")

    print("recording...")
    return time

def fetch_output():
    output = input("How would you like to save the recording?\n> ")
    print("saving...")
    return output

def fetch_mode():
    mode = input("How would you like to record?")

    print("recording...")
    return mode