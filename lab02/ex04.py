# https://cs.unibuc.ro/~crusu/ps/Procesarea%20Semnalelor%20(PS)%20-%20Laborator%2002.pdf

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

fs = 8000
t = np.arange(0, 0.01, 1/fs)
s1 = np.sin(2 * np.pi * 300 * t)
s2 = signal.sawtooth(2 * np.pi * 300 * t)
s_sum = s1 + s2
plt.figure(figsize=(8,6))
plt.subplot(3,1,1)
plt.plot(t, s1)
plt.title('Sinusoid')
plt.subplot(3,1,2)
plt.plot(t, s2)
plt.title('Sawtooth')
plt.subplot(3,1,3)
plt.plot(t, s_sum)
plt.title('Sum')
plt.tight_layout()
plt.savefig('ex04.eps', format='eps')
plt.show()
