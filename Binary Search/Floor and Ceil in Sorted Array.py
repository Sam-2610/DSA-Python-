def find_floor(arr, x):
    low, high = 0, len(arr) - 1
    ans = -1  # default: no element <= x found

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] <= x:
            ans = arr[mid]  # potential floor, but check right side for a larger one
            low = mid + 1
        else:
            high = mid - 1  # arr[mid] too big, discard right half including mid

    return ans


def find_ceil(arr, x):
    low, high = 0, len(arr) - 1
    ans = -1  # default: no element >= x found

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] >= x:
            ans = arr[mid]  # potential ceil, but check left side for a smaller one
            high = mid - 1
        else:
            low = mid + 1  # arr[mid] too small, discard left half including mid

    return ans


def get_floor_and_ceil(arr, x):
    floor = find_floor(arr, x)
    ceil = find_ceil(arr, x)
    return floor, ceil


def main():
    arr = list(map(int, input("Enter the Elements : ").split()))
    x = int(input("Enter the Target Element : "))
    print(get_floor_and_ceil(arr, x))


if __name__ == "__main__":
    main()