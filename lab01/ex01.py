# https://cs.unibuc.ro/~crusu/ps/Procesarea%20Semnalelor%20(PS)%20-%20Laborator%2001.pdf

import numpy as np
import matplotlib.pyplot as plt

t0 = np.arange(0, 0.03, 0.0005)
x0 = np.cos(520 * np.pi * t0 + np.pi / 3)
y0 = np.cos(280 * np.pi * t0 - np.pi / 3)
z0 = np.cos(120 * np.pi * t0 + np.pi / 3)

fs = 200
t1 = np.arange(0, 0.03, 1 / fs)
x1 = np.cos(520 * np.pi * t1 + np.pi / 3)
y1 = np.cos(280 * np.pi * t1 - np.pi / 3)
z1 = np.cos(120 * np.pi * t1 + np.pi / 3)


fig0, axs = plt.subplots(3)
fig0.suptitle("b)")
axs[0].plot(t0, x0)
axs[0].set_title("x(t)")
axs[0].set_xlabel("t (s)")
axs[0].set_ylabel("x(t)")
axs[1].plot(t0, y0)
axs[1].set_title("y(t)")
axs[1].set_xlabel("t (s)")
axs[1].set_ylabel("y(t)")
axs[2].plot(t0, z0)
axs[2].set_title("z(t)")
axs[2].set_xlabel("t (s)")
axs[2].set_ylabel("z(t)")

fig1, axs = plt.subplots(3)
fig1.suptitle("c)")
axs[0].stem(t1, x1)
axs[0].set_title("x[t]")
axs[0].set_xlabel("t (s)")
axs[0].set_ylabel("x[t]")
axs[1].stem(t1, y1)
axs[1].set_title("y[t]")
axs[1].set_xlabel("t (s)")
axs[1].set_ylabel("y[t]")
axs[2].stem(t1, z1)
axs[2].set_title("z[t]")
axs[2].set_xlabel("t (s)")
axs[2].set_ylabel("z[t]")

plt.tight_layout()
plt.savefig("ex01.eps", format="eps")
plt.show()