import random
import math
import time

# ---------------------------------------------------------
# Generate random 2D points
# ---------------------------------------------------------
def generate_points(n, limit=100):
    return [(random.randint(0, limit), random.randint(0, limit)) for _ in range(n)]


# ---------------------------------------------------------
# Convex Hull using Graham Scan
# ---------------------------------------------------------
def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    return 1 if val > 0 else 2

def dist_sq(p, q):
    return (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2

def convex_hull(points):
    n = len(points)
    if n < 3:
        return points

    # Step 1: Find bottom-most point
    low = min(points, key=lambda p: (p[1], p[0]))
    points.pop(points.index(low))

    # Step 2: Sort by polar angle w.r.t low point
    points.sort(key=lambda p: (math.atan2(p[1] - low[1], p[0] - low[0]), dist_sq(low, p)))

    # Step 3: Graham scan
    hull = [low, points[0], points[1]]

    for p in points[2:]:
        while len(hull) > 1 and orientation(hull[-2], hull[-1], p) != 2:
            hull.pop()
        hull.append(p)

    return hull


# ---------------------------------------------------------
# Closest Pair of Points
# ---------------------------------------------------------

# Brute Force → O(n²)
def closest_pair_bruteforce(points):
    n = len(points)
    min_dist = float("inf")
    pair = None

    for i in range(n):
        for j in range(i + 1, n):
            d = math.dist(points[i], points[j])
            if d < min_dist:
                min_dist = d
                pair = (points[i], points[j])

    return min_dist, pair


# Divide & Conquer → O(n log n)
def closest_pair_dc(points):
    px = sorted(points, key=lambda p: p[0])
    py = sorted(points, key=lambda p: p[1])
    return closest_pair_rec(px, py)[0:2]

def closest_pair_rec(px, py):
    n = len(px)

    if n <= 3:
        return closest_pair_bruteforce(px) + (px, py)

    mid = n // 2
    mid_point = px[mid]

    Qx = px[:mid]
    Rx = px[mid:]

    Qy = [p for p in py if p in Qx]
    Ry = [p for p in py if p in Rx]

    (dl, pl, Qx, Qy) = closest_pair_rec(Qx, Qy)
    (dr, pr, Rx, Ry) = closest_pair_rec(Rx, Ry)

    d = min(dl, dr)
    best_pair = pl if dl < dr else pr

    strip = [p for p in py if abs(p[0] - mid_point[0]) < d]

    for i in range(len(strip)):
        for j in range(i+1, min(i+7, len(strip))):
            dist = math.dist(strip[i], strip[j])
            if dist < d:
                d = dist
                best_pair = (strip[i], strip[j])

    return d, best_pair, px, py


# ---------------------------------------------------------
# MAIN
# ---------------------------------------------------------
if __name__ == "__main__":
    n = 20
    points = generate_points(n)

    print("Generated Points:")
    print(points)

    # Convex Hull
    hull = convex_hull(points.copy())
    print("\nConvex Hull (Graham Scan):")
    print(hull)

    # Closest Pair (Brute Force)
    t1 = time.time()
    bf_dist, bf_pair = closest_pair_bruteforce(points)
    t1 = time.time() - t1

    # Closest Pair (Divide & Conquer)
    t2s = time.time()
    dc_dist, dc_pair = closest_pair_dc(points)
    t2 = time.time() - t2s

    print("\nClosest Pair Results:")
    print("Brute Force Distance:", bf_dist, "Pair:", bf_pair)
    print("Divide & Conquer Distance:", dc_dist, "Pair:", dc_pair)

    print("\nExecution Time:")
    print("Brute Force:", t1, "seconds")
    print("Divide & Conquer:", t2, "seconds")
