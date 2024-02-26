import numpy as np
import matplotlib.pyplot as plt

# Sampling frequency
fs = 1600
# Calculating the sampling period
T = 1 / fs
# Over a period of two seconds (start 0, end 2, sampling rate is 1/1600Hz)
sampling_period = np.arange(0, 2, T)

sampled_signal = 4+2*np.sin(2*np.pi*100*sampling_period)

plt.plot(sampling_period, sampled_signal)
plt.xlabel('Time in seconds')
plt.ylabel('Sampled Signal Amplitude')
plt.title('Sampled Signal Over 200 milliseconds at 1600Hz')
plt.xlim(0, 0.2)
plt.show()