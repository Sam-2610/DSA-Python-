def single_element():
    arr = []
    n = int(input("Enter the Number of Elements : "))
    for i in range(n):
        x = int(input(f"Enter the Element {i + 1} : "))
        arr.append(x)

    xor = 0
    for i in range(n):
        xor = xor ^ arr[i]
    print("Number : ",xor)

single_element()