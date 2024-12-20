import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.io.wavfile import write
from scipy.signal import freqz


def fast_fourier_transform(sample_rate, audio_data):
    yf = np.fft.fft(audio_data)
    # Compute the frequency bins
    N = len(audio_data)
    xf = np.fft.fftfreq(N, 1 / sample_rate)[:N // 2]
    # Calculating the power spectrum
    magnitude_spectrum = 2.0 / N * np.abs(yf[:N // 2])
    return xf, magnitude_spectrum

def plot_frequency_response(b, a, sample_rate):
    w, h = freqz(b, a)
    frequencies = (w / (2 * np.pi)) * sample_rate

    plt.figure()
    plt.plot(frequencies, 20 * np.log10(abs(h)))  
    plt.title('Frequency Response of Notch Filter')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude (dB)')
    plt.grid()
    plt.show()

def single_sided_spectrum(sample_rate, audio_signal):
    # Compute FFT
    N = len(audio_signal)
    yf = np.fft.fft(audio_signal)
    xf = np.fft.fftfreq(N, 1 / sample_rate)[:N // 2]  
    magnitude = 2.0 / N * np.abs(yf[:N // 2])  

    # Plot
    plt.figure()
    plt.plot(xf, magnitude)
    plt.title('Single-Sided Spectrum of Filtered Audio Signal')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude')
    plt.grid()
    plt.show()
        
def notch_filter_with_for_loop(audio_data, b, a):
    filtered_audio = np.zeros_like(audio_data)

    for n in range(2, len(audio_data)):  
        filtered_audio[n] = (-a[1] * filtered_audio[n-1] - a[2] * filtered_audio[n-2] +
                             b[0] * audio_data[n] + b[1] * audio_data[n-1] + b[2] * audio_data[n-2])

    return filtered_audio

def calculate_db_suppressed(magnitude_interference, magnitude_interference_filtered):
    db = 10 * np.log10(magnitude_interference ** 2 / magnitude_interference_filtered ** 2)
    print(f"Decibel interference signal suppressed: {db} dB")

def calculate_magnitude_index(f_interference, xf, magnitude_spectrum):
    index = np.argmin(np.abs(xf - f_interference))
    magnitude_interference = magnitude_spectrum[index]
    return magnitude_interference    
    
def main():
    sample_rate, audio_data = wavfile.read("Week 4\Code\week3_sample_dist.wav")
    xf, magnitude_spectrum = fast_fourier_transform(sample_rate, audio_data)
    f_interference = xf[np.argmax(magnitude_spectrum)]
    print(f"Sample freq {sample_rate}")
    print(f"Interference freq {f_interference}")
    
    normalized_freq = (2*np.pi * f_interference) / sample_rate
    print(f"Normalized freq: {normalized_freq}")
    freq_dip = 0.9
    b = [1, -2 * np.cos(normalized_freq), 1]
    a = [1, -2 * freq_dip * np.cos(normalized_freq), freq_dip**2]
    
    plot_frequency_response(b, a, sample_rate)
    
    filtered_audio = notch_filter_with_for_loop(audio_data, b, a)
    write("Week 4\Code\week4_filtered_audio.wav", sample_rate, np.int16(filtered_audio))
    
    single_sided_spectrum(sample_rate, filtered_audio)

    xf_filtered, magnitude_spectrum_filtered = fast_fourier_transform(sample_rate, filtered_audio)

    calculate_db_suppressed(
        calculate_magnitude_index(f_interference, xf, magnitude_spectrum),
        calculate_magnitude_index(f_interference, xf_filtered, magnitude_spectrum_filtered))

    

if __name__ == '__main__':
    main()
