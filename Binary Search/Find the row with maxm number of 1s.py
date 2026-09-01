def lower_bound(arr, n, x):
    """
    Return the index of the first element in arr[0:n] that is >= x.
    If no such element exists, return n.
    Standard binary search, requires arr to be sorted.
    """
    low = 0
    high = n - 1
    ans = n  # default: no element >= x found

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] >= x:
            ans = mid       # candidate answer; try to find an earlier one
            high = mid - 1
        else:
            low = mid + 1
    return ans


def row_with_max_1s(mat, n, m):
    """
    Given an n x m binary matrix where each row is sorted (0s then 1s),
    return the index of the row with the most 1s (-1 if all rows are 0s).
    """
    cnt_max = 0
    index = -1

    for i in range(n):
        # First index in this row where a 1 appears (via binary search,
        # since the row is sorted). Count of 1s = m - first_one.
        first_one = lower_bound(mat[i], m, 1)
        cnt_ones = m - first_one

        # FIX: this comparison must happen inside the loop, once per row.
        # Originally it was outside the loop (unindented), so it only ran
        # once after the loop ended, comparing just the LAST row's count
        # instead of tracking the max across all rows.
        if cnt_ones > cnt_max:
            cnt_max = cnt_ones
            index = i

    return index


def main():
    n = int(input("Enter the Number of rows : "))
    m = int(input("Enter the Number of columns : "))
    mat = []
    for i in range(n):
        row = list(map(int, input(f"Enter the elements of row {i}").split()))
        mat.append(row)
    answer = row_with_max_1s(mat, n, m)
    print("Row with max 1s : ", answer)


if __name__ == "__main__":
    main()