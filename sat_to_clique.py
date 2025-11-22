import itertools

# -------------------------------------------------------------
# Parse 3-CNF input like:
# (x1 OR ~x2 OR x3) AND (~x1 OR x2 OR ~x3)
# -------------------------------------------------------------
def parse_3sat(formula):
    formula = formula.replace(" ", "")
    clauses = formula.split(")AND(")
    clauses[0] = clauses[0][1:]
    clauses[-1] = clauses[-1][:-1]

    parsed = []
    for clause in clauses:
        literals = clause.split("OR")
        parsed.append(literals)
    return parsed


# -------------------------------------------------------------
# Helper: Check if two literals contradict
# -------------------------------------------------------------
def contradicts(l1, l2):
    if l1.startswith("~") and l1[1:] == l2:
        return True
    if l2.startswith("~") and l2[1:] == l1:
        return True
    return False


# -------------------------------------------------------------
# Build graph for Clique reduction
# -------------------------------------------------------------
def build_graph(clauses):
    graph = {}  # each literal occurrence becomes a vertex
    index = 0

    clause_vertices = []

    for clause in clauses:
        group = []
        for lit in clause:
            graph[index] = {"literal": lit, "clause": len(clause_vertices), "edges": []}
            group.append(index)
            index += 1
        clause_vertices.append(group)

    # Connect compatible vertices across different clauses
    for c1, c2 in itertools.combinations(range(len(clauses)), 2):
        for v1 in clause_vertices[c1]:
            for v2 in clause_vertices[c2]:
                l1 = graph[v1]["literal"]
                l2 = graph[v2]["literal"]

                if not contradicts(l1, l2):
                    graph[v1]["edges"].append(v2)
                    graph[v2]["edges"].append(v1)

    return graph, len(clauses)


# -------------------------------------------------------------
# Check if graph contains a clique of size k
# -------------------------------------------------------------
def is_clique(graph, vertices):
    for u, v in itertools.combinations(vertices, 2):
        if v not in graph[u]["edges"]:
            return False
    return True

def find_k_clique(graph, k):
    for subset in itertools.combinations(graph.keys(), k):
        if is_clique(graph, subset):
            return True, subset
    return False, None


# -------------------------------------------------------------
# MAIN
# -------------------------------------------------------------
if __name__ == "__main__":
    formula = "(x1 OR ~x2 OR x3) AND (~x1 OR x2 OR ~x3) AND (x2 OR x3 OR ~x1)"
    print("Formula:", formula)

    clauses = parse_3sat(formula)
    print("\nParsed Clauses:", clauses)

    graph, k = build_graph(clauses)

    print("\nGraph Vertices:")
    for v in graph:
        print(v, graph[v])

    print(f"\nChecking for clique of size {k} ...")
    possible, clique_set = find_k_clique(graph, k)

    if possible:
        print("3-SAT instance is SATISFIABLE!")
        print("Clique found:", clique_set)
    else:
        print("3-SAT instance is UNSATISFIABLE.")
