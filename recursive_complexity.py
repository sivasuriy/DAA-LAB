import random
import time

# ---------------------------------------------------------
# Merge Sort → O(n log n)
# Recurrence: T(n) = 2T(n/2) + O(n)
# Using Master Theorem → T(n) = O(n log n)
# ---------------------------------------------------------
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    L = merge_sort(arr[:mid])
    R = merge_sort(arr[mid:])

    return merge(L, R)

def merge(L, R):
    result = []
    i = j = 0

    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            result.append(L[i])
            i += 1
        else:
            result.append(R[j])
            j += 1

    result.extend(L[i:])
    result.extend(R[j:])
    return result


# ---------------------------------------------------------
# Quick Sort → Average O(n log n), Worst O(n²)
# Recurrence (best/avg): T(n) = T(n/2) + T(n/2) + O(n)
# ---------------------------------------------------------
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    mid  = [x for x in arr if x == pivot]
    right= [x for x in arr if x > pivot]

    return quick_sort(left) + mid + quick_sort(right)


# ---------------------------------------------------------
# BST Insert (Recursive)
# Recurrence: T(h) = T(h-1) + O(1)
# Worst-case height = n → O(n)
# Best/avg = O(log n) for balanced tree
# ---------------------------------------------------------
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def bst_insert(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = bst_insert(root.left, key)
    else:
        root.right = bst_insert(root.right, key)
    return root


# ---------------------------------------------------------
# Time Measuring Utility
# ---------------------------------------------------------
def measure_time(func, arr):
    start = time.time()
    func(arr)
    return time.time() - start


# ---------------------------------------------------------
# MAIN
# ---------------------------------------------------------
if __name__ == "__main__":
    n = 50_000
    arr = [random.randint(1, 100000) for _ in range(n)]

    print("\nCO1 – Program 2: Recursive Algorithm Complexity")
    print("------------------------------------------------\n")

    # Measure Merge Sort
    t1 = measure_time(merge_sort, arr.copy())
    print("Merge Sort Time:", t1, "seconds")

    # Measure Quick Sort
    t2 = measure_time(quick_sort, arr.copy())
    print("Quick Sort Time:", t2, "seconds")

    # Measure BST insertion time
    root = None
    start = time.time()
    for x in arr:
        root = bst_insert(root, x)
    t3 = time.time() - start
    print("BST Insertion Time:", t3, "seconds")

    print("\n--- Complexity Summary ---")
    print("Merge Sort      → O(n log n)  (Master Method Case 2)")
    print("Quick Sort      → O(n log n) avg, O(n²) worst")
    print("BST Insertion   → O(log n) avg, O(n) worst (unbalanced)")
