import numpy as np
import serial
import serial.tools.list_ports
import sys
import time
import wave
# split file up in the future gng >:)

def collect_data(ser, recordTime):
    start = time.time()
    elapsed = 0
    samples = []

    # collecting data
    while elapsed < recordTime:
        sample = list(ser.read(1))
        if sample:
            samples.append(sample)
        elapsed = time.time() - start
    
    # reshaping to 1xN array
    data = np.array(samples)
    data = data.reshape(-1)
    
    return elapsed, data


# NOTE: This needs to be better implemented, I did a rough job on this
def collect_data_us(ser):
    start = time.time()
    samples = []
    elapsedOffset = 0

    # collecting data
    try:
        #samplingStopped = False;
        #pauseTimeStart = 0
        while True:
            sample = list(ser.read(1))
            if sample:
                samples.append(sample)
                if samplingStopped:
                   elapsedOffset += time.time() - pauseTimeStart
                   samplingStopped = False
            else:
                if not samplingStopped:
                   pauseTimeStart = time.time()
                   samplingStopped= True
    except KeyboardInterrupt:
        elapsed = time.time() - start# - elapsedOffset
        # reshaping to 1xN array
        data = np.array(samples)
        data = data.reshape(-1)
        
        return elapsed, data

def normalise_data(data):
    data = (data-data.min())/(data.max()-data.min())
    data = data*255
    data = data.astype(np.uint8)

    return data

def write_to_wav(data, sampleRate):
    with wave.open('output.wav', 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(1)
        wf.setframerate(sampleRate)
        wf.writeframes(data.tobytes())