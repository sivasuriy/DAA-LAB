import random

# Simulate tossing n coins (0 = tail, 1 = head)
def coin_toss(n):
    tosses = [random.choice([0, 1]) for _ in range(n)]
    heads = sum(tosses)     # indicator variables sum
    return heads

# Run multiple trials to estimate expectation & variance
def coin_toss_trials(n, trials):
    results = []
    for _ in range(trials):
        results.append(coin_toss(n))

    avg = sum(results) / trials
    var = sum((x - avg) ** 2 for x in results) / trials
    return avg, var

# Example extended hiring using indicator variables
# (This reuses result from hiring simulation)
def hiring_indicator(n):
    best = -1
    hires = 0
    candidates = [random.random() for _ in range(n)]

    for i in range(n):
        # Indicator variable: I(i) = 1 if candidate i is a new best
        if candidates[i] > best:
            best = candidates[i]
            hires += 1
    return hires

def hiring_indicator_trials(n, trials):
    total = 0
    for _ in range(trials):
        total += hiring_indicator(n)
    return total / trials

# Example usage
if __name__ == "__main__":
    n = 100
    trials = 500

    print("Indicator Variables: Coin Toss Simulation")
    print("----------------------------------------")
    avg, var = coin_toss_trials(n, trials)
    print("Coins:", n)
    print("Trials:", trials)
    print("Average Heads:", avg)
    print("Variance:", var)

    print("\nIndicator Variables: Hiring Problem Extension")
    print("---------------------------------------------")
    print("Expected hires:", hiring_indicator_trials(1000, 500))
