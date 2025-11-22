import time
import random

# ---------------------------------------------------------
# Linear Search  → O(n)
# ---------------------------------------------------------
def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1


# ---------------------------------------------------------
# Binary Search → O(log n)
# ---------------------------------------------------------
def binary_search(arr, key):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1


# ---------------------------------------------------------
# Sum of first n numbers (Iterative) → O(n)
# ---------------------------------------------------------
def sum_iterative(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


# ---------------------------------------------------------
# Sum of first n numbers (Recursive) → O(n)
# ---------------------------------------------------------
def sum_recursive(n):
    if n == 0:
        return 0
    return n + sum_recursive(n - 1)


# ---------------------------------------------------------
# Measure execution time
# ---------------------------------------------------------
def measure_time(func, *args):
    start = time.time()
    func(*args)
    return time.time() - start


# ---------------------------------------------------------
# MAIN
# ---------------------------------------------------------
if __name__ == "__main__":
    sizes = [10_000, 50_000, 1_00_000]

    print("\nTIME COMPLEXITY ANALYSIS (CO1 - Program 1)")
    print("------------------------------------------\n")

    for n in sizes:
        arr = list(range(n))
        key = random.randint(0, n - 1)

        print(f"Input Size: {n}")

        # Linear Search
        t1 = measure_time(linear_search, arr, key)
        print("Linear Search Time:", t1, "seconds")

        # Binary Search
        t2 = measure_time(binary_search, arr, key)
        print("Binary Search Time:", t2, "seconds")

        # Sum iterative
        t3 = measure_time(sum_iterative, n)
        print("Sum Iterative Time:", t3, "seconds")

        # Sum recursive
        t4 = measure_time(sum_recursive, n)
        print("Sum Recursive Time:", t4, "seconds")

        print("------------------------------------------")
