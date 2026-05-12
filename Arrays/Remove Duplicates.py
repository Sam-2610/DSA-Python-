# WAP to Remove the Duplicates.

def remove_duplicates():
    arr = []
    n = int(input("Enter the Number of Values in Array : "))
    for i in range(n):
        x = int(input(f"Enter the Element {i + 1} : "))
        arr.append(x)
        
    s = set(arr)
    print(list(s))
    
    """ if n == 0:
        print("Array is empty.")
        return
    
    # Sort the array first
    arr.sort()
    
    # Remove duplicates using two-pointer approach
    k = 0
    for j in range(1, n):
        if arr[k] != arr[j]:
            arr[k + 1] = arr[j]
            k = k + 1
    
    # Print the unique elements
    unique_count = k + 1
    print("Array after removing duplicates:")
    for i in range(unique_count):
        print(arr[i], end=" ")
    print()
    print(f"Count of unique elements: {unique_count}")
 """

remove_duplicates()
        