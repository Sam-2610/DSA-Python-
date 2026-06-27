def matrix_rotate():
    # Providing a sample 3x3 matrix to test
    matt = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    n = len(matt)

    # Step 1: Transpose the matrix (swap rows and columns)
    for i in range(n):
        for j in range(i + 1, n):
            # Fixed: Use Python's tuple unpacking to swap the values
            matt[i][j], matt[j][i] = matt[j][i], matt[i][j]
    
    # Step 2: Reverse each individual row
    for i in range(n):
        # Fixed: Reverse the specific row (matt[i]), not the whole matrix
        matt[i].reverse()
        
    # Print the result row by row for readability
    for row in matt:
        print(row)

matrix_rotate()