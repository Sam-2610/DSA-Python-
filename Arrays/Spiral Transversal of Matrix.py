def traverse_spiral():
    matt = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    arr = []

    n = len(matt)
    m = len(matt[0])
    left = 0
    right = m - 1
    top = 0
    bottom = n - 1

    while top <= bottom and left <= right:
        # Move Right
        for i in range(left, right + 1): # Fixed: added + 1
            arr.append(matt[top][i])
        top = top + 1
        
        # Move Down
        for i in range(top, bottom + 1): # Fixed: added + 1
            arr.append(matt[i][right])
        right = right - 1

        if top <= bottom:
            # Move Left
            for i in range(right, left - 1, -1): # Fixed: changed to left - 1
                arr.append(matt[bottom][i])
            bottom = bottom - 1
        
        if left <= right:
            # Move Up
            for i in range(bottom, top - 1, -1): # Fixed: changed to top - 1
                arr.append(matt[i][left])
            left = left + 1
    
    print(arr)

traverse_spiral()