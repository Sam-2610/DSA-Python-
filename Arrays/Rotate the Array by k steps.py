def rotatebyk_steps():
    l = []
    n = int(input("Enter the Number of Elements : "))
    for i in range(n):
        x = int(input(f"Enter the Element {i + 1} : "))
        l.append(x) # type: ignore

    d = int(input("Enter the number of steps (k) : "))
    d = d % n  # handle if k > n

    # Step 1: Save first d elements
    temp = l[:d] # type: ignore

    # Step 2: Shift remaining elements to the left
    for i in range(d, n):
        l[i - d] = l[i]

    # Step 3: Place saved elements at the end
    for i in range(n - d, n):
        l[i] = temp[i - (n - d)]

    print(l) # type: ignore

rotatebyk_steps()