def union_array():
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

    n1 = len(l1)
    n2 = len(l2)

    i = 0
    j = 0
    l3 = []

    # Step 1: Traverse both arrays together
    while i < n1 and j < n2:
        if l1[i] <= l2[j]:
            if len(l3) == 0 or l3[-1] != l1[i]:   # avoid duplicates
                l3.append(l1[i])
            i += 1                                   # ✅ move i forward
        else:
            if len(l3) == 0 or l3[-1] != l2[j]:   # avoid duplicates
                l3.append(l2[j])
            j += 1                                   # ✅ move j forward

    # Step 2: Add remaining elements of l1
    while i < n1:
        if l3[-1] != l1[i]:
            l3.append(l1[i])
        i += 1

    # Step 3: Add remaining elements of l2
    while j < n2:
        if l3[-1] != l2[j]:
            l3.append(l2[j])
        j += 1

    print("Union : ", l3)

union_array()