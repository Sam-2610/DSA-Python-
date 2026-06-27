def leaders_in_an_array():
    arr = []
    n = int(input("Enter the Number of Elements : "))
    for i in range(n):
        x = int(input(f"Enter the Element {i + 1} : "))
        arr.append(x)

    arr2 = []
    maxi = float('-inf')              # ✅ handles negative numbers too

    for i in range(n - 1, -1, -1):   # ✅ step -1 to go right to left
        if arr[i] >= maxi:            # ✅ current element is a leader
            arr2.append(arr[i])
            maxi = arr[i]             # ✅ update max inside if, not else

    arr2.reverse()                    # ✅ reverse to get original order
    print("Leaders : ", arr2)

leaders_in_an_array()