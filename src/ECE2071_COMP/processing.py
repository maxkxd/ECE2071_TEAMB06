import numpy as np
import serial
import serial.tools.list_ports
import sys
import time
import wave
import pandas as pd
import matplotlib.pyplot as plt
# split file up in the future gng >:)

def collect_data(ser, recordTime):
    time.sleep(1)
    start = time.time()
    elapsed = 0
    samples = []

    # collecting data
    while elapsed < recordTime:
        sample = ser.read(1)
        if sample:
            samples.append(sample[0])
        elapsed = time.time() - start
    
    # reshaping to 1xN array
    data = np.array(samples)

    print(data.shape)
    
    return elapsed, data


# NOTE: This needs to be better implemented, I did a rough job on this
def collect_data_us(ser):
    start = time.time()
    samples = []

    # collecting data
    try:
        while True:
            sample = ser.read(1)
            if sample:
                samples.append(sample[0])
            else:
                print("stop")

    except KeyboardInterrupt:
        # reshaping to 1xN array
        elapsedTime = time.time() - start
        data = np.array(samples)
        return elapsedTime, data

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

def write_to_csv(data, sampleRate):
    data_array = np.frombuffer(data, dtype=np.uint8)
    data_frame = pd.DataFrame(data_array, columns=[f'Data - Sample Rate: {sampleRate}'])
    data_frame.to_csv('output.csv', index=False)

def write_to_png(data, sampleRate):
    data_array = np.frombuffer(data, dtype=np.uint8)
    num_samples = len(data_array)
    time_array = np.linspace(0, num_samples/sampleRate, num_samples)
    
    plt.figure()
    plt.plot(time_array, data_array)
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.title("Plot of ADC Voltage Samples over Time")
    plt.savefig('output.png')
    plt.close()
