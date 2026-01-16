import numpy as np
import sounddevice as sd
import time

def play_sound(x, alpha, L, fs, n_samples):

    y = np.zeros(n_samples)
    y[:L] = x

    for i in range(L, n_samples):
        y[i] = alpha * y[i - L]

    # soundsc equivalente (normalização automática)
    y = y / np.max(np.abs(y))

    sd.play(y, fs)
    sd.wait()

if __name__ == "__main__":

    fs = 48000
    duration = 2
    L = 100
    n_samples = duration * fs
    n = np.arange(L)

    # a) Senoide
    alpha_a = 0.995
    x_a = np.sin(2 * np.pi * n / L)

    # b) Triangular
    alpha_b = 1.0
    x_b = (2 * n / L) - 1

    # c) Quadrada
    alpha_c = 0.95
    x_c = np.concatenate([
        np.ones(L // 2),
        -np.ones(L // 2)
    ])

    # d) Aleatória (normal)
    alpha_d = 0.995
    x_d = np.random.randn(L)

    # Tocar os sinais
    play_sound(x_a, alpha_a, L, fs, n_samples)
    time.sleep(duration + 1)

    play_sound(x_b, alpha_b, L, fs, n_samples)
    time.sleep(duration + 1)

    play_sound(x_c, alpha_c, L, fs, n_samples)
    time.sleep(duration + 1)

    play_sound(x_d, alpha_d, L, fs, n_samples)
    time.sleep(duration + 1)