def four_sum():
    # Read space-separated integers and sort them
    # Sorting is essential — it lets us use two pointers to find pairs efficiently
    # and makes skipping duplicates straightforward
    arr = list(map(int, input("Enter the Elements separated by Space").split()))
    n = len(arr)
    arr.sort()

    target = int(input("Enter the Target : "))
    ans = []

    # Fix the first element of the quadruple
    for i in range(n):
        # Skip duplicate values for i to avoid duplicate quadruples
        if i > 0 and arr[i] == arr[i - 1]:
            continue

        # Fix the second element of the quadruple
        for j in range(i + 1, n):
            # Skip duplicate values for j (only skip if j isn't right after i,
            # since consecutive equal values right after i are still valid starts)
            if j != i + 1 and arr[j] == arr[j - 1]:
                continue

            # Two pointers for the remaining two elements
            k = j + 1
            l = n - 1

            while k < l:
                sum = arr[i] + arr[j] + arr[k] + arr[l]

                if sum == target:
                    # Found a valid quadruple
                    temp = [arr[i], arr[j], arr[k], arr[l]]
                    ans.append(temp)

                    k = k + 1
                    l = l - 1

                    # Skip duplicates for k
                    while k < l and arr[k] == arr[k - 1]:
                        k = k + 1
                    # Skip duplicates for l
                    while k < l and arr[l] == arr[l + 1]:
                        l = l - 1

                elif sum < target:
                    # Sum too small, move k right to increase sum
                    k = k + 1
                else:
                    # Sum too large, move l left to decrease sum
                    l = l - 1

    print(ans)


four_sum()