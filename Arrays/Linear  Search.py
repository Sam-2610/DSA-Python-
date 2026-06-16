def linear_search():
    l = []
    n = int(input("Enter the Number of Elements : "))
    for i in range(n):
        x = int(input(f"Enter the Element {i + 1} : "))
        l.append(x) # type: ignore

    target = int(input("Enter the number to search for: "))
    found = False

    for j in range(n):
        if l[j] == target:
            print(j)
            found = True
            break

    if not found:
        print("-1")

linear_search()