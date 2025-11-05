# https://cs.unibuc.ro/~crusu/ps/Procesarea%20Semnalelor%20(PS)%20-%20Laborator%2002.pdf

import numpy as np
import matplotlib.pyplot as plt

fs = 1000
t = np.arange(0, 0.05, 1/fs)
f = 50.0
x = np.sin(2 * np.pi * f * t)
x_decim = x[::4]
t_decim = t[::4]
x_decim_shift = x[1::4]
t_decim_shift = t[1::4]
plt.figure(figsize=(8,6))
plt.subplot(3,1,1)
plt.plot(t, x)
plt.title('Original sampled signal')
plt.subplot(3,1,2)
plt.stem(t_decim, x_decim)
plt.title('Decimated by 4 (starting at sample 0)')
plt.subplot(3,1,3)
plt.stem(t_decim_shift, x_decim_shift)
plt.title('Decimated by 4 (starting at sample 1)')
plt.tight_layout()
plt.savefig('ex07.eps', format='eps')
plt.show()
