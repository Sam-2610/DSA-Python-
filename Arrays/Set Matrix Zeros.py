def set_matrix():
    # Sample 3x3 matrix to test
    matt = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    n = len(matt)        # number of rows
    m = len(matt[0])      # number of columns (BUG FIX: was hardcoded to 0)

    # col0 tracks whether the FIRST COLUMN itself needs to be zeroed.
    # We can't use matt[i][0] for this like we do for other columns,
    # because matt[i][0] is also being used as a marker for row i.
    col0 = 1

    # --- Step 1: Use first row and first column as "markers" ---
    # If matt[i][j] == 0, mark its row (matt[i][0]) and column (matt[0][j])
    for i in range(n):
        for j in range(m):
            if matt[i][j] == 0:
                matt[i][0] = 0          # mark row i
                if j != 0:
                    matt[0][j] = 0       # mark column j (using first row)
                else:
                    col0 = 0             # column 0 needs zeroing (tracked separately)

    # --- Step 2: Zero out cells based on markers ---
    # Skip column 0 here (range starts at 1) since it's handled separately via col0
    for i in range(n):
        for j in range(1, m):
            if matt[i][j] != 0:
                # If either this cell's row-marker or column-marker is 0, zero it
                if matt[0][j] == 0 or matt[i][0] == 0:
                    matt[i][j] = 0

    # --- Step 3: Handle the first row itself ---
    # matt[0][0] doubles as the marker for both row 0 and column 0.
    # If it's 0, that means row 0 originally had a zero -> zero out entire first row.
    if matt[0][0] == 0:
        for j in range(m):
            matt[0][j] = 0

    # --- Step 4: Handle the first column itself ---
    # If col0 flag was set to 0, zero out entire first column.
    if col0 == 0:
        for i in range(n):
            matt[i][0] = 0

    return matt