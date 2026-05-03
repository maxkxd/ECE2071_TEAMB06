# This is a temporary solution...
# This file will run 5 minute audio samples and determine the results for sampling
# in std mode

import time
import sys
# caution: path[0] is reserved for script path (or '' in REPL)
sys.path.insert(1, './src/ECE2071_COMP')

import utils as utils
import processing as proc

#import src.ECE2071_COMP.utils as utils
#import src.ECE2071_COMP.processing as proc
import numpy as np

def run_std_test():

    port = utils.find_port()
    ser = utils.init_port(port)

    tests = 5
    totalTime = 300 #seconds

    sampleRates = np.zeros(tests)

    print("---START---")
    for i in range(tests):
        print(f"---TEST {i}---")
        utils.transmit_state(ser, 1)
        elapsed, data = proc.collect_data(ser, totalTime)

        utils.transmit_state(ser, 0)

        sampleRate = int(len(data)/elapsed)

        sampleRates[i] = sampleRate

        print(f"\tsample rate: {sampleRate}")
        print(f"\ttotal samples: {len(data)}")
        print(f"\telapsed: {elapsed:.2f}\n")

    print("---END TESTS---\n\n---RESULTS---")
    # printing out results
    print(f"Mean sample rate: {np.mean(sampleRates)}")
    print(f"Median sample rate: {np.median(sampleRates)}")
    print(f"Sample rate max: {sampleRates.max()}")
    print(f"Sample rate min: {sampleRates.min()}")
    print(f"Sample rate range: {sampleRates.max()-sampleRates.min()}")

    print("---END---")


# to run this test, set the distance to 1000 or some arbitrarily large value
def run_us_test():
    port = utils.find_port()
    ser = utils.init_port(port)

    print("---START---\n")
    utils.transmit_state(ser, 1)
    start = time.time()
    data = proc.collect_data_us(ser)
    elapsed = time.time() - start

    utils.transmit_state(ser, 0)

    sampleRate = int(len(data)/elapsed)

    print(f"\ttotal samples: {len(data)}")
    print(f"\telapsed: {elapsed:.2f}")
    print(f"\tsample rate: {sampleRate}\n")

    print("---END---")


if __name__=="__main__":
    run_us_test()
