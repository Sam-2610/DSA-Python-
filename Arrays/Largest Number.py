# WAP to print the Largest Number in Array.

def largest_number():
    arr = []
    n = int(input("Enter the Number of Values in Array : "))
    for i in range(n):
        x = int(input(f"Enter the element {i + 1} : "))
        arr.append(x)
    if arr:
        largest = arr[0]
        for j in range(1, n):
            if arr[j] > largest:
                largest = arr[j]
        print("The Largest Element in the Array is : ",largest)
    else:
        print("No elements in array")


largest_number()