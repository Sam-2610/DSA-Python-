def intersection_array():
    l1 = []
    n = int(input("Enter the Number of Elements in Array 1 : "))
    for i in range(n):
        x = int(input(f"Enter the Element {i + 1} : "))
        l1.append(x)

    l2 = []
    m = int(input("Enter the Number of Elements in Array 2 : "))
    for i in range(m):
        x = int(input(f"Enter the Element {i + 1} : "))
        l2.append(x)

    i = 0                               
    j = 0                               

    l3 = []

    while i < n and j < m:
        if l1[i] < l2[j]:
            i += 1
        elif l2[j] < l1[i]:
            j += 1
        else:                           # l1[i] == l2[j]
            l3.append(l1[i])
            i += 1
            j += 1

    print("Intersection : ", l3)

intersection_array()