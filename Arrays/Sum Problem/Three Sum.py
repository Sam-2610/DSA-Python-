def three_sum():
    # Take input from user and convert to list of integers
    arr = list(map(int, input("Enter the Number Separated by Spaces ").split()))
    
    # Get length of array
    n = len(arr)
    
    # Sort the array in ascending order
    # Sorting is necessary for two pointer approach to work
    arr.sort()

    # List to store all unique triplets
    ans = []

    # Iterate through each element as the first element of triplet
    for i in range(n):
        
        # Skip duplicate elements for first pointer
        # to avoid duplicate triplets in answer
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        
        # Second pointer starts from element after i
        j = i + 1
        
        # Third pointer starts from last element
        k = n - 1

        # Two pointer approach
        # Move j and k towards each other
        while j < k:
            
            # Calculate sum of three elements
            sum = arr[i] + arr[j] + arr[k]
            
            if sum < 0:
                # Sum is too small
                # Move left pointer right to increase sum
                j = j + 1
                
            elif sum > 0:
                # Sum is too large
                # Move right pointer left to decrease sum
                k = k - 1
                
            else:
                # Sum is exactly zero
                # Found a valid triplet
                temp = [arr[i], arr[j], arr[k]]
                ans.append(temp)
                
                # Move both pointers inward
                # to look for more triplets
                j = j + 1
                k = k - 1

                # Skip duplicate elements for second pointer
                # to avoid duplicate triplets
                while j < k and arr[j] == arr[j - 1]:
                    j = j + 1
                    
                # Skip duplicate elements for third pointer
                # to avoid duplicate triplets
                while j < k and arr[k] == arr[k + 1]:
                    k = k - 1

    # Print all unique triplets
    print(ans)

# Call the function
three_sum()