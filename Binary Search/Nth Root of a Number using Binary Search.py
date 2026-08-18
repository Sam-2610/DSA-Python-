def func(mid, n, m):
    ans = 1
    for i in range(1, n + 1):  # fixed: run n times, not n-1
        ans = ans * mid
        if ans > m:
            return 2  # mid^n overshot m -> mid is too large
        if ans == m:
            return 1  # mid^n exactly matches m -> found the answer
    return 0  # mid^n never reached or exceeded m -> mid is too small


def nthroot(n, m):
    low = 1
    high = m

    while low <= high:
        mid = (low + high) // 2
        midn = func(mid, n, m)

        if midn == 1:
            return mid  # exact nth root found
        elif midn == 0:
            low = mid + 1  # mid too small, search right half
        else:
            high = mid - 1  # mid too large, search left half

    return -1  # no integer nth root exists


def main():
    n = int(input("Enter n (the root, e.g. 2 for square root): "))
    m = int(input("Enter m (the number to find the root of): "))
    print(nthroot(n, m))  # fixed: removed extra 'mid' argument


if __name__ == "__main__":
    main()