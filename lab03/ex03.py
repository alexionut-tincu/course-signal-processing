# https://cs.unibuc.ro/~crusu/ps/Procesarea%20Semnalelor%20(PS)%20-%20Laborator%2003.pdf

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["figure.dpi"] = 120

sample_rate = 2**13
dft_points = 2**9
t = np.linspace(0, 1, sample_rate, endpoint=False)
freq_indices = [13, 58, 123]

signals = []
for i, idx in enumerate(freq_indices, start=1):
    freq = sample_rate / dft_points * idx
    print(f"{freq} Hz")
    signals.append(i * np.sin(2 * np.pi * freq * t))

signal = np.sum(signals, axis=0)

n = np.arange(dft_points)
k = n.reshape((dft_points, 1))
W = np.exp(-2j * np.pi * k * n / dft_points)
X = W @ signal[:dft_points]

freqs = np.linspace(0, sample_rate, dft_points, endpoint=False)

fig, axs = plt.subplots(1, 2, figsize=(12, 4))

axs[0].plot(t, signal)
axs[0].set_xlabel("Timp (s)")
axs[0].set_ylabel("x(t)")

markerline, stemlines, baseline = axs[1].stem(
    freqs, np.abs(X), linefmt="k-", markerfmt="ko"
)
markerline.set_markerfacecolor("none")
stemlines.set_linewidth(0.5)
baseline.set_color("k")

axs[1].set_xlabel("Frecvență (Hz)")
axs[1].set_ylabel("|X(ω)|")
axs[1].set_xlim([0, sample_rate / 2])

plt.tight_layout()
plt.savefig("ex03.eps", format="eps")
plt.show()
