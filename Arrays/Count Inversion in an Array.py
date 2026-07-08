# WAP to Count Inversions in an Array using Merge Sort.
# An inversion is a pair (i, j) such that i < j but arr[i] > arr[j].

def merge_sort_count(arr):
    # Base case — a single element is already sorted, 0 inversions
    if len(arr) <= 1:
        return arr, 0

    # Step 1: DIVIDE — find the middle and split
    mid = len(arr) // 2
    left, left_inv = merge_sort_count(arr[:mid])    # sort left half + count its inversions
    right, right_inv = merge_sort_count(arr[mid:])  # sort right half + count its inversions

    # Step 2: MERGE — combine both sorted halves, counting cross inversions along the way
    merged, cross_inv = merge_count(left, right)

    # Total inversions = inversions within left + within right + across the merge
    total_inv = left_inv + right_inv + cross_inv

    return merged, total_inv


def merge_count(left, right):
    sorted_arr = []
    i = 0    # pointer for left
    j = 0    # pointer for right
    inv_count = 0

    # Compare elements from both halves, pick the smaller one
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            # left[i] > right[j] means left[i], left[i+1], ..., left[end]
            # are ALL greater than right[j] (since left is already sorted)
            # so each of them forms an inversion with right[j]
            sorted_arr.append(right[j])
            inv_count += len(left) - i   # count all remaining left elements at once
            j += 1

    # Append any remaining elements (no more inversions possible here,
    # since one side is already fully merged in)
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])

    return sorted_arr, inv_count


# Main — take array input from the user
n = int(input("Enter number of elements: "))
arr = list(map(int, input(f"Enter {n} elements separated by space: ").split()))

sorted_result, inversions = merge_sort_count(arr)
print("Sorted Array :", sorted_result)
print("Inversion Count :", inversions)