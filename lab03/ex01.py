# https://cs.unibuc.ro/~crusu/ps/Procesarea%20Semnalelor%20(PS)%20-%20Laborator%2003.pdf

import matplotlib.pyplot as plt
import numpy as np

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

# l-am facut higher res aici:

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
plt.savefig('ex01.eps', format='eps')

def is_unitary(m):
    mat = m.dot(m.T.conj()) / len(m)
    res = np.allclose(np.eye(len(m)), mat)
    print(mat[0:2][0:2])
    return res


print("Unitara?: ", is_unitary(F))

