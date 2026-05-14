# WAP to Perform Merge Sort.

def merge_sort(arr):
    # Base case — a single element is already sorted
    if len(arr) <= 1:
        return arr

    # Step 1: DIVIDE — find the middle and split
    mid = len(arr) // 2
    left  = merge_sort(arr[:mid])   # sort left half recursively
    right = merge_sort(arr[mid:])   # sort right half recursively

    # Step 2: MERGE — combine both sorted halves
    return merge(left, right)


def merge(left, right):
    sorted_arr = []
    i = 0   # pointer for left
    j = 0   # pointer for right

    # Compare elements from both halves, pick the smaller one
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1

    # Append any remaining elements
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])

    return sorted_arr


# Main
arr = [5, 3, 8, 1]
result = merge_sort(arr)
print("Sorted Array :", result)