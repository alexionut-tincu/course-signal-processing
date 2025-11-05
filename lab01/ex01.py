# https://cs.unibuc.ro/~crusu/ps/Procesarea%20Semnalelor%20(PS)%20-%20Laborator%2001.pdf

import numpy as np
import matplotlib.pyplot as plt

# (a) Time axis (using 0.0305 to include 0.03)
t = np.arange(0, 0.0305, 0.0005)

# (b) Defining the continuous signals
x_t = np.cos(520 * np.pi * t + np.pi / 3)
y_t = np.cos(280 * np.pi * t - np.pi / 3)
z_t = np.cos(120 * np.pi * t + np.pi / 3)

fig_cont, axs_cont = plt.subplots(3, 1, figsize=(10, 8))
fig_cont.suptitle('Ex 1(b): Continuous Signals')

# Plot x(t)
axs_cont[0].plot(t, x_t)
axs_cont[0].set_title('x(t) = cos(520πt + π/3)')
axs_cont[0].set_xlabel('Time (t)')
axs_cont[0].set_ylabel('Amplitude')

# Plot y(t)
axs_cont[1].plot(t, y_t)
axs_cont[1].set_title('y(t) = cos(280πt - π/3)')
axs_cont[1].set_xlabel('Time (t)')
axs_cont[1].set_ylabel('Amplitude')

# Plot z(t)
axs_cont[2].plot(t, z_t)
axs_cont[2].set_title('z(t) = cos(120πt + π/3)')
axs_cont[2].set_xlabel('Time (t)')
axs_cont[2].set_ylabel('Amplitude')

fig_cont.tight_layout(rect=[0, 0.03, 1, 0.96])
plt.savefig('ex01b.eps', format='eps')
plt.show()



# (c) Sample at 200 Hz
fs = 200.0
T = 1.0 / fs
t_discrete = np.arange(0, 0.0305, T)

# Generate the discrete signals
x_n = np.cos(520 * np.pi * t_discrete + np.pi / 3)
y_n = np.cos(280 * np.pi * t_discrete - np.pi / 3)
z_n = np.cos(120 * np.pi * t_discrete + np.pi / 3)

fig_disc, axs_disc = plt.subplots(3, 1, figsize=(10, 8))
fig_disc.suptitle('Ex 1(c): Sampled Signals (fs = 200 Hz)')

# Plot x[n]
axs_disc[0].stem(t_discrete, x_n)
axs_disc[0].set_title('x[n]')
axs_disc[0].set_xlabel('Time (s)')
axs_disc[0].set_ylabel('Amplitude')

# Plot y[n]
axs_disc[1].stem(t_discrete, y_n)
axs_disc[1].set_title('y[n]')
axs_disc[1].set_xlabel('Time (s)')
axs_disc[1].set_ylabel('Amplitude')

# Plot z[n]
axs_disc[2].stem(t_discrete, z_n)
axs_disc[2].set_title('z[n]')
axs_disc[2].set_xlabel('Time (s)')
axs_disc[2].set_ylabel('Amplitude')

fig_disc.tight_layout(rect=[0, 0.03, 1, 0.96])
plt.savefig('ex01c.eps', format='eps')
plt.show()