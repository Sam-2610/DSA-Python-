def nCr():
    n = int(input("Enter the Column : "))
    r = int(input("Enter the Row : "))
    res = 1
    for i in range(r):
        res = res * (n - i) // (i + 1)
    print(res)

nCr()