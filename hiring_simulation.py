import random
import math

# Simulate the hiring process for n candidates
def hiring_simulation(n):
    best = -1
    hires = 0
    for candidate in [random.random() for _ in range(n)]:
        if candidate > best:
            best = candidate
            hires += 1
    return hires

# Run Monte Carlo trials to estimate expected hires
def hiring_trials(n, trials):
    total = 0
    for _ in range(trials):
        total += hiring_simulation(n)
    return total / trials

# Example usage
if __name__ == "__main__":
    n = 1000       # number of candidates
    trials = 500   # number of simulations

    print("Hiring Simulation Results")
    print("--------------------------")
    print("Candidates:", n)
    print("Trials:", trials)
    print("Expected hires (Monte Carlo):", hiring_trials(n, trials))
    print("Theoretical ≈ ln(n):", math.log(n))
