# coding=utf-8

import matplotlib.pyplot as plt
from scipy.integrate import odeint
import numpy as np

T = 700
t = np.arange(0, 700, 0.01)
N = 2e08
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


gamma = 0.05
alpha1 = 0.1
alpha2 = alpha1 * 1.5

res1 = SIR(alpha1, gamma)
res2 = SIR(alpha2, gamma)


plt.style.use("ggplot")

fig = plt.figure(figsize=(9, 8))

for i in range(3):
    plt.plot(t, res1[:, i])

for i in range(3):
    plt.plot(t, res2[:, i], ls="dotted", lw=2)

plt.annotate(
    r"$\gamma$ = " + f"{gamma}",
    (T * 0.9, N * 0.95),
    bbox=dict(boxstyle="round,pad=0.9", fc="white", alpha=0.6),
)
plt.ylabel("População")
plt.xlabel("Tempo")

plt.legend(
    [
        r"Infectados $\alpha$ = " + f"{alpha1:.2f}",
        r"Suscetiveis $\alpha$ = " + f"{alpha1:.2f}",
        r"Recuperados $\alpha$ = " + f"{alpha1:.2f}",
        r"Infectados $\alpha$ = " + f"{alpha2:.2f}",
        r"Suscetiveis $\alpha$ = " + f"{alpha2:.2f}",
        r"Recuperados $\alpha$ = " + f"{alpha2:.2f}",
    ]
)


plt.show()
