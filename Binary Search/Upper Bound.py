def upper_bound(arr, x, n):
    low = 0
    high = n - 1
    ans = n  # default: if no element > x is found, upper bound is n (one past last index)

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] > x:
            # arr[mid] is a valid candidate (strictly greater than x)
            ans = mid
            high = mid - 1  # look further left for an even smaller valid index
        else:
            # arr[mid] <= x, discard left half including mid
            low = mid + 1

    return ans


def main():
    arr = list(map(int, input("Enter the Elements : ").split()))
    n = len(arr)
    x = int(input("Enter the Target Element : "))
    print(upper_bound(arr, x, n))


if __name__ == "__main__":
    main()