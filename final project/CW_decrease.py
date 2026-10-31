import numpy as np
import matplotlib.pyplot as plt


def CW_decrease(current_trust, decrease_rate,a, b):
    """Multiplicative trust decrease (confident wrong response)."""
    x = np.random.beta(a,b)
    return current_trust * decrease_rate ** x


def exponential(x, T0, alpha):
    """Continuous exponential decay T(x) = T0 * exp(-alpha * x)."""
    return T0 * np.exp(-alpha * x)


if __name__ == "__main__":
    num_iterations = 5
    decrease_rate = 0.496
    alpha = 0.496
    T0 = 1.0
    a = 4
    b = 0.25

    current_trust = T0
    trust_history = [current_trust]

    for _ in range(num_iterations):
        current_trust = CW_decrease(current_trust, decrease_rate)
        trust_history.append(current_trust)

    # Plot both curves in one figure:
    # blue = discrete CW_decrease update, red = exponential function.
    x_discrete = np.arange(num_iterations + 1)
    x_cont = np.linspace(0, num_iterations, 500)
    y_exp = exponential(x_cont, T0, alpha)

    plt.figure(figsize=(10, 4))
    plt.plot(
        x_discrete,
        trust_history,
        marker="o",
        color="blue",
        linewidth=1.8,
        label="Blue: CW_decrease iterative trust_history",
    )
    plt.plot(
        x_cont,
        y_exp,
        color="red",
        linewidth=2,
        label=r"Red: exponential $T_0 e^{-\alpha x}$",
    )
    plt.title("CW_decrease: iterative update vs exponential function")
    plt.xlabel("x / iteration")
    plt.ylabel("Trust")
    plt.grid(alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.show()
