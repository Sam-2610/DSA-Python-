def search_element(mat, target):
    """
    Search for `target` in a matrix where each row is sorted left-to-right
    AND each column is sorted top-to-bottom (rows/columns independently
    sorted -- not necessarily fully flattened-sorted like a strictly
    row-major sorted matrix).

    "Staircase search": start at the top-right corner.
      - If the current value equals target, found it.
      - If the current value is smaller than target, the whole current
        column above is even smaller (column is sorted top-to-bottom),
        so target can't be in this column -> move down a row.
      - If the current value is larger than target, the whole rest of
        this row to the right is even larger (row is sorted left-to-right),
        so target can't be in the rest of this row -> move left a column.

    Each step eliminates a full row or column, so this runs in O(n + m).
    """
    if not mat or not mat[0]:
        return False

    n = len(mat)
    m = len(mat[0])

    row = 0
    col = m - 1  # start at top-right corner

    while row < n and col >= 0:
        if mat[row][col] == target:
            return True
        elif mat[row][col] < target:
            row = row + 1  # eliminate current column, move down
        else:
            col = col - 1  # eliminate current row, move left
    return False


def main():
    n = int(input("Enter the Number of rows : "))
    m = int(input("Enter teh Number of Columns : "))
    target = int(input("Enter the target Element : "))
    mat = []
    for i in range(n):
        rows = list(map(int, input("Enter the Elements : ").split()))
        mat.append(rows)
    result = search_element(mat, target)
    print(result)


if __name__ == "__main__":
    main()