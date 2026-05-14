# WAP to perform Insertion Sort.

def insertion_sort():
    arr = []
    n = int(input("Enter the Number you want in array : "))
    for i in range(n):
        x = int(input(f"Enter the Element {i + 1} : "))
        arr.append(x)

    for j in range(1,n):
        k = j
        while k > 0 and arr[k - 1] > arr[k]:
            temp = arr[k - 1]
            arr[k - 1] = arr[k]
            arr[k] = temp
            k = k - 1
    if arr:
        print("Sorted Array : ",arr)
    else:
        print("No Elements in Array")

insertion_sort()