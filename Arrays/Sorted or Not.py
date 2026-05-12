# WAP to Check the Array is Sorted or Not.

def sorted_or_not():
    arr = []
    n = int(input("Enter the Number of Values in Array : "))
    for i in range(n):
        x = int(input(f"Enter the Element {i + 1} : "))
        arr.append(x)
    if arr:
        is_sorted = True
        for j in range(1, n):
            if arr[j] < arr[j - 1]:
                is_sorted = False
                break
        if is_sorted:
            print("Array is Sorted.")
        else:
            print("Array is Not Sorted.")
    else:
        print("Array is empty.")


sorted_or_not()