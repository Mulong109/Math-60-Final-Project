import numpy as np
import matplotlib.pyplot as plt


def uncertain_move(current_trust, alpha, rng=None):
    """Trust step with random noise: sigma ~ Normal(0, 1)."""
    gen = rng if rng is not None else np.random.default_rng()
    sigma = gen.standard_normal()
    return current_trust + alpha * current_trust * (1 - current_trust) * sigma


if __name__ == "__main__":
    num_iteration = 100
    alpha = 0.08
    current_trust = 0.5
    trust_history = [current_trust]

    rng = np.random.default_rng(42)

    for _ in range(num_iteration):
        current_trust = uncertain_move(current_trust, alpha, rng=rng)
        current_trust = float(np.clip(current_trust, 0.0, 1.0))
        trust_history.append(current_trust)

    plt.figure(figsize=(10, 4))
    plt.plot(range(num_iteration + 1), trust_history, linewidth=1.5)
    plt.title("Uncertain move: trust over iterations (sigma ~ N(0,1))")
    plt.xlabel("Iteration")
    plt.ylabel("Trust")
    plt.ylim(-0.05, 1.05)
    plt.grid(alpha=0.3)
    plt.tight_layout()
    print(f"Final trust: {trust_history[-1]:.6f}")
    plt.show()
