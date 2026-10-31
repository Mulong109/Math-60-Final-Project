import numpy as np
import matplotlib.pyplot as plt

# Parameters
lambda_s = 0.8
mu_s = 1.0
lambda_r = 0.9
mu_r = 0.4
alpha = 0.02

# Initial condition
S = 50
R = 0
t = 0.0

# Simulation settings
T_max = 100
max_pop = 10000

# Store trajectory
times = [t]
S_values = [S]
R_values = [R]

while t < T_max and S + R > 0 and S + R < max_pop:
    # Event rates
    rates = np.array([
        lambda_s * S,   # sensitive cell division
        mu_s * S,       # sensitive cell death
        lambda_r * R,   # resistant cell division
        mu_r * R,       # resistant cell death
        alpha * S       # mutation from sensitive to resistant
    ])

    total_rate = np.sum(rates)

    if total_rate == 0:
        break

    # Time until next event
    dt = np.random.exponential(1 / total_rate)
    t += dt

    # Choose which event occurs
    event = np.random.choice(5, p=rates / total_rate)

    if event == 0:
        S += 1
    elif event == 1:
        S -= 1
    elif event == 2:
        R += 1
    elif event == 3:
        R -= 1
    elif event == 4:
        S -= 1
        R += 1

    # Store new state
    times.append(t)
    S_values.append(S)
    R_values.append(R)

# Plot trajectory
plt.plot(times, S_values, label="Sensitive cells S(t)")
plt.plot(times, R_values, label="Resistant cells R(t)")
plt.xlabel("Time")
plt.ylabel("Number of cells")
plt.title("Gillespie Simulation of Tumor Cell Population")
plt.legend()
plt.show()