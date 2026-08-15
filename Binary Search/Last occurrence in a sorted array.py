def lower_bound(arr, n, x):
    low = 0
    high = n - 1
    ans = n  # default: if no element >= x is found, lower bound is n (one past last index)

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] >= x:
            # arr[mid] is a valid candidate for the answer
            ans = mid
            high = mid - 1  # look further left for an even smaller valid index
        else:
            # arr[mid] is too small, discard left half including mid
            low = mid + 1

    return ans


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


def first_and_last(arr, n, x):
    lb = lower_bound(arr, n, x)

    # x doesn't exist in arr at all: either lb ran past the end,
    # or lb is valid but doesn't actually equal x
    if lb == n or arr[lb] != x:
        return (-1, -1)

    ub = upper_bound(arr, x, n)  # fixed: correct parameter order
    return (lb, ub - 1)  # fixed: tuple instead of set, so both values are preserved


def main():
    arr = list(map(int, input("Enter the Elements : ").split()))
    n = len(arr)
    x = int(input("Enter the Target Element : "))
    print(first_and_last(arr, n, x))


if __name__ == "__main__":
    main()