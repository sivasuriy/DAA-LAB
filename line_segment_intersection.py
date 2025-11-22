import random

# ---------------------------------------------------------
# Orientation of ordered triplet (p, q, r)
# Returns:
# 0 → collinear
# 1 → clockwise
# 2 → counterclockwise
# ---------------------------------------------------------
def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    return 1 if val > 0 else 2

# Check if point q lies on segment pr
def on_segment(p, q, r):
    return (min(p[0], r[0]) <= q[0] <= max(p[0], r[0]) and
            min(p[1], r[1]) <= q[1] <= max(p[1], r[1]))

# ---------------------------------------------------------
# Check if segment p1q1 intersects p2q2
# ---------------------------------------------------------
def segments_intersect(p1, q1, p2, q2):
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

    # General case
    if o1 != o2 and o3 != o4:
        return True

    # Special collinear cases
    if o1 == 0 and on_segment(p1, p2, q1):
        return True
    if o2 == 0 and on_segment(p1, q2, q1):
        return True
    if o3 == 0 and on_segment(p2, p1, q2):
        return True
    if o4 == 0 and on_segment(p2, q1, q2):
        return True

    return False

# ---------------------------------------------------------
# Random Test Generator
# ---------------------------------------------------------
def random_segments(n, limit=50):
    segments = []
    for _ in range(n):
        p1 = (random.randint(0, limit), random.randint(0, limit))
        q1 = (random.randint(0, limit), random.randint(0, limit))
        segments.append((p1, q1))
    return segments

# ---------------------------------------------------------
# Check all pairs of segments for intersection
# O(n²) worst-case, expected ~ much less
# ---------------------------------------------------------
def check_all_intersections(segments):
    n = len(segments)
    intersecting_pairs = []

    for i in range(n):
        for j in range(i + 1, n):
            p1, q1 = segments[i]
            p2, q2 = segments[j]
            if segments_intersect(p1, q1, p2, q2):
                intersecting_pairs.append((i, j))

    return intersecting_pairs


# ---------------------------------------------------------
# MAIN DEMO
# ---------------------------------------------------------
if __name__ == "__main__":
    segments = random_segments(10)

    print("Generated Line Segments:")
    for idx, s in enumerate(segments):
        print(f"{idx}: {s}")

    pairs = check_all_intersections(segments)

    print("\nIntersecting Segment Pairs:")
    print(pairs if pairs else "No intersections found")
