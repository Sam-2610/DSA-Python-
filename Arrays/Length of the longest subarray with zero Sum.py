def maxLen(A: list[int], n: int) -> int:
    mpp = {}   # prefix_sum -> first index where it occurred
    maxi = 0   # length of longest zero-sum subarray found so far
    s = 0      # running prefix sum

    for i in range(n):
        s += A[i]

        if s == 0:
            # whole subarray from 0 to i sums to 0
            maxi = i + 1
        elif s in mpp:
            # same prefix sum seen before -> elements between are zero-sum
            maxi = max(maxi, i - mpp[s])
        else:
            # store first occurrence only (keeps subarray as long as possible)
            mpp[s] = i

    return maxi


A = [9, -3, 3, -1, 6, -5]
print(maxLen(A, len(A)))  # Time: O(n), Space: O(n)