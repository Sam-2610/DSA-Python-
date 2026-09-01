def find_index(mat, n, m, col):
    """
    Return the row index of the maximum value in column `col`.
    """
    max_value = -1
    index = -1

    for i in range(n):
        if mat[i][col] > max_value:
            # FIX: was `mat[i][0]` (always column 0), which desyncs
            # max_value from the comparison above whenever col != 0,
            # and can make this return the wrong row.
            max_value = mat[i][col]
            index = i
    return index


def find_peak_grind(mat):
    """
    Find a 2D peak: an element that is >= its left, right, top, and
    bottom neighbors. (This implementation only checks left/right,
    which is sufficient because within the chosen column it always
    looks at the column's maximum -- see below.)

    Binary search over columns:
      - For the middle column, find the row with the max value in
        that column (this row's value is automatically >= its
        top/bottom neighbors in that column, since it's the max).
      - Compare that value to its left/right neighbors:
          - If it's greater than both -> it's a peak, done.
          - If the left neighbor is bigger -> a peak must exist
            somewhere to the left -> search the left half.
          - Otherwise the right neighbor is bigger (or equal) ->
            search the right half.
    Runs in O(n log m): each of the O(log m) steps scans a column
    of height n.
    """
    n = len(mat)
    m = len(mat[0])

    low = 0
    high = m - 1

    while low <= high:
        mid = (low + high) // 2
        max_row_index = find_index(mat, n, m, mid)
        current = mat[max_row_index][mid]
        left = mat[max_row_index][mid - 1] if mid - 1 >= 0 else -1
        right = mat[max_row_index][mid + 1] if mid + 1 < m else -1

        if current > left and current > right:
            return (max_row_index, mid)
        elif current < left:
            high = mid - 1   # bigger value to the left -> peak is that way
        else:
            low = mid + 1    # bigger (or equal) value to the right
    return (-1, -1)


def main():
    n = int(input("Enter the Number of rows : "))
    m = int(input("Enter the Number of Columns : "))
    mat = []
    for i in range(n):
        rows = list(map(int, input("Enter the Elements : ").split()))
        mat.append(rows)

    result = find_peak_grind(mat)
    print("Peak Position", result)


if __name__ == "__main__":
    main()