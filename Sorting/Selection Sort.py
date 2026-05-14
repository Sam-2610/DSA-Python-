# WAP to perform Selection Sort on Arrays.

def selection_sort():
    arr = []
    n = int(input("Enter the Numbers you want in your Array : "))
    for i in range(n):
        x = int(input(f"Enter the Element {i + 1} : "))
        arr.append(x)

    for j in range(n - 1):
        mini = j
        for k in range(j + 1,n):
            if arr[k] < arr[mini]:
                mini = k

        temp = arr[mini]
        arr[mini] = arr[j]
        arr[j] = temp

    if arr:
        print(f"Sorted Array : {arr}")
    else:
        print("No Elements in Array")

selection_sort()