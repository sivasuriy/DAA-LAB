from collections import deque

# -------------------------------------------------------
# Using Max Flow (Ford–Fulkerson with BFS → Edmonds–Karp)
# -------------------------------------------------------
class MaxFlow:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, u, v, capacity):
        self.graph[u][v] = capacity

    def bfs(self, s, t, parent):
        visited = [False] * self.V
        queue = deque([s])
        visited[s] = True

        while queue:
            u = queue.popleft()
            for v in range(self.V):
                if not visited[v] and self.graph[u][v] > 0:
                    queue.append(v)
                    visited[v] = True
                    parent[v] = u
                    if v == t:
                        return True
        return False

    def edmonds_karp(self, source, sink):
        parent = [-1] * self.V
        max_flow = 0

        while self.bfs(source, sink, parent):
            path_flow = float("inf")
            v = sink

            # Find minimum residual capacity
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

        return max_flow


# -------------------------------------------------------
# Convert Bipartite Graph → Flow Network
# -------------------------------------------------------
def max_bipartite_matching(U, V, edges):
    """
    U = number of left partition nodes
    V = number of right partition nodes
    edges = list of (u, v) pairs meaning u ∈ U connects to v ∈ V
    """

    total_nodes = U + V + 2
    source = U + V      # virtual source
    sink = U + V + 1    # virtual sink

    mf = MaxFlow(total_nodes)

    # connect source → U partition
    for u in range(U):
        mf.add_edge(source, u, 1)

    # connect V partition → sink
    for v in range(V):
        mf.add_edge(U + v, sink, 1)

    # connect U → V edges
    for u, v in edges:
        mf.add_edge(u, U + v, 1)

    max_match = mf.edmonds_karp(source, sink)
    return max_match


# -------------------------------------------------------
# Example
# -------------------------------------------------------
if __name__ == "__main__":
    # U = {0,1,2}, V = {0,1,2}
    U = 3
    V = 3

    # edges: u → v
    edges = [
        (0, 0),
        (0, 2),
        (1, 0),
        (2, 1),
        (2, 2)
    ]

    print("Maximum Bipartite Matching:", max_bipartite_matching(U, V, edges))
