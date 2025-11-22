import random
import time

# ------------------------------
# Deterministic QuickSort
# ------------------------------
def quicksort_det(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]  # fixed pivot → deterministic
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    return quicksort_det(left) + [pivot] + quicksort_det(right)

# ------------------------------
# Randomized QuickSort
# ------------------------------
def quicksort_rand(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    arr2 = arr.copy()
    arr2.remove(pivot)
    left = [x for x in arr2 if x <= pivot]
    right = [x for x in arr2 if x > pivot]
    return quicksort_rand(left) + [pivot] + quicksort_rand(right)

# ------------------------------
# Compare execution times
# ------------------------------
def compare_sorts(n):
    arr = [random.randint(1, 100000) for _ in range(n)]

    # deterministic
    t1 = time.time()
    quicksort_det(arr.copy())
    det_time = time.time() - t1

    # randomized
    t2 = time.time()
    quicksort_rand(arr.copy())
    rand_time = time.time() - t2

    return det_time, rand_time

# ------------------------------
# Demo
# ------------------------------
if __name__ == "__main__":
    n = 2000

    det, rnd = compare_sorts(n)

    print("QuickSort Performance Comparison")
    print("--------------------------------")
    print("Array size:", n)
    print("Deterministic QuickSort time:", det)
    print("Randomized QuickSort time:", rnd)
