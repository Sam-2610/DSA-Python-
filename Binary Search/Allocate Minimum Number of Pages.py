def count_students(arr, pages):
    students = 1       # at least one student is needed to hold any books
    pages_student = 0   # pages assigned to the current student so far

    for i in range(len(arr)):
        if pages_student + arr[i] <= pages:
            # current student can take this book without exceeding the limit
            pages_student += arr[i]
        else:
            # current student is full; assign a new student starting with this book
            students += 1
            pages_student = arr[i]

    return students  # fixed: moved outside the loop, so it counts all books


def find_pages(arr, n, m):
    if m > n:
        return -1  # more students than books -> can't allocate at least one book each

    low = max(arr)   # minimum possible max-pages: at least the largest single book
    high = sum(arr)  # maximum possible max-pages: one student takes everything

    while low <= high:
        mid = (low + high) // 2
        students = count_students(arr, mid)  # students needed if limit is `mid`

        if students > m:
            # too many students needed, limit is too tight -> raise it
            low = mid + 1
        else:
            # fits within m students (or fewer) -> try to shrink the limit further
            high = mid - 1

    return low  # smallest max-pages limit that still needs <= m students


def main():
    arr = list(map(int, input("Enter the Elements : ").split()))
    students = int(input("Enter the number of Students : "))
    print(find_pages(arr, len(arr), students))


if __name__ == "__main__":
    main()