import matplotlib.pyplot as plt
from scipy.integrate import odeint
from scipy import interpolate
import numpy as np

T = 800
t = np.linspace(0, T, T + 1)
N = 1e05
r0 = 0
i0 = 1
s0 = N - (i0 + r0)
SIR0 = i0, s0, r0
capacity = 0.2 * N
alphas = [0.1, 0.15, 0.08]
gamma = 0.05


def SIR(alpha, gamma, N=N):
    def modeloSIR(SIR, t, N=N):
        i, s, r = SIR[0], SIR[1], SIR[2]
        idot = ((alpha / N) * s - gamma) * i
        sdot = (-alpha / N) * s * i
        rdot = gamma * i
        return [idot, sdot, rdot]

    return odeint(modeloSIR, SIR0, t)


def h_line(a, parametro):
    return np.full(a.shape, parametro)


reta = h_line(t, capacity)


def I(alpha, gamma, N=N):
    return SIR(alpha, gamma, N=N)[:, 0]


def intersection(x, a, b):
    y = a - b
    s = np.abs(np.diff(np.sign(y))).astype(bool)
    return x[:-1][s] + np.diff(x)[s] / (np.abs(y[1:][s] / y[:-1][s]) + 1)


plt.style.use("ggplot")

fig1 = plt.figure(1)

for i in range(len(alphas)):
    plt.plot(t, I(alphas[i], gamma), label=r"$\alpha =$" + f"{alphas[i]}")
    intersec_array = intersection(t, I(alphas[i], gamma), reta)
    if intersec_array.size != 0:
        plt.plot(
            intersec_array, len(intersec_array) * [capacity], "x", label="interseção"
        )

plt.plot(t, reta, ls="dotted", lw=1.2)
plt.annotate(
    r"$\gamma =$" + f"{gamma:.2f}\n" + f"N = {N:.2e}",
    (T * 0.75, N * 0.1),
    bbox=dict(boxstyle="round,pad=0.9", fc="white", alpha=0.6),
)
plt.ylabel("Infectados")
plt.xlabel("Tempo")
plt.legend()

plt.show()

# print(t[intersec])  # [22. 64.]
