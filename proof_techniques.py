# ---------------------------------------------------------
# Factorial (Induction Proof Example)
# ---------------------------------------------------------
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

# ---------------------------------------------------------
# Fibonacci (Recursive)
# ---------------------------------------------------------
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# ---------------------------------------------------------
# Binary Search (works only on sorted array)
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
# MAIN (User Input Only)
# ---------------------------------------------------------
if __name__ == "__main__":

    print("=== Factorial Using Induction ===")
    n = int(input("Enter n for factorial: "))
    print("factorial(", n, ") =", factorial(n))

    print("\n=== Fibonacci (Recursive) ===")
    f = int(input("Enter n for fibonacci: "))
    print("fibonacci(", f, ") =", fibonacci(f))

    print("\n=== Binary Search (Contradiction Example) ===")
    arr = list(map(int, input("Enter sorted array (space-separated): ").split()))
    key = int(input("Enter value to search: "))
    print("Binary Search Result:", binary_search(arr, key))

    print("\n=== Binary Search on Unsorted Array (Expected Wrong Behaviour) ===")
    arr2 = list(map(int, input("Enter UNSORTED array (space-separated): ").split()))
    key2 = int(input("Enter value to search: "))
    print("Binary Search Result:", binary_search(arr2, key2))
