# ---------------------------------------------------------
# Subset Sum (Recursive Backtracking)
# ---------------------------------------------------------
def subset_sum(nums, target, index=0, current=None):
    if current is None:
        current = []

    # If target reached → success
    if target == 0:
        return current.copy()

    # If no numbers left or target < 0 → fail
    if index >= len(nums) or target < 0:
        return None

    # Include nums[index]
    current.append(nums[index])
    result = subset_sum(nums, target - nums[index], index + 1, current)
    if result:
        return result

    # Exclude nums[index]
    current.pop()
    return subset_sum(nums, target, index + 1, current)


# ---------------------------------------------------------
# Reduction: Subset Sum → Partition Problem
# Partition requires splitting array into 2 equal-sum sets
# ---------------------------------------------------------
def can_partition(nums):
    total = sum(nums)
    if total % 2 != 0:
        return False, None

    target = total // 2
    result = subset_sum(nums, target)
    if result:
        return True, result
    return False, None


# ---------------------------------------------------------
# MAIN
# ---------------------------------------------------------
if __name__ == "__main__":
    nums = [3, 1, 5, 9, 12]
    target = 9

    print("Numbers:", nums)
    print("Target Sum:", target)

    print("\n--- Subset Sum (Backtracking) ---")
    subset = subset_sum(nums, target)
    if subset:
        print("Subset Found:", subset)
    else:
        print("No subset matches target.")

    print("\n--- Reduction to Partition Problem ---")
    possible, subset_part = can_partition(nums)
    if possible:
        print("Partition possible!")
        print("One subset:", subset_part)
        print("Other subset:", [x for x in nums if x not in subset_part])
    else:
        print("Partition NOT possible.")
