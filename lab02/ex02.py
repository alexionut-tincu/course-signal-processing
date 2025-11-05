# https://cs.unibuc.ro/~crusu/ps/Procesarea%20Semnalelor%20(PS)%20-%20Laborator%2002.pdf

import numpy as np
import matplotlib.pyplot as plt

fs = 8000
t = np.arange(0, 0.01, 1/fs)
A = 1.0
f = 500.0
phases = [0.0, np.pi/6, np.pi/3, np.pi/2]
signals = [A * np.sin(2 * np.pi * f * t + p) for p in phases]
plt.figure(figsize=(8,3))
for s in signals:
    plt.plot(t, s)
plt.title('Four phases of the same unit-amplitude sinusoid')
plt.tight_layout()
plt.savefig('eps02a.eps', format='eps')
plt.show()

x = signals[0]
SNRs = [0.1, 1, 10, 100]
noisy_signals = []
gammas = []
for S in SNRs:
    z = np.random.normal(size=x.shape)
    gamma = np.sqrt(np.linalg.norm(x)**2 / (S * np.linalg.norm(z)**2))
    noisy_signals.append(x + gamma * z)
    gammas.append(gamma)

plt.figure(figsize=(8,6))
for i, ns in enumerate(noisy_signals):
    plt.subplot(4,1,i+1)
    plt.plot(t, ns)
    plt.title(f'Noisy signal, SNR={SNRs[i]}, gamma={gammas[i]:.4g}')
plt.tight_layout()
plt.savefig('ex02b.eps', format='eps')
plt.show()
