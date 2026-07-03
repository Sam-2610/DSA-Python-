def n_rows():
    n = int(input("Enter the Number of Row : "))
    ans = 1
    print(ans, end=' ')
    for i in range(1, n + 1):
        ans = ans * (n - i + 1) // i
        print(ans, end=' ')

n_rows()