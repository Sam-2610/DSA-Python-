def missingk(arr, n, k):
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2

        # number of missing positives up to arr[mid]:
        # if nothing were missing, arr[mid] would equal (mid + 1) (1-indexed count)
        # so the gap between actual value and expected value = count of missing numbers so far
        missing = arr[mid] - (mid + 1)

        if missing < k:
            # not enough missing numbers yet, k-th missing is further right
            low = mid + 1
        else:
            # already passed (or reached) k missing numbers, look further left
            high = mid - 1

    return k + high + 1  # reconstruct the k-th missing number from final `high` position


def main():
    arr = list(map(int, input("Enter the Element : ").split()))
    n = len(arr)
    k = int(input("Enter the Target Element : "))
    print(missingk(arr, n, k))


if __name__ == "__main__":
    main()