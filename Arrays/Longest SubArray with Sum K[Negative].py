def longest_subarray_with_sum_k():
    arr = []
    n = int(input("Enter the Number of Elements : "))
    for i in range(n):
        x = int(input(f"Enter the Elements {i + 1} : "))
        arr.append(x) # type: ignore

    k = int(input("Enter the Target Sum : "))
    
    prefix_sum = 0
    maxlen = 0
    mpp = {}          # hashmap stores {prefix_sum : index}

    for i in range(n):
        prefix_sum += arr[i] # type: ignore

        # case 1 : sum from index 0 to i equals k
        if prefix_sum == k:
            maxlen = max(maxlen, i + 1)

        # case 2 : check if (prefix_sum - k) exists in map
        remainder = prefix_sum - k # type: ignore
        if remainder in mpp:
            maxlen = max(maxlen, i - mpp[remainder]) # type: ignore

        # store prefix_sum only if not already present
        if prefix_sum not in mpp:
            mpp[prefix_sum] = i     # store first occurrence only

    print("Longest Subarray Length : ", maxlen)

longest_subarray_with_sum_k()