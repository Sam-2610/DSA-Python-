def peak_element(arr, n):
    if n == 1:
        return 0  # only one element, trivially a peak

    if arr[0] > arr[1]:
        return 0  # first element is a peak (no left neighbor to compare)

    if arr[n - 1] > arr[n - 2]:
        return n - 1  # last element is a peak (no right neighbor to compare)

    low = 1
    high = n - 2  # only check interior elements; edges already handled above

    while low <= high:
        mid = (low + high) // 2  # fixed: parentheses ensure correct midpoint

        if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
            # mid is greater than both neighbors -> it's a peak
            return mid
        elif arr[mid] > arr[mid - 1]:
            # still climbing upward -> peak must be to the right
            low = mid + 1
        else:
            # descending -> peak must be to the left
            high = mid - 1

    return -1  # shouldn't be reached if a peak is guaranteed to exist


def main():
    arr = list(map(int, input("Enter the Elements : ").split()))
    n = len(arr)
    print(peak_element(arr, n))


if __name__ == "__main__":
    main()