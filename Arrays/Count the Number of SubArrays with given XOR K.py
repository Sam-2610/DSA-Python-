def subarray_with_given_xor_k():
    # Read the array
    arr = list(map(int, input("Enter the Element with Separated Spaces").split()))

    xr = 0  # running prefix XOR — XOR of all elements from index 0 to current i
    K = int(input("Enter the Target : "))

    # hash_dict maps: prefix_XOR_value -> how many times that prefix XOR has occurred so far
    # Start with {0: 1} because an "empty prefix" (before the array starts) has XOR = 0,
    # which correctly accounts for subarrays starting from index 0 that XOR to exactly K
    hash_dict : dict[int,int] = {0: 1}
    cnt = 0  # total count of subarrays whose XOR equals K

    for i in range(len(arr)):
        # Update running XOR to include the current element
        xr = xr ^ arr[i]

        # Key idea: if prefix_xor[j] ^ prefix_xor[i] = K for some j < i,
        # then the subarray between j+1 and i has XOR = K.
        # Rearranging: prefix_xor[j] = prefix_xor[i] ^ K
        # So we look up how many earlier prefixes equal (xr ^ K)
        x = xr ^ K
        if x in hash_dict:
            cnt = cnt + hash_dict[x]

        # Record the current prefix XOR in the hashmap for future indices to reference
        if xr in hash_dict:
            hash_dict[xr] += 1
        else:
            hash_dict[xr] = 1

    print(cnt)

subarray_with_given_xor_k()