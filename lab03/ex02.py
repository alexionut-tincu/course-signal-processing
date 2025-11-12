# https://cs.unibuc.ro/~crusu/ps/Procesarea%20Semnalelor%20(PS)%20-%20Laborator%2003.pdf

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["figure.dpi"] = 120


# Helpere
def plot_multicolor(ax, x, y, color_source, cmap, x_label, y_label):
    values = np.abs(color_source)
    norm = plt.Normalize(values.min(), values.max())

    for i in range(len(x) - 1):
        color = cmap(norm(values[i]))
        ax.plot([x[i], x[i + 1]], [y[i], y[i + 1]], color=color)

    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.axhline(0, color="black", linewidth=0.8)


def plot_complex_path(ax, z, cmap, omega=None):
    values = np.abs(z)
    norm = plt.Normalize(values.min(), values.max())

    for i in range(len(z) - 1):
        color = cmap(norm(values[i]))
        ax.plot(
            [np.real(z[i]), np.real(z[i + 1])],
            [np.imag(z[i]), np.imag(z[i + 1])],
            color=color,
        )

    # Centrul de greutate
    center = np.mean(z)
    ax.scatter(np.real(center), np.imag(center), color="black", s=50, zorder=3)

    ax.axhline(0, color="black", linewidth=0.8)
    ax.axvline(0, color="black", linewidth=0.8)
    ax.set_aspect("equal", "box")
    ax.set_xlim([-1.1, 1.1])
    ax.set_ylim([-1.1, 1.1])
    ax.set_xlabel("Real")
    ax.set_ylabel("Imaginar")
    if omega is not None:
        ax.set_title(f"ω = {omega}")


t = np.linspace(0, 1, 1000)
omega = 6
signal = np.sin(2 * np.pi * omega * t + np.pi / 2)
cmap = plt.get_cmap("viridis")


# Figura 1
fig, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
fig.suptitle("Semnal sinusoidal")

plot_multicolor(ax1, t, signal, signal, cmap, "Timp (esantioane)", "Amplitudine")

z = signal * np.exp(-2 * np.pi * 1j * t)
plot_multicolor(ax2, np.real(z), np.imag(z), z, cmap, "Real", "Imaginar")

ax2.add_patch(plt.Circle((0, 0), 1, fill=False, color="red", linestyle="dotted"))
ax2.axvline(0, color="black", linewidth=0.8)
ax2.set_aspect("equal", "box")

plt.tight_layout()
plt.show()
plt.savefig('ex02a.eps', format='eps')


# Fiura 2
omegas = [3, 6, 10, 12]
fig, axs = plt.subplots(2, 2, figsize=(6, 6), sharex=True, sharey=True)

for ax, omega in zip(axs.flat, omegas):
    z = signal * np.exp(-2 * np.pi * omega * 1j * t)
    plot_complex_path(ax, z, cmap, omega)

for ax in axs.flat:
    ax.label_outer()

plt.tight_layout()
# nu stiu dc creeaza un window gol aditional
plt.show()
plt.savefig('ex02b.eps', format='eps')

