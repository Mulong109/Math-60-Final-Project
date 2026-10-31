"""Small probability helper used only to validate the OwnIt PR checkpoint."""


def normalize_weights(weights):
    """Normalize non-negative weights; reject empty or zero-total inputs."""
    values = list(weights)
    if not values:
        raise ValueError("At least one weight is required")
    if any(value < 0 for value in values):
        raise ValueError("Weights must be non-negative")
    total = sum(values)
    if total <= 0:
        raise ValueError("The total weight must be positive")
    return [value / total for value in values]


def cumulative_probabilities(weights):
    """Build ordered cumulative cutoffs ending at exactly 1.0."""
    probabilities = normalize_weights(weights)
    result = []
    cumulative = 0.0
    for probability in probabilities:
        cumulative += probability
        result.append(cumulative)
    result[-1] = 1.0
    return result
