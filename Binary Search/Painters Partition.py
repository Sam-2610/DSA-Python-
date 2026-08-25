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

    return students


def find_pages(arr, n, m):
    if m > n:
        return -1  # more students than books -> can't allocate at least one book each

    low = max(arr)   # minimum possible max-pages: at least the largest single book
    high = sum(arr)  # maximum possible max-pages: one student takes everything

    while low <= high:
        mid = (low + high) // 2
        students = count_students(arr, mid)  # students needed if limit is `mid`

        if students > m:
            low = mid + 1
        else:
            high = mid - 1

    return low  # smallest max-pages limit that still needs <= m students


def find_largest_mini_distance(a, k):
    # NOTE: this just delegates straight to find_pages -> still solving
    # "Book Allocation" (minimize the maximum), NOT "largest minimum distance"
    return find_pages(a, len(a), k)


def main():
    a = list(map(int, input("Enter the Elements : ").split()))
    k = int(input("Enter the number of Students : "))
    print(find_largest_mini_distance(a, k))


if __name__ == "__main__":
    main()