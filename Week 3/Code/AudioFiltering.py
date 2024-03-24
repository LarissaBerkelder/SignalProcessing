import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.io.wavfile import write


def read_audio_file():
    # Reading the audio file
    sample_rate, audio_data = wavfile.read("week3_sample_dist.wav")
    return sample_rate, audio_data


def fast_fourier_transform(sample_rate, audio_data):
    yf = np.fft.fft(audio_data)
    # Compute the frequency bins
    N = len(audio_data)
    xf = np.fft.fftfreq(N, 1/sample_rate)[:N // 2]
    # Calculating the power spectrum
    magnitude_spectrum = 2.0 / N * np.abs(yf[:N // 2])
    return xf, magnitude_spectrum


def filter_audio(audio_data, alpha):
    # difference equation: y[n] = exp(-T/tau) y[n-1] + (1 - exp(-T/tau)) x[n-1]
    filtered_audio = np.zeros_like(audio_data)
    for n in range(1, len(audio_data)):
        filtered_audio[n] = alpha * filtered_audio[n-1] + (1 - alpha) * audio_data[n-1]
    return filtered_audio


def calculate_magnitude_index(f_interference, xf, magnitude_spectrum):
    index = np.argmin(np.abs(xf - f_interference))
    magnitude_interference = magnitude_spectrum[index]
    return magnitude_interference


def calculate_db_suppressed(magnitude_interference, magnitude_interference_filtered):
    db = 10 * np.log10(magnitude_interference ** 2 / magnitude_interference_filtered ** 2)
    print(f"Decibel interference signal suppressed: {db} dB")

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
    sample_rate, audio_data = read_audio_file()

    xf, magnitude_spectrum = fast_fourier_transform(sample_rate, audio_data)
    plot_graph(xf, magnitude_spectrum, sample_rate, "Frequency Spectrum")

    f_interference = xf[np.argmax(magnitude_spectrum)]

    # Variables for the filter
    T = 1 / sample_rate
    fc = f_interference / 2
    tau = 1 / (2 * np.pi * fc)
    alpha = np.exp(-T / tau)

    filtered_audio = filter_audio(audio_data, alpha)
    xf_filtered, magnitude_spectrum_filtered = fast_fourier_transform(sample_rate, filtered_audio)
    plot_graph(xf_filtered, magnitude_spectrum_filtered, sample_rate, "Frequency Spectrum Filtered")

    calculate_db_suppressed(
        calculate_magnitude_index(f_interference, xf, magnitude_spectrum),
        calculate_magnitude_index(f_interference, xf_filtered, magnitude_spectrum_filtered))


if __name__ == '__main__':
    main()

