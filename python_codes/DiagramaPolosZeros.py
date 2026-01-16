import numpy as np
import matplotlib.pyplot as plt

L = 3
alpha_vec = [1, 3]

plt.figure(figsize=(10, 4))

theta = np.linspace(0, 2 * np.pi, 400)
unit_circle_x = np.cos(theta)
unit_circle_y = np.sin(theta)

for i, alpha in enumerate(alpha_vec, start=1):
    numerator = [1]
    denominator = [1] + [0] * (L - 1) + [-alpha]

    zeros = np.roots(numerator)
    poles = np.roots(denominator)

    plt.subplot(1, len(alpha_vec), i)

    # Círculo unitário
    plt.plot(unit_circle_x, unit_circle_y, 'k--', linewidth=1)

    # Polos e zeros
    plt.scatter(np.real(zeros), np.imag(zeros), marker='o', s=80)
    plt.scatter(np.real(poles), np.imag(poles), marker='x', s=80)

    # Eixos
    plt.axhline(0)
    plt.axvline(0)
    plt.grid(True)

    # Escala correta
    plt.gca().set_aspect('equal', adjustable='box')

    plt.title(f'Diagrama de Polos e Zeros\nα = {alpha}')
    plt.xlabel('Parte Real')
    plt.ylabel('Parte Imaginária')

plt.tight_layout()
plt.show()