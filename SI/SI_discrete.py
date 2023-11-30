# coding=utf-8

import matplotlib.pyplot as plt
import numpy as np


T = 15
td = np.linspace(1, T, T)
N = 2e08


def i_td(alpha, N=N, T=T):
    i0 = 1
    i_f = [
        i0,
    ]
    for t in range(1, T):
        i_f.append((i_f[t - 1]) * (1 + (alpha / N) * (t - 1) * (N - i_f[t - 1])))
        """
        Nessa etapa, obtemos valores negativos caso a população de infectados
        supera a população total, logo podemos assumir 'i_t = N' nesse caso.
        """
        i_f[t] = min(i_f[t], N)

    return i_f


### GRÁFICOS ###
alphas = [1, 2, 3]

plt.style.use("ggplot")

fig, axs = plt.subplots(1, 3, constrained_layout=True, figsize=(9, 4))
axs[0].set_ylabel("Infectados", fontsize=14)
axs[1].set_xlabel("Tempo", fontsize=14)

for i in range(3):
    axs[i].scatter(td, i_td(alphas[i]))
    axs[i].set_title(r"$\alpha = " + f"{alphas[i]}$")

plt.show()
