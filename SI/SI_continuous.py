# coding=utf-8

import matplotlib.pyplot as plt
import numpy as np


T = 30
tc = np.arange(0, T, 0.00001)
N = 2e08
i_0 = 1


def i_tc(alpha, N=N, i_0=i_0):
    return N * i_0 / (i_0 + (np.exp(-alpha * tc)) * (N - i_0))

def s_tc(alpha, N=N, i_0=i_0):
    s_0 = N-i_0
    return N * s_0 / (s_0 + (np.exp(alpha * tc)) * (N - s_0))

### GRÁFICOS ###
alphas = [1, 2, 3]

plt.style.use("ggplot")

fig, axs = plt.subplots(1, 3, constrained_layout=True, figsize=(9, 4))
axs[0].set_ylabel("População", fontsize=14)
axs[1].set_xlabel("Tempo", fontsize=14)

for i in range(3):
    axs[i].plot(tc, i_tc(alphas[i]), lw=1.5)
    axs[i].plot(tc, s_tc(alphas[i]), ls='dotted', lw=1.5)
    axs[i].set_title(r"$\alpha = " + f"{alphas[i]}$")

plt.legend(["infectados" , "suscetiveis"])

plt.show()
