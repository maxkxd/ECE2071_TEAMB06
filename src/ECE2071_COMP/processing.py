import numpy as np
import serial
import serial.tools.list_ports
import sys
import time
import wave
import csv
import matplotlib.pyplot as plt
import config

SAMPLE_RATE = config.Config.sample_rate


def collect_data(ser, recordTime):
    # Flush stale data, then wait briefly for STM to begin streaming
    ser.reset_input_buffer()
    time.sleep(0.2)
    ser.reset_input_buffer()

    start = time.time()
    samples = []
    leftover = b''   # carry-over byte when a read returns an odd number of bytes

    while (time.time() - start) < recordTime:
        chunk = leftover + ser.read(128)   # read a larger chunk at once
        leftover = b''
        i = 0
        while i + 1 < len(chunk):
            frame = int.from_bytes(chunk[i:i+2], byteorder='little')
            if (frame & 0xF) == 0xA:
                samples.append(frame >> 4)
                i += 2
            else:
                i += 1   # re-sync: advance one byte and try again
        if len(chunk) % 2 == 1:
            leftover = chunk[-1:]

    data = np.array(samples, dtype=np.uint16)
    elapsed = time.time() - start
    print(f"Collected {len(data)} samples in {elapsed:.2f}s  (~{int(len(data)/elapsed)} sps)")
    return data


def collect_data_us(ser):
    """Collect samples until Ctrl-C. The STM only sends when object is in range."""
    samples = []
    print("Recording (Ctrl-C to stop)...")
    try:
        while True:
            raw_data = ser.read(2)
            if len(raw_data) == 2:
                frame = int.from_bytes(raw_data, byteorder='little')
                if (frame & 0xF) == 0xA:
                    samples.append(frame >> 4)
    except KeyboardInterrupt:
        pass

    data = np.array(samples, dtype=np.uint16)
    print(f"Collected {len(data)} samples")
    return data


def normalise_data(data):
    """Convert 12-bit unsigned ADC values to 16-bit signed PCM.
    Uses the measured mean as the DC midpoint so any microphone bias level works.
    """
    if len(data) == 0:
        return data
    data = data.astype(np.float32)
    data -= np.mean(data)          # remove actual DC (not assumed 2048)
    data = (data / 2048.0) * 32767.0  # keep same gain as a properly biased input
    return np.clip(data, -32768, 32767).astype(np.int16)


def write_to_wav(data, filename='output.wav'):
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(SAMPLE_RATE)
        wf.writeframes(data.tobytes())
    print(f"Saved {filename}")


def write_to_png(data, filename='output.png'):
    t = np.arange(len(data)) / SAMPLE_RATE
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(t, data, linewidth=0.5)
    ax.set_title('Audio Waveform')
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Amplitude')
    ax.grid(True)
    fig.tight_layout()
    fig.savefig(filename, dpi=150)
    plt.close(fig)
    print(f"Saved {filename}")


def write_to_csv(data, filename='output.csv'):
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([f'sample_rate={SAMPLE_RATE}'])
        for sample in data:
            writer.writerow([sample])
    print(f"Saved {filename}")


def write_to_fft(data, filename='output_fft.png'):
    freqs = np.fft.rfftfreq(len(data), d=1/SAMPLE_RATE)
    magnitude = np.abs(np.fft.rfft(data))
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(freqs, 20 * np.log10(magnitude + 1e-9), linewidth=0.5)
    ax.set_title('FFT Spectrum')
    ax.set_xlabel('Frequency (Hz)')
    ax.set_ylabel('Magnitude (dB)')
    ax.set_xlim(0, SAMPLE_RATE / 2)
    ax.grid(True)
    fig.tight_layout()
    fig.savefig(filename, dpi=150)
    plt.close(fig)
    print(f"Saved {filename}")


def save_outputs(data, output_flags):
    """Write selected outputs. output_flags is a set of strings: 'wav','png','csv','fft'."""
    if 'wav' in output_flags:
        write_to_wav(data)
    if 'png' in output_flags:
        write_to_png(data)
    if 'csv' in output_flags:
        write_to_csv(data)
    if 'fft' in output_flags:
        write_to_fft(data)