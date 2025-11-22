import random

# ---------------------------------------------------
# MONTE CARLO ALGORITHM: Fermat Primality Test
# (Fast, may be wrong with small probability)
# ---------------------------------------------------
def fermat_test(n, k=5):
    if n <= 1:
        return False
    if n == 2:
        return True

    for _ in range(k):
        a = random.randint(2, n - 2)
        # Fermat's Little Theorem
        if pow(a, n - 1, n) != 1:
            return False     # definitely composite

    return True               # probably prime (small error probability)

# ---------------------------------------------------
# LAS VEGAS ALGORITHM: Randomized QuickSort
# (Always correct, runtime is random)
# ---------------------------------------------------
def las_vegas_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    arr2 = arr.copy()
    arr2.remove(pivot)

    left = [x for x in arr2 if x <= pivot]
    right = [x for x in arr2 if x > pivot]

    return las_vegas_sort(left) + [pivot] + las_vegas_sort(right)

# ---------------------------------------------------
# Demo / Example Usage
# ---------------------------------------------------
if __name__ == "__main__":
    print("Monte Carlo vs Las Vegas Algorithms")
    print("----------------------------------")

    # Monte Carlo primality test
    n = 101  # test number
    print("\nTesting primality using Monte Carlo (Fermat’s Test)")
    print("Number:", n)
    print("Is probably prime?", fermat_test(n, k=10))

    # Las Vegas randomized sorting
    arr = [5, 3, 8, 1, 7, 2]
    print("\nSorting using Las Vegas Randomized QuickSort")
    print("Original array:", arr)
    print("Sorted array:", las_vegas_sort(arr.copy()))
