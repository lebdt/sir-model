# coding=utf-8

import matplotlib.pyplot as plt
import numpy as np


T = 15
tc = np.arange(0, T, 0.00001)
N = 2e08


def i_tc(alpha):
    i_0 = 1
    i_tc = N * i_0 / (i_0 + (np.exp(-alpha * tc)) * (N - 1))
    return i_tc


### GRÁFICOS ###
alphas = [1, 2, 3]

plt.style.use("ggplot")

fig, axs = plt.subplots(1, 3, constrained_layout=True, figsize=(9, 4))
axs[0].set_ylabel("Infectados", fontsize=14)
axs[1].set_xlabel("Tempo", fontsize=14)

for i in range(3):
    axs[i].plot(tc, i_tc(alphas[i]))
    axs[i].set_title(r"$\alpha = " + f"{alphas[i]}$")

plt.show()
