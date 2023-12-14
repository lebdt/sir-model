# coding=utf-8

import matplotlib.pyplot as plt


def time(ini, end, n):
    res = [
        ini,
    ]
    step = abs(end - ini) / n
    for i in range(n):
        res.append(res[i] + step)
    return res


n_points = 120

T = 700
dt = T / n_points
t = time(0, T, n_points)
N = 2e08

gamma = 0.05
alpha1 = 0.1
alpha2 = alpha1 * 1.5


def SIR(alpha, gamma, T, dt, n, N=N):
    r = [
        0,
    ]
    i = [
        1,
    ]
    s = [
        N - (i[0] + r[0]),
    ]

    for t in range(n):
        i.append(i[t] * (1 + (alpha / N) * dt * s[t] - gamma * dt))
        s.append(s[t] * (1 - (alpha / N) * dt * i[t]))
        r.append(r[t] + gamma * dt * i[t])

    return [i, s, r]


res1 = SIR(alpha1, gamma, T, dt, n_points)
res2 = SIR(alpha2, gamma, T, dt, n_points)


plt.style.use("ggplot")

fig = plt.figure(figsize=(9, 8))

for i in range(3):
    plt.plot(t, res1[:][i], "D-", ms=2.5, lw=1)

for i in range(3):
    plt.plot(t, res2[:][i], "*", ls="dotted", ms=2.5, lw=1)


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
