import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
from scipy.fft import fft

fs = 48000
duration = 2
L = 100
n_samples = fs * duration
n = np.arange(L)

def generate_signal(x, alpha):
    y = np.zeros(n_samples)
    y[:L] = x
    for i in range(L, n_samples):
        y[i] = alpha * y[i - L]
    sd.play(y, fs)
    sd.wait()
    return y

def plot_spectrum(y):
    Y = fft(y)
    N = len(Y)
    f = np.arange(N) * fs / N / 1000

    plt.figure(figsize=(8, 6))
    plt.subplot(2, 1, 1)
    plt.plot(f, np.abs(Y))
    plt.title('Magnitude')
    plt.grid()

    plt.subplot(2, 1, 2)
    plt.plot(f, np.angle(Y))
    plt.title('Fase')
    plt.grid()
    plt.tight_layout()
    plt.show()

x_a = np.sin(2 * np.pi * n / L)
x_b = (2 * n / L) - 1
x_c = np.concatenate([np.ones(L//2), -np.ones(L//2)])
x_d = np.random.randn(L)

for x, alpha in [(x_a, 0.995), (x_b, 1.0), (x_c, 0.95), (x_d, 0.995)]:
    y = generate_signal(x, alpha)
    plot_spectrum(y)