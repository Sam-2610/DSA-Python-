def sqrt(n):
    low = 1
    high = n

    while low <= high:
        mid = (low + high) // 2
        val = mid * mid  # fixed: was mid + mid, should be mid squared

        if val <= n:
            # mid*mid fits within n, so mid could be the answer (or answer is bigger)
            low = mid + 1
        else:
            # mid*mid overshot n, answer must be smaller
            high = mid - 1

    return high  # high ends up being the floor of sqrt(n)


def main():
    n = int(input("Enter the Number : "))
    print(sqrt(n))


if __name__ == "__main__":
    main()