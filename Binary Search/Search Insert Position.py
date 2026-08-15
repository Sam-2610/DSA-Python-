def search(arr, x, n):
    low = 0
    high = n - 1
    ans = n  # default: if no element >= x is found, answer is n (one past last index)

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] >= x:
            # arr[mid] is a valid candidate for the answer
            ans = mid
            high = mid - 1  # look further left for an even smaller valid index
        else:
            # arr[mid] < x, discard left half including mid
            low = mid + 1

    return ans


def main():
    arr = list(map(int, input("Enter the Elements : ").split()))
    x = int(input("Enter the Target Element : "))
    n = len(arr)
    print(search(arr, x, n))


if __name__ == "__main__":
    main()