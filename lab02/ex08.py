# https://cs.unibuc.ro/~crusu/ps/Procesarea%20Semnalelor%20(PS)%20-%20Laborator%2002.pdf

import numpy as np
import matplotlib.pyplot as plt

alpha = np.linspace(-np.pi/2, np.pi/2, 1001)
s = np.sin(alpha)
taylor = alpha
pade = (alpha - 7 * alpha**3 / 60) / (1 + alpha**2 / 20)
err_linear = np.abs(s - taylor)
err_pade = np.abs(s - pade)
plt.figure(figsize=(8,6))
plt.subplot(3,1,1)
plt.plot(alpha, s, label='sin(alpha)')
plt.plot(alpha, taylor, label='linear approx')
plt.legend()
plt.title('sin vs linear approx')
plt.subplot(3,1,2)
plt.plot(alpha, s, label='sin(alpha)')
plt.plot(alpha, pade, label='Pade approx')
plt.legend()
plt.title('sin vs Pade approx')
plt.subplot(3,1,3)
plt.semilogy(alpha, err_linear, label='|sin - linear|')
plt.semilogy(alpha, err_pade, label='|sin - Pade|')
plt.legend()
plt.title('Error (log scale)')
plt.tight_layout()
plt.savefig('ex08.eps', format='eps')
plt.show()
