def maximum_consecutives():
    arr = []
    n = int(input("Enter the Number of Elements : "))
    for i in range(n):
        x = int(input(f"Enter the Element {i + 1} : "))
        arr.append(x) # type: ignore

    maxi = 0
    cnt = 0

    for i in range(n):
        if arr[i] == 1:
            cnt = cnt + 1
            maxi = max(maxi,cnt)
        else:
            cnt = 0
    print(maxi)

maximum_consecutives()