# WAP to Count the Number of Zeros in an Array using Hashing.

def count_zeros():
    arr = []
    n = int(input("Enter the Number: "))
    for i in range(n):
        x = int(input(f"Enter the Element {i + 1}: "))
        arr.append(x)
    
    # Using a dictionary (hash map) to count frequencies
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    
    # Get the count of zeros
    count = freq.get(0, 0)
    if count > 0:
        print(f"The Count of Zeros is: {count}")
    else:
        print("No Zeros")

count_zeros()
        
    