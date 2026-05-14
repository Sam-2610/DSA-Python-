# WAP to perform Bubble Sort on an Array.

def bubble_sort():
    arr = []
    n = int(input("Enter the Numbers you want in your Array : "))
    for i in range(n):
        x = int(input(f"Enter the Element {i + 1}: "))
        arr.append(x)

    for j in range(n - 1):
        for k in range(n-1-j):
            if arr[k] > arr[k + 1]:
                temp = arr[k + 1]
                arr[k + 1] = arr[k]
                arr[k] = temp

    if arr:
        print("Sorted Array : ",arr)
    else:
        print("No Elements in Array")

bubble_sort()