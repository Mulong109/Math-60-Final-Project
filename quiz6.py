import random
import matplotlib.pyplot as plt


def one_trial(p):
    state = 2
    T = 0

    while True:
        T = T + 1
        r = random.random()

        if state == 0:
            break
        elif state == 1:
            if r < p:
                state = 2
            else:
                state = 1
        else:
            if r < p:
                state = 1
            else:
                state = 0

    return T


def estimate_expected_value(p, trials=1000):
    total = 0

    for i in range(trials):
        total = total + one_trial(p)

    return total / trials


def theoretical_expected_value(p):
    return (p - 3) / (p - 1)


p = 0.3
trials = 1000

estimated = estimate_expected_value(p, trials)
theoretical = theoretical_expected_value(p)

print(estimated)
print(theoretical)

p_values = [i / 100 for i in range(5, 100, 5)]
estimated_values = []
theoretical_values = []
error_values = []

for p in p_values:
    estimated = estimate_expected_value(p, trials)
    theoretical = theoretical_expected_value(p)

    estimated_values.append(estimated)
    theoretical_values.append(theoretical)
    error_values.append(estimated - theoretical)

plt.subplot(2, 1, 1)
plt.plot(p_values, estimated_values, "o-", label="Simulation estimate")
plt.plot(p_values, theoretical_values, "-", label="Theoretical value")
plt.xlabel("p")
plt.ylabel("Expected number of steps")
plt.title("Estimated expected number of steps depending on p")
plt.legend()
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(p_values, error_values, "o-", label="Estimate - theoretical")
plt.axhline(0, color="black", linewidth=1)
plt.xlabel("p")
plt.ylabel("Difference")
plt.title("Difference between estimated and theoretical values")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
