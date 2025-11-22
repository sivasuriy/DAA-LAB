import heapq
import itertools
import random
import time

# ---------------------------------------------------------
# Dijkstra's Algorithm → Polynomial Time
# ---------------------------------------------------------
def dijkstra(graph, start):
    n = len(graph)
    dist = [float("inf")] * n
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue

        for v, w in graph[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))

    return dist


# ---------------------------------------------------------
# TSP Brute Force → NP-Hard
# ---------------------------------------------------------
def tsp_bruteforce(graph):
    n = len(graph)
    nodes = list(range(n))
    best = float("inf")

    for perm in itertools.permutations(nodes[1:]):
        path = [0] + list(perm) + [0]
        cost = 0
        for i in range(len(path)-1):
            cost += graph[path[i]][path[i+1]]
        best = min(best, cost)

    return best


# ---------------------------------------------------------
# Random Graph Generator
# ---------------------------------------------------------
def generate_weighted_graph(n):
    # For Dijkstra: adjacency list of (node, weight)
    g = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                w = random.randint(1, 20)
                g[i].append((j, w))
    return g

def generate_tsp_graph(n):
    # TSP uses matrix form
    graph = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                graph[i][j] = random.randint(1, 20)
    return graph


# ---------------------------------------------------------
# MAIN
# ---------------------------------------------------------
if __name__ == "__main__":
    print("Polynomial vs Non-Deterministic Algorithm Comparison")
    print("-----------------------------------------------------")

    sizes = [4, 5, 6, 7, 8]   # TSP can't go higher (n!)
    print("\nn | Dijkstra Time (sec) | TSP Time (sec)")
    print("-----------------------------------------------")

    for n in sizes:
        # Dijkstra performance
        g1 = generate_weighted_graph(n)
        t1 = time.time()
        dijkstra(g1, 0)
        t1 = time.time() - t1

        # TSP brute force performance
        g2 = generate_tsp_graph(n)
        t2 = time.time()
        tsp_bruteforce(g2)
        t2 = time.time() - t2

        print(f"{n:2d} | {t1:.6f}           | {t2:.6f}")
