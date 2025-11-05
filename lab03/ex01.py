import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import Normalize
from matplotlib import cm
from matplotlib.ticker import ScalarFormatter

plt.rcParams["figure.dpi"] = 120

# N = 8
# F = np.zeros((N, N), dtype=complex)
# for index in range(N):
#     for j in range(N):
#         F[index][j] = np.power(np.e, -2 * np.pi * 1j * index * j / N)
#
# fig, axs = plt.subplots(N, figsize=(12, 6), sharex=True, sharey=True)
#
# for index in range(N):
#     axs[index].plot([j + 1 for j in range(8)], F[index].real)
#     axs[index].plot([j + 1 for j in range(8)], F[index].imag, ".--")
#     axs[index].set_ylabel(f"linia {index}")
#
# plt.show()

N = 64
F = np.zeros((N, N), dtype=complex)
for index in range(N):
    for j in range(N):
        F[index][j] = np.power(np.e, -2 * np.pi * 1j * index * j / N)

fig, axs = plt.subplots(N//8, figsize=(12, 6), sharex=True, sharey=True)

for index in range(N//16):
    axs[index].plot([j + 1 for j in range(N)], F[index].real)
    axs[index].plot([j + 1 for j in range(N)], F[index].imag, ".--")
    axs[index].set_ylabel(f"linia {index}")

for index in range(N//16):
    axs[index + 4].plot([j + 1 for j in range(N)], F[N + index - N//16].real)
    axs[index + 4].plot([j + 1 for j in range(N)], F[N + index - N//16].imag, ".--")
    axs[index + 4].set_ylabel(f"linia {N + index - N // 16}")

plt.show()