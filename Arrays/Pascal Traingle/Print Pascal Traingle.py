def generate_row(row):
    ans = 1
    ansrow = [1]

    for i in range(1, row):
        ans = ans * (row - i) // i
        ansrow.append(ans)
    return ansrow

def pascal_triangle():
    N = int(input("Enter the Number : "))
    triangle = []
    for row in range(1, N + 1):
        triangle.append(generate_row(row))
    for ansrow in triangle:
        print(ansrow)

pascal_triangle()