def count_subarrays(arr, max_sum):
    subarrays = 1        # at least one subarray needed
    current_sum = 0       # running sum of the current subarray

    for num in arr:
        if current_sum + num <= max_sum:
            # current element still fits within this subarray's limit
            current_sum += num
        else:
            # limit exceeded, start a new subarray with this element
            subarrays += 1
            current_sum = num

    return subarrays  # minimum subarrays needed to keep every sum <= max_sum


def split_array_largest_sum(arr, k):
    if k > len(arr):
        return -1  # can't split into more subarrays than there are elements

    low = max(arr)   # smallest possible answer: at least the largest single element
    high = sum(arr)  # largest possible answer: one subarray containing everything

    while low <= high:
        mid = (low + high) // 2
        subarrays = count_subarrays(arr, mid)  # subarrays needed if max sum allowed is `mid`

        if subarrays > k:
            # too many subarrays needed, limit too tight -> raise it
            low = mid + 1
        else:
            # fits within k subarrays (or fewer) -> try to shrink the limit further
            high = mid - 1

    return low  # fixed: added return, gives the minimum largest-sum achievable with k splits


def main():
    arr = list(map(int, input("Enter the Elements : ").split()))
    k = int(input("Enter the number of subarrays : "))
    result = split_array_largest_sum(arr, k)
    print("Minimum possible largest sum", result)


if __name__ == "__main__":
    main()