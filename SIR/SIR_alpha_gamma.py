# coding=utf-8

import matplotlib.pyplot as plt
from scipy.integrate import odeint
import numpy as np

T = 30
t = np.arange(0, T, 0.001)
N = 1e02
r0 = 0
i0 = 1
s0 = N - (i0 + r0)
SIR0 = i0, s0, r0


def SIR(alpha, gamma, N=N):
    def modeloSIR(SIR, t, N=N):
        i, s, r = SIR[0], SIR[1], SIR[2]
        idot = ((alpha / N) * s - gamma) * i
        sdot = (-alpha / N) * s * i
        rdot = gamma * i
        return [idot, sdot, rdot]

    return odeint(modeloSIR, SIR0, t)


alpha_gamma_to_fit = [
    1.65,
    2.20,
    2.95,
    3.90,
    5.30,
    7.50,
    11.40,
    14.70,
    19.90,
    29.05,
    48.80,
    114.60,
]

fraction = [0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.75, 0.80, 0.85, 0.90, 0.95]

estimate = np.poly1d(np.polyfit(fraction, alpha_gamma_to_fit, 25))

fraction_random = [
    [round(np.random.uniform(0.1, 0.95), 2) for _ in range(3)],
    [round(np.random.uniform(0.1, 0.95), 2) for _ in range(3)],
    [round(np.random.uniform(0.1, 0.95), 2) for _ in range(3)],
]


def h_line(a, parametro):
    return np.full(a.shape, parametro)


plt.style.use("ggplot")

fig, axs = plt.subplots(3, 3, figsize=(10, 9))

gammas = [
    [round(np.random.rand(), 2) for _ in range(3)],
    [round(np.random.rand(), 2) for _ in range(3)],
    [round(np.random.rand(), 2) for _ in range(3)],
]

alphas = [
    [
        round(gammas[0][i] * round(estimate(fraction_random[0][i]), 2), 2)
        for i in range(len(gammas[0]))
    ],
    [
        round(gammas[1][i] * round(estimate(fraction_random[1][i]), 2), 2)
        for i in range(len(gammas[1]))
    ],
    [
        round(gammas[2][i] * round(estimate(fraction_random[2][i]), 2), 2)
        for i in range(len(gammas[2]))
    ],
]

for i in range(3):
    for j in range(3):
        axs[i, j].plot(t, SIR(alphas[i][j], gammas[i][j]))
        axs[i, j].annotate(
            r"$\gamma =$"
            + f"{gammas[i][j]:.2f}\n"
            + r"$\alpha =$"
            + f"{alphas[i][j]:.2f}\n"
            + f"{fraction_random[i][j]} N",
            (T*0.65, N*0.2),
            bbox=dict(boxstyle='round,pad=0.9', fc='white', alpha=0.6),
        )
        axs[i, j].plot(t, h_line(t, N * fraction_random[i][j]), ls="dotted")


plt.legend(["infectados", "suscetiveis", "recuperados"], loc="upper right")


plt.show()
