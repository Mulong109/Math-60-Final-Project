import numpy as np
import matplotlib.pyplot as plt

lamda = 1
miu = 0.95
n_iter = 1000
n_sim = 5
N0 = 5

bar = lamda / (lamda + miu)

for sim in range(n_sim):
    N = N0
    N_history = [N]

    for _ in range(n_iter):
        u2 = np.random.uniform(0, 1)
        if u2 > bar:
            N -= 1
        else:
            N += 1
        N_history.append(N)

        if N <= 0:
            break

    plt.plot(N_history, label=f"Simulation {sim + 1}", alpha=0.8)

plt.title(f"N over {n_iter} iterations ({n_sim} simulations)")
plt.xlabel("Iteration")
plt.ylabel("N")
plt.legend()
plt.show()