import numpy as np
import matplotlib.pyplot as plt

from CC_increase import trust_boost
from CW_decrease import CW_decrease
from Uncertain_move import uncertain_move


def run_simulation(
    p_correct,
    p_confident_correct,
    p_confident_incorrect,
    num_iterations=500,
    current_trust=0.5,
):

    # CC: confident when correct. CW: confident when wrong. Rest → uncertain moves.
    p_CC = p_confident_correct * p_correct
    p_CW = p_confident_incorrect * (1 - p_correct)
    p_uncertain = 1.0 - p_CC - p_CW

    delta = 1
    k = 0.044
    decrease_rate = 0.93
    alpha = 0.022
    a =2
    b = 0.5

    trust_history = [current_trust]


    for _ in range(num_iterations):
        u1 = np.random.uniform(0, 1)
        if u1 < p_CC:
            current_trust = current_trust + trust_boost(k, delta, current_trust)
        elif u1 < p_CC + p_CW:
            current_trust = CW_decrease(current_trust, decrease_rate, a, b)
        else:
            current_trust = uncertain_move(current_trust, alpha)

        current_trust = float(np.clip(current_trust, 0.0, 1.0))
        trust_history.append(current_trust)

    return trust_history, dict(
        p_CC=p_CC,
        p_CW=p_CW,
        p_uncertain=p_uncertain,
    )


if __name__ == "__main__":
    num_iterations = 500
    p_correct = 0.98
    p_confident_correct = 0.9
    p_confident_incorrect = 0.3
    trust_history, probs = run_simulation(
        p_correct=p_correct,
        p_confident_correct=p_confident_correct,
        p_confident_incorrect=p_confident_incorrect,
        num_iterations=num_iterations
    )


    plt.figure(figsize=(10, 4))
    plt.plot(
        range(num_iterations + 1),
        trust_history,
        linewidth=1.5,
        color="steelblue",
    )
    plt.title(
        "Combined trust dynamics (CC boost / CW decrease / uncertain noise)"
    )
    plt.xlabel("Iteration")
    plt.ylabel("Trust")
    plt.ylim(-0.05, 1.05)
    plt.grid(alpha=0.3)
    plt.tight_layout()
    print(
        f"Final trust: {trust_history[-1]:.6f} | "
        f"p_CC={probs['p_CC']:.3f}, p_CW={probs['p_CW']:.3f}, "
        f"p_uncertain={probs['p_uncertain']:.3f}"
    )
    plt.show()
