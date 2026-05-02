# This is a temporary solution...
# This file will run 5 minute audio samples and determine the results for sampling
# in std mode

import sys
# caution: path[0] is reserved for script path (or '' in REPL)
sys.path.insert(1, './src/ECE2071_COMP')

import utils as utils
import processing as proc

#import src.ECE2071_COMP.utils as utils
#import src.ECE2071_COMP.processing as proc
import numpy as np

def run_test():

    port = utils.find_port()
    ser = utils.init_port(port)

    tests = 10
    totalTime = 300 #second

    totalSamples = np.zeros(tests)
    sampleRates = np.zeros(tests)
    sampleTimes = np.zeros(tests)

    for i in range(tests):
        utils.transmit_state(ser, 1)
        elapsed, data = proc.collect_data(ser, totalTime)

        utils.transmit_state(ser, 0)

        sampleRate = int(len(data)/elapsed)

        totalSamples[i] = len(data)
        sampleRates[i] = sampleRate
        sampleTimes[i] = elapsed

    # printing out results
    print(f"Mean sample rate: {np.mean(sampleRates)}")
    print(f"Median sample rate: {np.median(sampleRates)}")
    print(f"Sample rate max: {sampleRates.max()}")
    print(f"Sample rate min: {sampleRates.min()}")
    print(f"Sample rate range: {sampleRates.max()-sampleRates.min()}")

if __name__=="__main__":
    run_test()
