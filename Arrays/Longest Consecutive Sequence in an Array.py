def longest_consecutive_sequence():
    arr = []
    n = int(input("Enter the Number of Elements in the Array: "))
    
    if n == 0:
        print(0)
        return
        
    for i in range(n):
        x = int(input(f"Enter Element {i + 1}: "))
        arr.append(x)

    # Convert the array to a set for incredibly fast O(1) lookups
    num_set = set(arr)
    longest = 0

    for num in num_set:
        # Step 1: Check if 'num' is the START of a sequence.
        # It is only the start if the number right before it doesn't exist.
        if (num - 1) not in num_set:
            current_num = num
            current_streak = 1
            
            # Step 2: Now that we found a start, keep counting upwards
            # to see how long the consecutive streak goes.
            while (current_num + 1) in num_set:
                current_num += 1
                current_streak += 1
                
            # Step 3: Update the longest streak found so far
            longest = max(longest, current_streak)

    print(f"The longest consecutive sequence is: {longest}")

longest_consecutive_sequence()