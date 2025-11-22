import itertools
import random
import time

# ---------------------------------------------------------
# Generate complete weighted graph
# ---------------------------------------------------------
def generate_graph(n):
    graph = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                graph[i][j] = random.randint(1, 20)  # random weights
    return graph

# ---------------------------------------------------------
# TSP Brute Force (Check all permutations)
# ---------------------------------------------------------
def tsp_bruteforce(graph):
    n = len(graph)
    vertices = list(range(n))
    min_cost = float("inf")

    for perm in itertools.permutations(vertices[1:]):
        path = [0] + list(perm) + [0]
        cost = 0
        for i in range(len(path)-1):
            cost += graph[path[i]][path[i+1]]
        min_cost = min(min_cost, cost)

    return min_cost

# ---------------------------------------------------------
# TSP Dynamic Programming – Held Karp Algorithm
# ---------------------------------------------------------
def tsp_held_karp(graph):
    n = len(graph)
    dp = {}

    # Base cases
    for i in range(1, n):
        dp[(1 << i, i)] = graph[0][i]

    # Build DP
    for mask in range(1 << n):
        for j in range(1, n):
            if mask & (1 << j):
                prev_mask = mask ^ (1 << j)
                if prev_mask == 0:
                    continue
                best = float("inf")
                for k in range(1, n):
                    if k != j and (prev_mask & (1 << k)):
                        best = min(best,
                                   dp.get((prev_mask, k), float("inf")) + graph[k][j])
                dp[(mask, j)] = best

    # Final step: return to start
    full_mask = (1 << n) - 1
    result = float("inf")
    for j in range(1, n):
        result = min(result, dp[(full_mask - 1, j)] + graph[j][0])

    return result


# ---------------------------------------------------------
# MAIN
# ---------------------------------------------------------
if __name__ == "__main__":
    n = 10  # Keep small because brute force is O(n!)
    graph = generate_graph(n)

    print("Generated Graph:")
    for row in graph:
        print(row)

    print("\n--- TSP Brute Force ---")
    t1 = time.time()
    bf_cost = tsp_bruteforce(graph)
    t1 = time.time() - t1
    print("Brute Force Cost:", bf_cost)
    print("Time:", t1, "seconds")

    print("\n--- TSP Dynamic Programming (Held–Karp) ---")
    t2 = time.time()
    dp_cost = tsp_held_karp(graph)
    t2 = time.time() - t2
    print("DP Cost:", dp_cost)
    print("Time:", t2, "seconds")
