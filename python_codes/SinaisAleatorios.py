import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
import time
import math

def loop(FO, volume, pitch_shift, decay_factor):

    # Mapeamento das notas
    notas_n = ['LA', 'SI', 'DO', 'RE', 'MI', 'FA', 'SOL', 'SILENCIO']
    equivalente_n = [0, 2, 3, 5, 7, 8, 10, 91]
    mapeamento = dict(zip(notas_n, equivalente_n))

    notas = ['DO', 'RE', 'MI', 'FA', 'SOL', 'LA', 'SI']

    fs = 48000       # Frequência de amostragem
    D = 1.5          # Duração da nota (s)

    plt.figure(figsize=(8, 12))

    for i, nome_nota in enumerate(notas):
        nota_entero = mapeamento[nome_nota]

        Y = nota(D, fs, FO, nota_entero, volume, pitch_shift, decay_factor)

        t = np.arange(len(Y)) / fs

        plt.subplot(len(notas), 1, i + 1)
        plt.plot(t, Y)
        plt.xlabel("Time (s)")
        plt.ylabel("Amplitude")
        plt.title(f"Forma de Onda da Nota {nome_nota}")

    plt.tight_layout()
    plt.show()

def nota(D, fs, FO, nota_entero, volume, pitch_shift, decay_factor):

    Fo = FO * 2 ** ((nota_entero + pitch_shift) / 12)

    T = int(np.floor(fs / Fo))

    # Sinal inicial aleatório
    x = (math.pi / 2) * np.random.rand(T) - 1
    x *= volume

    N = int(D * fs)

    Y = np.zeros(N)
    Y[:T] = x

    Y = tom(Y, N, T, fs, decay_factor)

    return Y

def tom(Y, N, T, fs, decay_factor):

    for i in range(N - T - 1):
        Y[i + T] = (Y[i] + Y[i + 1]) / (2 + decay_factor)

    sd.play(Y, fs)
    sd.wait()
    time.sleep(0.3)

    return Y

if __name__ == "__main__":

    FO = 220            # Base de Lá
    volume = 1
    mudanca_pitch = 2
    decaimento_onda = 0.0001

    loop(FO, volume, mudanca_pitch, decaimento_onda)