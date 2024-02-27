import numpy as np
import matplotlib.pyplot as plt

# Calculating the sampling period
T = 1 / 1600

# Over a period of two seconds (start 0, end 2, sampling rate is 1/1600Hz)
sampling_period = np.arange(0, 2, T)

# Function
sampled_signal = 4+2*np.sin(2*np.pi*100*sampling_period)

# Number of samples
N = len(sampling_period)

# Compute fast fourier transform
fft = np.fft.fft(sampled_signal)

# Generate array of frequency bins with the length of the signal and the sampling period
freqs = np.fft.fftfreq(N, T)

# Calculating the power spectrum
S = np.abs(fft)**2/N

# Plotting the graph
plt.figure()
plt.plot(freqs, S)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.xlim(-400, 400)
plt.title('Double-sided frequency spectrum')
plt.grid(True)
plt.show()

sampled_signal_2 = 2*np.sin(2*np.pi*100*sampling_period) + 5*np.cos(2*np.pi*1200*sampling_period)
N2 = len(sampled_signal_2)
fft2 = np.fft.fft(sampled_signal_2)
freqs2 = np.fft.fftfreq(N2, T)
S2 = np.abs(fft2)**2/N2

plt.figure()
plt.plot(freqs2, S2)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Power")
plt.xlim(-600, 600)
plt.title('Double-trouble')
plt.grid(True)
plt.show()

# Square wave
fs_sw = 1000
T_sw = 1/fs_sw
t_sw = np.arange(0, 0.5, T)
sampled_signal_sw = 2 * np.sign(np.sin(2 * np.pi * 50 * t_sw))

# Plotting the time domain signal
plt.plot(t_sw, sampled_signal_sw)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude (V)')
plt.title('50 Hz Square Waveform')
plt.grid(True)
plt.show()

N_sw = len(t_sw)
fft_sw = np.fft.fft(sampled_signal_sw)
freqs_sw = np.fft.fftfreq(N_sw, T_sw)

magnitude = 2/N_sw * np.abs(fft_sw[:N//2])

plt.plot(freqs_sw, magnitude)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.title('Frequency Spectrum of 50 Hz Square Wave')
plt.grid(True)
plt.xlim(0, 500)  # Limit x-axis for better visibility
plt.show()
