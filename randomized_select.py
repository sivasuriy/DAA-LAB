import random

# ---------------------------------------------------
# Deterministic Partition (Used by QuickSelect)
# ---------------------------------------------------
def partition(arr, low, high):
    pivot = arr[high]
    i = low
    for j in range(low, high):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i

# ---------------------------------------------------
# Deterministic QuickSelect (find kth smallest)
# ---------------------------------------------------
def quickselect(arr, low, high, k):
    if low == high:
        return arr[low]

    pivot_index = partition(arr, low, high)

    if k == pivot_index:
        return arr[k]
    elif k < pivot_index:
        return quickselect(arr, low, pivot_index - 1, k)
    else:
        return quickselect(arr, pivot_index + 1, high, k)

# ---------------------------------------------------
# Randomized Partition (swap random pivot to end)
# ---------------------------------------------------
def randomized_partition(arr, low, high):
    rand_index = random.randint(low, high)
    arr[rand_index], arr[high] = arr[high], arr[rand_index]
    return partition(arr, low, high)

# ---------------------------------------------------
# Randomized-Select (Expected O(n))
# ---------------------------------------------------
def randomized_select(arr, low, high, k):
    if low == high:
        return arr[low]

    pivot_index = randomized_partition(arr, low, high)

    if k == pivot_index:
        return arr[k]
    elif k < pivot_index:
        return randomized_select(arr, low, pivot_index - 1, k)
    else:
        return randomized_select(arr, pivot_index + 1, high, k)

# ---------------------------------------------------
# Example usage
# ---------------------------------------------------
if __name__ == "__main__":
    arr = [random.randint(1, 1000) for _ in range(20)]
    k = 5  # 6th smallest element (0-indexed)

    print("Array:", arr)
    print("k =", k)

    print("\nDeterministic QuickSelect:", 
          quickselect(arr.copy(), 0, len(arr)-1, k))

    print("Randomized Select:", 
          randomized_select(arr.copy(), 0, len(arr)-1, k))
