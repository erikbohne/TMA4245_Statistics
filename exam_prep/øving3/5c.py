import numpy as np
import matplotlib.pyplot as plt

def Mu(t, n):
    return np.exp(n * np.log((np.exp(t/np.sqrt(n)) + np.exp(-t/np.sqrt(n))) / 2))

def Mz(t):
    return np.exp(t**2 / 2)

N = [4, 10, 100]

for n in N:
    t = np.linspace(0,1,1000)
    U = [Mu(i, n) for i in t]
    Z = [Mz(i) for i in t]
    plt.plot(t, U, label=f'Mu(t, {n})')
    plt.plot(t, Z, label='Mz(t)')
    plt.legend()

plt.savefig("5c.png")