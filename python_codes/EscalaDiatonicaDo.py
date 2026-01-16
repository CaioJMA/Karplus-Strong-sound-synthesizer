import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
from scipy.fft import fft

fs = 48000
D = 1  # duração (s)

notas = ['DO', 'RE', 'MI', 'FA', 'SOL', 'LA', 'SI']
frequencias = [262, 294, 330, 350, 392, 440, 494]
pentagrama = dict(zip(notas, frequencias))

def tom(Y, N, T):
    for i in range(N - T - 1):
        Y[i + T] = (Y[i] + Y[i + 1]) / 2.01
    return Y

def nota(D, fs, Fo):
    T = int(fs / Fo)
    x = (np.pi / 2) * np.random.rand(T) - 1
    N = int(D * fs)

    Y = np.zeros(N)
    Y[:T] = x
    Y = tom(Y, N, T)

    sd.play(Y, fs)
    sd.wait()
    return Y

def plot_spectro(Y, fs, nome):
    Y_fft = fft(Y)
    N = len(Y)
    f = np.arange(N) * fs / N / 1000
    mag = np.abs(Y_fft) / N

    plt.plot(f, mag)
    plt.title(f'Espectro da Nota {nome}')
    plt.xlabel('Frequência (kHz)')
    plt.ylabel('Magnitude')
    plt.grid()

for nota_nome in notas:
    Y = nota(D, fs, pentagrama[nota_nome])

    plt.figure(figsize=(8, 6))
    t = np.arange(len(Y)) / fs

    plt.subplot(2, 1, 1)
    plt.plot(t, Y)
    plt.title(f'Forma de Onda – {nota_nome}')
    plt.xlabel('Tempo (s)')
    plt.ylabel('Amplitude')

    plt.subplot(2, 1, 2)
    plot_spectro(Y, fs, nota_nome)

    plt.tight_layout()
    plt.show()