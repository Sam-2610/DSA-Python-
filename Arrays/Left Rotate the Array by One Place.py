def roatate_Array():
    l = []
    n = int(input("Enter the Number of Elements : "))
    for i in range(n):
        x = int(input(f"Enter the Element {i + 1} : "))
        l.append(x) # type: ignore

    if n > 0:
        temp = l[0] # type: ignore
        for j in range(1, n):
            l[j - 1] = l[j]

        l[n - 1] = temp

    print(l) # type: ignore

roatate_Array()