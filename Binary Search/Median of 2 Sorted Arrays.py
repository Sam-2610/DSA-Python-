def median(arr1, arr2):
    """
    Find the median of two sorted arrays in O(log(min(n1, n2))) time
    using binary search on the smaller array to find a valid partition.
    """
    n1 = len(arr1)
    n2 = len(arr2)

    # Always binary-search on the smaller array for O(log(min(n1,n2))) time
    # and so that (n1 + n2 + 1)//2 - mid1 never goes negative or out of range.
    if n1 > n2:
        return median(arr2, arr1)

    low = 0
    high = n1
    # left = size of the "left half" combined across both arrays.
    # For an odd total, the left half has one extra element (the median).
    left = (n1 + n2 + 1) // 2
    n = n1 + n2

    while low <= high:
        # mid1 = how many elements of arr1 go into the left half
        mid1 = (low + high) >> 1
        # mid2 = how many elements of arr2 go into the left half
        # (whatever's left after taking mid1 from arr1)
        mid2 = left - mid1

        # l1/l2 = last element of the left half from arr1/arr2 (-inf if none)
        # r1/r2 = first element of the right half from arr1/arr2 (+inf if none)
        l1 = float('-inf')
        l2 = float('-inf')
        r1 = float('inf')   # FIX: was float('-inf') — this was the bug.
        r2 = float('inf')

        if mid1 < n1:
            r1 = arr1[mid1]

        if mid2 < n2:
            r2 = arr2[mid2]

        if mid1 - 1 >= 0:
            l1 = arr1[mid1 - 1]

        if mid2 - 1 >= 0:
            l2 = arr2[mid2 - 1]

        # Valid partition: every left element <= every right element
        if l1 <= r2 and l2 <= r1:
            if n % 2 == 1:
                # Odd total: median is the max of the left half
                return max(l1, l2)
            else:
                # Even total: median is avg of max(left) and min(right)
                return (max(l1, l2) + min(r1, r2)) / 2.0
        elif l1 > r2:
            # Left part of arr1 too big -> move partition left in arr1
            high = mid1 - 1
        else:
            # l2 > r1: left part of arr2 too big -> move partition right in arr1
            low = mid1 + 1

    # With the fix above, a valid partition is always found for non-empty,
    # correctly sorted input, so this line should not be reached.
    # (Kept only as a defensive fallback.)
    return 0


def main():
    arr1 = list(map(int, input("Enter the Element : ").split()))
    arr2 = list(map(int, input("Enter the Element : ").split()))
    print("Median : ", median(arr1, arr2))


if __name__ == "__main__":
    main()