def missing_number():
    arr = []
    n = int(input("Enter the Number of Elements : "))
    for i in range(n):
        x = int(input(f"Enter the Element {i + 1} : "))
        arr.append(x)

    sum1 = n*(n+1)/2
    sum2 = 0

    for i in range(n - 1):
        sum2 = sum2 + arr[i]

    print("Missing Number : ",sum1 - sum2)

missing_number()