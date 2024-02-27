import numpy as np
import matplotlib.pyplot as plt


def plot_time(time, signal, title):
    plt.plot(time, signal)
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.title(title)
    plt.grid(True)
    plt.show()


def plot_freq(freq, mag, title, freq_range=None):
    plt.figure()
    plt.plot(freq, mag)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude")
    if freq_range is not None:
        plt.xlim(freq_range)
    plt.title(title)
    plt.grid(True)
    plt.show()


def ignition():
    T = 1 / 1600
    x = np.arange(0, 2, T)
    y = 4 + 2 * np.sin(2 * np.pi * 100 * x)

    # Compute the FFT
    yf = np.fft.fft(y)

    # Compute the frequency bins
    N = len(y)
    xf = np.fft.fftfreq(N, T)

    # Calculating the power spectrum
    magnitude_spectrum = np.abs(yf)

    # Plot
    plot_freq(xf, magnitude_spectrum, 'Double-sided frequency spectrum', freq_range=(-800, 800))


def double_trouble():
    T = 1 / 1600
    x = np.arange(0, 2, T)
    y = 2 * np.sin(2 * np.pi * 100 * x) + 5 * np.cos(2 * np.pi * 1200 * x)

    # Compute the FFT
    yf = np.fft.fft(y)

    # Compute the frequency bins
    N = len(y)
    xf = np.fft.fftfreq(N, T)

    # Calculating the power spectrum
    magnitude_spectrum = np.abs(yf)

    # Plot
    plot_freq(xf, magnitude_spectrum, 'Double-trouble', freq_range=(-800, 800))


def square_wave():
    T = 1 / 1600
    x = np.arange(0, 0.04, T)
    y = 2 * np.sign(np.sin(2 * np.pi * 50 * x))

    # Plot for time domain
    plot_time(x, y, '50 Hz Square Waveform Time domain')

    # Compute the FFT
    yf = np.fft.fft(y)

    # Compute the frequency bins
    N = len(y)
    xf = np.fft.fftfreq(N, T)

    # Calculating the power spectrum
    magnitude_spectrum = np.abs(yf)

    # Plot
    plot_freq(xf, magnitude_spectrum, '50 Hz Square Waveform Frequency domain', freq_range=(-800, 800))


def main():
    ignition()
    double_trouble()
    square_wave()


if __name__ == '__main__':
    main()
