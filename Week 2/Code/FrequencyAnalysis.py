import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile


def main():
    # Reading the audio file
    sample_rate, audio_data = wavfile.read("week2_unknown_guitar_string.wav")
    T = 1 / sample_rate

    # Compute the FFT
    yf = np.fft.fft(audio_data)

    # Compute the frequency bins
    N = len(audio_data)
    xf = np.fft.fftfreq(N, T)[:N//2]

    # Calculating the power spectrum
    magnitude_spectrum = 2.0/N * np.abs(yf[:N//2])

    # Plot
    plt.figure()
    plt.plot(xf, magnitude_spectrum)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude")
    plt.xlim(0, 1000)
    plt.title("Single-Sided Frequency Spectrum")
    plt.grid(True)
    plt.show()

    # Print the peak frequency
    peak_freq = xf[np.argmax(magnitude_spectrum)]
    print(peak_freq, "Hz")


if __name__ == '__main__':
    main()
