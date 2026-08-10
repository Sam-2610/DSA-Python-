def find_repeating_and_missing():
    arr = list(map(int, input("Enter the Element with Space : ").split()))
    n = len(arr)
    SN = n * (n + 1) // 2
    SN2 = n * (n + 1) * (2 * n + 1) // 6
    S = 0
    S2 = 0

    for i in range(n):
        S += arr[i]
        S2 += arr[i] * arr[i]

    val1 = S - SN            # repeating - missing
    val2 = (S2 - SN2) // val1  # repeating + missing

    repeating = (val1 + val2) // 2
    missing = repeating - val1

    return repeating, missing