def subarray_sum():
    arr = []
    n = int(input("Enter the Number of Elements: "))
    for i in range(n):
        x = int(input(f"Enter Element {i + 1}: "))
        arr.append(x)
    
    k = int(input("Enter the Target Sum (k): "))
    
    # Fixed: Use a dictionary for the map. 
    # Initialize it with 0: 1 to handle subarrays that start from index 0.
    prefix_map = {0: 1} 
    presum = 0
    cnt = 0
    
    for i in range(n):
        presum += arr[i]
        remove = presum - k
        
        # Fixed: Safely get the value from the dictionary. 
        # If 'remove' doesn't exist, it returns 0.
        cnt += prefix_map.get(remove, 0)
        
        # Fixed: Safely update the frequency of the current prefix sum.
        prefix_map[presum] = prefix_map.get(presum, 0) + 1
    
    print(cnt)

subarray_sum()