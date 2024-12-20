import numpy as np
import matplotlib.pyplot as plt


def plot_time_domain(sampling_period, sampled_signal, x_lim):
    plt.plot(sampling_period, sampled_signal)
    plt.xlabel('Time in seconds')
    plt.ylabel('Sampled Signal Amplitude')
    plt.title('Sampled Signal Over 200 milliseconds at 1600Hz')
    plt.xlim(0, x_lim)
    plt.show()


def plot_freq(freq, mag, title, freq_range=None):
    plt.plot(freq, mag)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude")
    if freq_range is not None:
        plt.xlim(freq_range)
    plt.title(title)
    plt.grid(True)
    plt.show()


def fast_fourier_transform(signal, sampling_rate):
    yf = np.fft.fft(signal)
    N = len(signal)
    xf = np.fft.fftfreq(N, sampling_rate)
    magnitude_spectrum = np.abs(yf)
    return xf, magnitude_spectrum


def main():
    fs = 1600
    T = 1 / fs
    sampling_period = np.arange(0, 2, T)
    sampled_signal = 4 + 2 * np.sin(2 * np.pi * 100 * sampling_period)
    plot_time_domain(sampling_period, sampled_signal, 0.2)
    xf, magnitude_spectrum = fast_fourier_transform(sampled_signal, T)
    plot_freq(xf, magnitude_spectrum, 'Double-sided frequency spectrum', freq_range=(-800, 800))


if __name__ == '__main__':
    main()
