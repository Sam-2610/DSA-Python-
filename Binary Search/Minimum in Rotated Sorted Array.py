def minmum(arr, n):
    low = 0
    high = n - 1
    ans = float('inf')  # tracks smallest candidate found so far

    while low <= high:
        mid = (low + high) // 2

        if arr[low] <= arr[mid]:
            # left half (low to mid) is sorted, so its smallest element is arr[low]
            ans = min(ans, arr[low])
            low = mid + 1  # move to the right half to check for a smaller value
        else:
            # right half (mid to high) is sorted, so its smallest element is arr[mid]
            high = mid - 1  # move to the left half to check for a smaller value
            ans = min(ans, arr[mid])

    return ans


def main():
    arr = list(map(int, input("Enter the Elements : ").split()))
    n = len(arr)
    print(minmum(arr, n))


if __name__ == "__main__":
    main()