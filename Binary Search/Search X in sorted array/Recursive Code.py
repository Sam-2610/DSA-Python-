def search(arr, low, high, target):
    # base case: search space exhausted, target not found
    if low > high:
        return -1

    mid = (low + high) // 2  # middle index of current search range

    if arr[mid] == target:
        # found the target
        return mid
    elif target > arr[mid]:
        # target must be in the right half (if it exists)
        return search(arr, mid + 1, high, target)
    else:
        # target must be in the left half (if it exists)
        return search(arr, low, mid - 1, target)


def search2(arr, target):
    # wrapper: kicks off recursion with the full array range
    return search(arr, 0, len(arr) - 1, target)