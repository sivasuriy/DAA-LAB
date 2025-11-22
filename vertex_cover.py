import itertools
import time

# -----------------------------------------------------------
# Exact Vertex Cover (Brute Force)
# -----------------------------------------------------------
def is_vertex_cover(graph, cover):
    cover = set(cover)
    for u in graph:
        for v in graph[u]:
            if u not in cover and v not in cover:
                return False
    return True

def brute_force_vertex_cover(graph):
    nodes = list(graph.keys())
    n = len(nodes)

    for r in range(1, n+1):
        for subset in itertools.combinations(nodes, r):
            if is_vertex_cover(graph, subset):
                return set(subset)
    return None


# -----------------------------------------------------------
# 2-Approximation for Vertex Cover (Greedy)
# -----------------------------------------------------------
def approx_vertex_cover(graph):
    visited = set()
    edges = []

    # collect edges
    for u in graph:
        for v in graph[u]:
            edges.append((u, v))

    cover = set()

    for (u, v) in edges:
        if u not in visited and v not in visited:
            cover.add(u)
            cover.add(v)
            visited.add(u)
            visited.add(v)

    return cover


# -----------------------------------------------------------
# Example Graph
# -----------------------------------------------------------
def sample_graph():
    return {
        0: [1, 2],
        1: [0, 3],
        2: [0, 3],
        3: [1, 2]
    }


# -----------------------------------------------------------
# MAIN
# -----------------------------------------------------------
if __name__ == "__main__":
    graph = sample_graph()

    print("Graph:", graph)
    print("\n--- Exact Vertex Cover (Brute Force) ---")
    t1 = time.time()
    exact = brute_force_vertex_cover(graph)
    t1 = time.time() - t1
    print("Exact Solution:", exact)
    print("Time:", t1, "seconds")

    print("\n--- 2-Approximation Algorithm ---")
    t2 = time.time()
    approx = approx_vertex_cover(graph)
    t2 = time.time() - t2
    print("Approx Solution:", approx)
    print("Time:", t2, "seconds")
