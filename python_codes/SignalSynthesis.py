import numpy as np
import matplotlib.pyplot as plt

def plot_response(x, alpha, L, n_samples, plot_title):

    y = np.zeros(n_samples)
    y[:L] = x

    for i in range(L, n_samples):
        y[i] = alpha * y[i - L]

    plt.figure()
    plt.stem(np.arange(n_samples), y)
    plt.title(f"Resposta ao Impulso: {plot_title}")
    plt.xlabel("n")
    plt.ylabel("y[n]")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":

    L = 100
    n_samples = 10 * L
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

    plot_response(x_a, alpha_a, L, n_samples, "Senoide")
    plot_response(x_b, alpha_b, L, n_samples, "Triangular")
    plot_response(x_c, alpha_c, L, n_samples, "Quadrada")
    plot_response(x_d, alpha_d, L, n_samples, "Aleatória")