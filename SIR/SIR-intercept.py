import matplotlib.pyplot as plt
from scipy.integrate import odeint
from scipy import interpolate
import numpy as np

t = np.linspace(0, 200, 201)
N = 10**2
r0 = 0
i0 = 1
s0 = N - (i0 + r0)
SIR0 = i0, s0, r0


def SIR(alpha, gamma):
    def modeloSIR(SIR, t):
        i, s, r = SIR[0], SIR[1], SIR[2]
        idot = ((alpha / N) * s - gamma) * i
        sdot = (-alpha / N) * s * i
        rdot = gamma * i
        return [idot, sdot, rdot]

    return odeint(modeloSIR, SIR0, t)


def reta(a, parametro):
    return np.full(a.shape, parametro)


rt = reta(t, 20)

I002 = SIR(0.2, 0.05)[:, 0]
I001 = SIR(0.1, 0.05)[:, 0]
intersec = np.argwhere(np.diff(np.sign(rt - I002))).flatten()

fig1 = plt.figure(1)
plt.plot(t, I002)
plt.plot(t, I001)
plt.plot(t, rt, ls="dotted")
plt.legend([r"$\alpha/N = 0.002$", r"$\alpha/N = 0.001$"])
plt.scatter(t[intersec], rt[intersec], color="red")
plt.show()

print(t[intersec])  # [22. 64.]
