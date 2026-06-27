def rearrangeArray():
    arr1 = []
    n = int(input("Enter the Number of Elements : "))
    for i in range(n):
        x = int(input(f"Enter the Element {i + 1} : "))
        arr1.append(x)

    arr2 = [0] * n        # ✅ pre-fill with n zeros so index assignment works

    posIndex = 0          # positives go to even indices 0, 2, 4...
    negIndex = 1          # negatives go to odd  indices 1, 3, 5...

    for i in range(n):
        if arr1[i] < 0:
            arr2[negIndex] = arr1[i]    # place negative
            negIndex += 2               # jump to next odd index
        else:
            arr2[posIndex] = arr1[i]    # place positive
            posIndex += 2               # jump to next even index

    print("Rearranged Array : ", arr2)

rearrangeArray()    