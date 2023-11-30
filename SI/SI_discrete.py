# coding=utf-8

import matplotlib.pyplot as plt
import numpy as np


T = 15
td = np.linspace(1, T, T)
N = 2e08
i_0 = 1


def i_td(alpha, N=N, T=T, i_0=i_0):
    i_f = [
        i_0,
    ]
    for t in range(1, T):
        i_f.append((i_f[t - 1]) * (1 + (alpha / N) * (t - 1) * (N - i_f[t - 1])))
        """
        Nessa etapa, obtemos valores negativos caso a população de infectados
        supera a população total, logo podemos assumir 'i_t = N' nesse caso.
        """
        i_f[t] = min(i_f[t], N)

    return i_f


def s_td(alpha, N=N, T=T, i_0=i_0):
    s_0 = N - i_0
    s_f = [
        s_0,
    ]
    for t in range(1, T):
        s_f.append((s_f[t - 1]) * (1 - (alpha / N) * (t - 1) * (N - s_f[t - 1])))
        """
        Assim como no caso anterior, obtemos valores negativos para os infectados,
        que superam a população total, logo '(s_t = N - i_t) < 0' nesse caso.
        """
        if s_f[t] < 0:
            s_f[t] = 0

    return s_f

### GRÁFICOS ###
alphas = [1, 2, 3]

plt.style.use("ggplot")

fig, axs = plt.subplots(1, 3, constrained_layout=True, figsize=(9, 4))
axs[0].set_ylabel("População", fontsize=14)
axs[1].set_xlabel("Tempo", fontsize=14)

for i in range(3):
    axs[i].plot(td, i_td(alphas[i]), "D-", ms=3.5, lw=1.5)
    axs[i].plot(td, s_td(alphas[i]), "*", ls='dotted', ms=3.5, lw=1)
    axs[i].set_title(r"$\alpha = " + f"{alphas[i]}$")

plt.legend(["infectados" , "suscetiveis"])

plt.show()
