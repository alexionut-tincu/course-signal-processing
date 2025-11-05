# https://cs.unibuc.ro/~crusu/ps/Procesarea%20Semnalelor%20(PS)%20-%20Laborator%2002.pdf

import numpy as np
import matplotlib.pyplot as plt

fs = 8000
t = np.arange(0, 0.02, 1/fs)
x_fs2 = np.sin(2 * np.pi * (fs/2) * t)
x_fs4 = np.sin(2 * np.pi * (fs/4) * t)
x_dc = np.ones_like(t)
plt.figure(figsize=(8,6))
plt.subplot(3,1,1)
plt.plot(t, x_fs2)
plt.title('f = fs/2')
plt.subplot(3,1,2)
plt.plot(t, x_fs4)
plt.title('f = fs/4')
plt.subplot(3,1,3)
plt.plot(t, x_dc)
plt.title('f = 0 Hz')
plt.tight_layout()
plt.savefig('ex06.eps', format='eps')
plt.show()
