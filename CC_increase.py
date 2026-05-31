import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x, k, x_0):
    return 1 / (1 + np.exp(- k * (x - x_0)))

def trust_boost(k,delta, current_trust):
    return k * current_trust * (1 - current_trust) * delta


if __name__ == "__main__":
    delta = 1
    k = 0.018
    num_iterations = 500
    # Initial trust must be non-zero, otherwise k * T * (1-T) stays 0.
    current_trust = 0.01099
    x_0 = 250

    trust_history = [current_trust]

    for i in range(num_iterations):
        # Treat trust_boost(...) as an increment, not a replacement.
        current_trust = current_trust + trust_boost(k, delta, current_trust)
        # Keep trust in a valid range.
        current_trust = float(np.clip(current_trust, 0.0, 1.0))
        trust_history.append(current_trust)

    # Plot both curves in one figure:
    # blue = discrete trust_boost iteration, red = true sigmoid function.
    x_discrete = np.arange(num_iterations + 1)
    x_cont = np.linspace(0, num_iterations, 1000)
    y_sigmoid = sigmoid(x_cont, k, x_0)

    plt.figure(figsize=(10, 4))
    plt.plot(
        x_discrete,
        trust_history,
        color="blue",
        linewidth=1.8,
        label="Blue: trust_boost iterative trust_history",
    )
    plt.plot(
        x_cont,
        y_sigmoid,
        color="red",
        linewidth=2,
        label="Red: sigmoid(x, k, x_0)",
    )
    plt.title("CC_increase: iterative update vs sigmoid function")
    plt.xlabel("x / iteration")
    plt.ylabel("Trust")
    plt.ylim(-0.05, 1.05)
    plt.grid(alpha=0.3)
    plt.legend()
    plt.tight_layout()
    print(f"Final trust: {trust_history[-1]:.6f}")
    plt.show()
