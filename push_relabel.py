from collections import deque
import random

# -------------------------------------------------------
# Push–Relabel Algorithm
# -------------------------------------------------------
class PushRelabel:
    def __init__(self, n):
        self.n = n
        self.capacity = [[0]*n for _ in range(n)]
        self.flow = [[0]*n for _ in range(n)]
        self.height = [0]*n
        self.excess = [0]*n
        self.count_relabels = 0

    def add_edge(self, u, v, cap):
        self.capacity[u][v] = cap

    # Push operation
    def push(self, u, v):
        send = min(self.excess[u], self.capacity[u][v] - self.flow[u][v])
        self.flow[u][v] += send
        self.flow[v][u] -= send
        self.excess[u] -= send
        self.excess[v] += send

    # Relabel operation
    def relabel(self, u):
        min_height = float("inf")
        for v in range(self.n):
            if self.capacity[u][v] - self.flow[u][v] > 0:
                min_height = min(min_height, self.height[v])
        self.height[u] = min_height + 1
        self.count_relabels += 1

    def discharge(self, u):
        while self.excess[u] > 0:
            done = False
            for v in range(self.n):
                if self.capacity[u][v] - self.flow[u][v] > 0 and self.height[u] == self.height[v] + 1:
                    self.push(u, v)
                    done = True
                    if self.excess[u] == 0:
                        break
            if not done:
                self.relabel(u)

    # Main function to compute max flow
    def max_flow(self, s, t):
        self.height[s] = self.n
        for v in range(self.n):
            if self.capacity[s][v] > 0:
                self.flow[s][v] = self.capacity[s][v]
                self.flow[v][s] -= self.capacity[s][v]
                self.excess[v] += self.capacity[s][v]

        active = [i for i in range(self.n) if i != s and i != t]

        p = 0
        while p < len(active):
            u = active[p]
            old_height = self.height[u]
            self.discharge(u)
            if self.height[u] > old_height:
                active.insert(0, active.pop(p))
            else:
                p += 1

        return sum(self.flow[s][v] for v in range(self.n)), self.count_relabels

# -------------------------------------------------------
# Example + Comparison with Ford–Fulkerson
# -------------------------------------------------------
def create_graph():
    # same example network for comparison
    pr = PushRelabel(6)

    edges = [
        (0,1,16), (0,2,13),
        (1,3,12), (2,1,4),
        (2,4,14), (3,5,20),
        (4,3,7), (4,5,4)
    ]

    for u, v, c in edges:
        pr.add_edge(u, v, c)

    return pr

if __name__ == "__main__":
    print("Push–Relabel Maximum Flow Algorithm")
    print("-----------------------------------")

    pr = create_graph()
    maxflow, relabels = pr.max_flow(0, 5)

    print("Maximum Flow:", maxflow)
    print("Relabel operations:", relabels)
