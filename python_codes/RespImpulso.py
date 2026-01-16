import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":

    L = 3
    alpha = 0.7

    n_samples = 10 * L

    h = np.zeros(n_samples)
    h[0] = 1

    for n in range(1, n_samples):
        if n >= L:
            h[n] = alpha * h[n - L]

    plt.stem(np.arange(n_samples), h)
    plt.title("Resposta ao Impulso h[n]")
    plt.xlabel("n")
    plt.ylabel("h[n]")
    plt.grid(True)
    plt.show()