def sorting():
    l = []
    n = int(input("How many elements? : "))
    
    for i in range(n):
        element = int(input(f"Enter element {i + 1} : "))
        l.append(element)
    
    # Bubble Sort
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]  # swap
    
    print("Sorted List :", l)

sorting()