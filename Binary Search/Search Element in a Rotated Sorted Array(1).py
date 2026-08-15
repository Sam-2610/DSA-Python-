def search(arr, n, x):
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == x:
            return mid  # found target

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
                high = mid - 1  # fixed: was `high = mid + 1`

    return -1  # target not found


def main():
    arr = list(map(int, input("Enter the Elements : ").split()))
    n = len(arr)
    x = int(input("Enter the Target Element:"))
    print(search(arr, n, x))


if __name__ == "__main__":
    main()