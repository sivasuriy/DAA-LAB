from collections import defaultdict
import random

# -------------------------------------------------------
# Graph class using adjacency list for Ford–Fulkerson
# -------------------------------------------------------
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0] * vertices for _ in range(vertices)]

    # Add capacity to an edge
    def add_edge(self, u, v, capacity):
        self.graph[u][v] = capacity

    # Depth-First Search to find augmenting path
    def dfs(self, s, t, parent):
        visited = [False] * self.V
        stack = [s]
        visited[s] = True

        while stack:
            u = stack.pop()
            for v in range(self.V):
                if not visited[v] and self.graph[u][v] > 0:
                    stack.append(v)
                    visited[v] = True
                    parent[v] = u
                    if v == t:
                        return True
        return False

    # Ford–Fulkerson Algorithm
    def ford_fulkerson(self, source, sink):
        parent = [-1] * self.V
        max_flow = 0

        while self.dfs(source, sink, parent):
            path_flow = float("inf")
            v = sink

            # Find minimum residual capacity along the path
            while v != source:
                u = parent[v]
                path_flow = min(path_flow, self.graph[u][v])
                v = u

            max_flow += path_flow

            # Update residual graph
            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = u

            print("\nResidual Graph After Augmentation:")
            for row in self.graph:
                print(row)

        return max_flow


# -------------------------------------------------------
# Helper to generate deterministic / random capacity graph
# -------------------------------------------------------
def create_test_graph(randomize=False):
    g = Graph(6)

    if randomize:
        g.add_edge(0, 1, random.randint(5,20))
        g.add_edge(0, 2, random.randint(5,20))
        g.add_edge(1, 3, random.randint(5,20))
        g.add_edge(2, 1, random.randint(5,20))
        g.add_edge(2, 4, random.randint(5,20))
        g.add_edge(3, 5, random.randint(5,20))
        g.add_edge(4, 3, random.randint(5,20))
        g.add_edge(4, 5, random.randint(5,20))
    else:
        # Deterministic fixed capacities
        edges = [
            (0,1,16), (0,2,13),
            (1,3,12), (2,1,4),
            (2,4,14), (3,5,20),
            (4,3,7),  (4,5,4)
        ]
        for u,v,c in edges:
            g.add_edge(u, v, c)

    return g


# -------------------------------------------------------
# MAIN
# -------------------------------------------------------
if __name__ == "__main__":
    print("Ford–Fulkerson (Deterministic Capacities)")
    g1 = create_test_graph(randomize=False)
    print("Maximum Flow:", g1.ford_fulkerson(0, 5))

    print("\n--------------------------------------------\n")

    print("Ford–Fulkerson (Randomized Capacities)")
    g2 = create_test_graph(randomize=True)
    print("Maximum Flow:", g2.ford_fulkerson(0, 5))
