# WAP to perform Quick Sort.

def quick_sort(arr, low, high):
    # Base case — if low crosses high, nothing to sort
    if low < high:

        # Step 1: PARTITION — place pivot in correct position
        pivot_index = partition(arr, low, high)

        # Step 2: RECURSE — sort left and right of pivot
        quick_sort(arr, low, pivot_index - 1)   # left side
        quick_sort(arr, pivot_index + 1, high)  # right side


def partition(arr, low, high):
    pivot = arr[high]   # pick last element as pivot
    i = low - 1         # i tracks the boundary of smaller elements

    for j in range(low, high):
        if arr[j] <= pivot:       # current element belongs on left
            i += 1
            arr[i], arr[j] = arr[j], arr[i]   # swap into left region

    # Place pivot in its correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1   # return pivot's final index


# Main
arr = [5, 3, 8, 1]
quick_sort(arr, 0, len(arr) - 1)
print("Sorted Array :", arr)