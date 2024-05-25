import numpy as np
import matplotlib.pyplot as plt

n = 100000
mu = 1
sd = 2
alpha = 2
beta = 0.5


x = np.random.normal(loc=mu, scale=sd, size=n)

y = np.zeros(n)
for i in range(n):
    y[i] = alpha*x[i] + beta

plt.hist(x=y, bins=100)
plt.savefig("4a.png")