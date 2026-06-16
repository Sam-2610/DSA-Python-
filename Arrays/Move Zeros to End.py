def move_zeros():
    l = []
    n = int(input("Enter the Number of Elements: "))
    for i in range(n):
        x = int(input(f"Enter the Element {i + 1}: "))
        l.append(x) # type: ignore

    # Two pointer approach
    j = 0  # points to the position where next non-zero should go

    for k in range(n):
        if l[k] != 0:
            l[j], l[k] = l[k], l[j]  # swap non-zero to front
            j += 1

    print(l) # type: ignore

move_zeros()