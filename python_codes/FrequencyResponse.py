from scipy.signal import freqz
import matplotlib.pyplot as plt
import numpy as np

L = 3
alpha = 0.7
fs = 1000

b = [1]
a = [1] + [0]*(L-1) + [-alpha]

w, H = freqz(b, a, worN=1024, fs=fs)
f = w / 1000

plt.figure()
plt.subplot(2, 1, 1)
plt.plot(f, np.abs(H))
plt.title('Magnitude |H(e^{jw})|')
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(f, np.angle(H))
plt.title('Fase θ(e^{jw})')
plt.grid()
plt.show()