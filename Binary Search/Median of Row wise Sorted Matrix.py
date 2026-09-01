def upper_bound(arr, x, n):
    """
    Return the count of elements in sorted arr[0:n] that are <= x.
    (Equivalently: the index of the first element strictly greater than x,
    which is the same thing for a sorted array -- hence the name
    "upper_bound", matching C++'s std::upper_bound semantics.)
    """
    low = 0
    high = n - 1
    ans = n  # default: every element is <= x

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] > x:
            ans = mid       # candidate first-index-greater-than-x
            high = mid - 1  # look for an even earlier one
        else:
            low = mid + 1
    return ans


def count_small_equal(mat, n, m, x):
    """
    Count how many elements of the whole matrix are <= x, by summing
    upper_bound() over every row (each row must be sorted ascending).
    """
    cnt = 0
    for i in range(n):
        cnt += upper_bound(mat[i], x, m)
    return cnt


def median(mat, n, m):
    """
    Find the median of a matrix where every row is individually sorted
    ascending. Assumes n * m is odd, so there's a single middle value
    once all elements are considered together.

    Binary searches over the VALUE range (not indices): for a candidate
    value `mid`, count how many matrix elements are <= mid. The median
    is the smallest value for which that count exceeds half the total
    element count -- i.e. the smallest value that "covers" the middle
    position once everything is conceptually merged and sorted.
    """
    low = float('inf')
    high = float('-inf')

    # The answer must lie between the smallest first-element and the
    # largest last-element across all rows (rows are sorted ascending,
    # so each row's min is its first entry, max is its last entry).
    for i in range(n):
        low = min(low, mat[i][0])
        high = max(high, mat[i][m - 1])

    req = (n * m) // 2  # index of the median in the fully merged, sorted array
    while low <= high:
        mid = (low + high) // 2
        small_equal = count_small_equal(mat, n, m, mid)

        if small_equal <= req:
            # Not enough elements are <= mid yet to reach the median
            # position -> the median must be larger.
            low = mid + 1
        else:
            # More than enough elements are <= mid -> the median could
            # be mid itself or something smaller.
            high = mid - 1
    # When the loop ends, low is the smallest value whose count of
    # elements <= it exceeds req -- that value is the median.
    return low


def main():
    n = int(input("Enter the Number of Rows : "))
    m = int(input("Enter the Number of Columns : "))
    mat = []
    for i in range(n):
        rows = list(map(int, input("Enter the Element : ").split()))
        mat.append(rows)

    result = median(mat, n, m)
    print(result)


if __name__ == "__main__":
    main()