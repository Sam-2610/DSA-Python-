def count_rotations(arr, n):
    low = 0
    high = n - 1
    ans = float('inf')  # tracks smallest value found so far
    index = -1           # index of that smallest value = number of rotations

    while low <= high:
        mid = (low + high) // 2

        if arr[low] <= arr[mid]:
            # left half (low to mid) is sorted, so its smallest is arr[low]
            if arr[low] < ans:
                ans = arr[low]
                index = low
            low = mid + 1  # move right to check for a smaller value
        else:
            # right half (mid to high) is sorted, so its smallest is arr[mid]
            if arr[mid] < ans:
                ans = arr[mid]
                index = mid
            high = mid - 1  # move left to check for a smaller value

    return index  # this is the number of times the array was rotated


def main():
    arr = list(map(int, input("Enter the Elements : ").split()))
    n = len(arr)
    print(count_rotations(arr, n))


if __name__ == "__main__":
    main()