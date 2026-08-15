def search(arr, n, x):
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == x:
            return True  # found target

        # edge case: can't tell which half is sorted when both ends equal mid
        # (e.g. [3, 1, 3, 3, 3] — arr[low]==arr[mid]==arr[high] gives no info)
        if arr[low] == arr[mid] and arr[mid] == arr[high]:
            low = low + 1    # shrink from both sides
            high = high - 1  # and just keep searching narrower range
            continue

        if arr[low] <= arr[mid]:
            # left half (low to mid) is sorted
            if arr[low] <= x <= arr[mid]:
                # target lies within the sorted left half
                high = mid - 1
            else:
                # target must be in the right half
                low = mid + 1
        else:
            # right half (mid to high) is sorted
            if arr[mid] <= x <= arr[high]:
                # target lies within the sorted right half
                low = mid + 1
            else:
                # target must be in the left half
                high = mid - 1

    return False  # target not found


def main():
    arr = list(map(int, input("Enter the Elements : ").split()))
    x = int(input("Enter the Target Element : "))
    n = len(arr)
    print(search(arr, n, x))


if __name__ == "__main__":
    main()