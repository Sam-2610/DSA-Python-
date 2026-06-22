def longest_subarray_with_sum_k():
    arr = []
    n = int(input("Enter the Number of Elements : "))
    for i in range(n):
        x = int(input(f"Enter the Elements {i + 1} : "))
        arr.append(x) # type: ignore

    k = int(input("Enter the Target Sum : "))
    left = 0
    right = 0
    curr_sum = arr[0] # type: ignore
    maxlen = 0

    while right < n:
        # shrink window from left if sum exceeds k
        while left <= right and curr_sum > k:
            curr_sum -= arr[left]   # type: ignore # ✅ subtract, not compare
            left += 1
        
        # check if current window sum equals k
        if curr_sum == k:
            maxlen = max(maxlen, right - left + 1)
        
        # expand window from right
        right += 1                  # ✅ always move right, not in else
        if right < n:
            curr_sum += arr[right] # type: ignore

    print("Longest Subarray Length : ", maxlen)

longest_subarray_with_sum_k()