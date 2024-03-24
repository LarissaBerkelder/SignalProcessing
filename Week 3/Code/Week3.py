import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile


def fast_fourier_transform(sample_rate, audio_data):
    yf = np.fft.fft(audio_data)
    # Compute the frequency bins
    N = len(audio_data)
    xf = np.fft.fftfreq(N, 1 / sample_rate)[:N // 2]
    # Calculating the power spectrum
    magnitude_spectrum = 2.0 / N * np.abs(yf[:N // 2])
    return xf, magnitude_spectrum


def plot_graph(xf, magnitude_spectrum, sample_rate, title):
    plt.figure()
    plt.plot(xf, magnitude_spectrum)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude")
    plt.xlim(0, sample_rate / 2)
    plt.title(title)
    plt.grid(True)
    plt.show()


def main():
    # Reading the audio file
    sample_rate, audio_data = wavfile.read("week3_sample_dist.wav")
    xf, magnitude_spectrum = fast_fourier_transform(sample_rate, audio_data)
    plot_graph(xf, magnitude_spectrum, sample_rate, "Frequency Spectrum")
    f_interference = xf[np.argmax(magnitude_spectrum)]
    print(f_interference)

if __name__ == '__main__':
    main()
