def search():
    arr = list(map(int, input("Enter the Elements with Space : ").split()))
    target = int(input("Enter the target Element : "))
    n = len(arr)
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2  # middle index of current search range

        if arr[mid] == target:
            print(mid)   # found target, print its index
            return       # stop the function immediately (fixes infinite loop)
        elif target > arr[mid]:
            low = mid + 1   # target is in the right half, discard left half
        else:
            high = mid - 1  # target is in the left half, discard right half

    print("-1")  # loop ended without finding target -> not found

search()