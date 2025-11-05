# https://cs.unibuc.ro/~crusu/ps/Procesarea%20Semnalelor%20(PS)%20-%20Laborator%2002.pdf

import numpy as np
import matplotlib.pyplot as plt

fs = 8000
t = np.arange(0, 0.01, 1/fs)
A = 1.2
f = 440.0
x_sin = A * np.sin(2 * np.pi * f * t )
x_cos = A * np.cos(2 * np.pi * f * t - np.pi/2)
plt.figure(figsize=(8,4))
plt.subplot(2,1,1)
plt.plot(t, x_sin)
plt.title('Sine wave')
plt.subplot(2,1,2)
plt.plot(t, x_cos)
plt.title('Cosine wave')
plt.tight_layout()
plt.savefig('ex01.eps', format='eps')
plt.show()
