def kth_element(arr1, arr2, k):
    """
    Find the k-th smallest element (1-indexed) across two sorted arrays,
    in O(log(min(n1, n2))) time via binary search on a partition.

    NOTE: originally this function took (arr1, arr2, n1, n2, k), but n1/n2
    were immediately overwritten by len(arr1)/len(arr2) anyway, and main()
    called it with only 3 args (arr1, arr2, k) -> TypeError at runtime.
    The unused n1/n2 parameters have been removed to match how it's called.
    """
    n1 = len(arr1)
    n2 = len(arr2)

    # Always binary-search on the smaller array for O(log(min(n1,n2))) time.
    if n1 > n2:
        return kth_element(arr2, arr1, k)

    # mid1 (elements taken from arr1 into the left partition) must satisfy:
    #   - mid2 = k - mid1 can't exceed n2  ->  mid1 >= k - n2
    #   - mid1 can't exceed n1
    #   - mid1 can't exceed k (mid2 can't go negative)
    low = max(k - n2, 0)
    high = min(k, n1)
    left = k  # total elements that must end up in the left partition

    while low <= high:
        mid1 = (low + high) >> 1   # elements of arr1 in the left partition
        mid2 = left - mid1         # elements of arr2 in the left partition

        # l1/l2 = last element of the left half from arr1/arr2 (-inf if none)
        # r1/r2 = first element of the right half from arr1/arr2 (+inf if none)
        l1 = float('-inf')
        l2 = float('-inf')
        r1 = float('inf')
        r2 = float('inf')

        if mid1 < n1:
            r1 = arr1[mid1]

        if mid2 < n2:
            r2 = arr2[mid2]

        if mid1 > 0:
            l1 = arr1[mid1 - 1]

        if mid2 > 0:
            l2 = arr2[mid2 - 1]

        # Valid partition: every left element <= every right element.
        # The k-th smallest is then the largest element in the left half.
        if l1 <= r2 and l2 <= r1:
            return max(l1, l2)
        elif l1 > r2:
            # Left part of arr1 too big -> shrink it
            high = mid1 - 1
        else:
            # l2 > r1: left part of arr1 too small -> grow it
            low = mid1 + 1

    # Reached only if k is out of valid range (k < 1 or k > n1 + n2).
    return -1


def main():
    arr1 = list(map(int, input("Enter the Elements : ").split()))
    arr2 = list(map(int, input("Enter the Element : ").split()))
    k = int(input("Enter the Target Element : "))
    print(kth_element(arr1, arr2, k))


if __name__ == "__main__":
    main()