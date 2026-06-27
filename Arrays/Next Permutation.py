def next_permutation():
    arr = []
    n = int(input("Enter the Number of Elements: "))
    for i in range(n):
        x = int(input(f"Enter Element {i + 1}: "))
        arr.append(x)

    ind = -1

    # Step 1: Find the break point
    for i in range(n - 2, -1, -1):
        if arr[i] < arr[i + 1]:
            ind = i
            break
    
    # Step 2: If the array is entirely in descending order, 
    # reverse it to the lowest permutation and exit.
    if ind == -1:
        arr.reverse()
        print(arr)
        return  # Fixed: Exit the function here so the rest doesn't run

    # Step 3: Find the next largest element to swap with arr[ind]
    for i in range(n - 1, ind, -1): # Fixed: Only need to check down to ind
        if arr[i] > arr[ind]:
            arr[i], arr[ind] = arr[ind], arr[i]
            break
    
    # Step 4: Reverse only the suffix starting right after 'ind'
    arr[ind + 1:] = reversed(arr[ind + 1:]) # Fixed: Suffix reversal instead of full reversal
    
    print(arr)

next_permutation()