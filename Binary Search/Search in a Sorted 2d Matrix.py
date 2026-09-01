def search_matrix(mat, target):
    """
    Search for `target` in a matrix that is fully sorted when read row by
    row left-to-right, top-to-bottom (i.e. each row is sorted, and each
    row's first element is greater than the previous row's last element).

    Treats the matrix as one flattened sorted array of size n*m and does
    a standard binary search over the virtual index `mid`, converting
    mid -> (row, col) via divmod. O(log(n*m)) time.
    """
    if len(mat) == 0:
        return False

    n = len(mat)
    m = len(mat[0])

    lo = 0
    hi = (n * m) - 1

    while lo <= hi:
        mid = lo + (hi - lo) // 2
        row = mid // m   # which row this flattened index falls in
        col = mid % m    # which column within that row

        if mat[row][col] == target:
            return True
        elif mat[row][col] < target:
            lo = mid + 1   # target is further right/down -> search right half
        else:
            hi = mid - 1   # target is further left/up -> search left half
    return False


def main():
    # FIX: target is a single integer, not a list of numbers, so it must
    # NOT be .split() before int(). Originally this was:
    #   target = int(input("Enter the Target : ").split())
    # which raises TypeError, since .split() returns a list and int()
    # can't convert a list.
    target = int(input("Enter the Target : "))
    n = int(input("Enter the Rows : "))
    m = int(input("Enter the Columns : "))

    mat = []
    for i in range(n):
        rows = list(map(int, input("Enter the Elements : ").split()))
        mat.append(rows)
    result = search_matrix(mat, target)

    if result:
        print("Target Found")
    else:
        print("Target Not Found")


if __name__ == "__main__":
    main()