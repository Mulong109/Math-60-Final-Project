import numpy as np
import matplotlib.pyplot as plt

from Individual_Simulation import run_simulation


def sample_final_trust_distribution(
    p_correct,
    p_confident_correct,
    p_confident_incorrect,
    num_people=1000,
    num_iterations=500,
    initial_trust=0.5,

):
    final_trusts = np.empty(num_people, dtype=float)
    trust_histories = np.empty((num_people, num_iterations + 1), dtype=float)

    for i in range(num_people):
        trust_history, _ = run_simulation(
            p_correct=p_correct,
            p_confident_correct = p_confident_correct,
            p_confident_incorrect = p_confident_incorrect,
            num_iterations = num_iterations,
            current_trust = initial_trust,
        )
        trust_histories[i] = trust_history
        final_trusts[i] = trust_history[-1]

    mean_trust_history = np.mean(trust_histories, axis=0)
    return final_trusts, mean_trust_history


if __name__ == "__main__":
    num_people = 1000
    num_iterations = 500

    scenarios = [
        {
            "label": "Normal AI",
            "p_correct": 0.74,
            "p_confident_correct": 0.7,
            "p_confident_incorrect": 0.67,
            "color": "darkgreen",
        },
        {
            "label": "Honest AI",
            "p_correct": 0.738,
            "p_confident_correct": 0.85,
            "p_confident_incorrect": 0.2,
            "color": "steelblue",
        },
        {
            "label": "Accurate AI",
            "p_correct": 0.9,
            "p_confident_correct": 0.7,
            "p_confident_incorrect": 0.67,
            "color": "crimson",
        },
    ]

    plt.figure(figsize=(10, 5))

    print(f"Running {len(scenarios)} scenarios: {num_people} simulations each.")
    scenario_results = []
    for scenario in scenarios:
        final_trusts, mean_trust_history = sample_final_trust_distribution(
            p_correct=scenario["p_correct"],
            p_confident_correct=scenario["p_confident_correct"],
            p_confident_incorrect=scenario["p_confident_incorrect"],
            num_people=num_people,
            num_iterations=num_iterations,
        )

        p_incorrect = 1.0 - scenario["p_correct"]
        print(
            f"{scenario['label']}: "
            f"p_correct={scenario['p_correct']:.2f}, "
            f"p_incorrect={p_incorrect:.2f}, "
            f"mean final trust={np.mean(final_trusts):.4f}, "
            f"std={np.std(final_trusts):.4f}"
        )

        scenario_results.append(
            {
                "scenario": scenario,
                "final_trusts": final_trusts,
            }
        )

        plt.plot(
            range(num_iterations + 1),
            mean_trust_history,
            color=scenario["color"],
            linewidth=2,
            label=(
                f"{scenario['label']} "
                f"(p_correct={scenario['p_correct']:.2f})"
            ),
        )

    plt.xlabel("Iteration")
    plt.ylabel("Mean trust in AI")
    plt.ylim(0, 1)
    plt.grid(alpha=0.3)
    plt.legend()
    plt.tight_layout()

    for result in scenario_results:
        scenario = result["scenario"]
        final_trusts = result["final_trusts"]

        plt.figure(figsize=(10, 5))
        plt.hist(
            final_trusts,
            bins=40,
            range=(0.0, 1.0),
            density=True,
            edgecolor="black",
            alpha=0.8,
            color=scenario["color"],
        )
        plt.xlabel("Final trust in AI")
        plt.ylabel("Density")
        plt.xlim(0, 1)
        plt.grid(alpha=0.3)
        plt.tight_layout()

    plt.show()
