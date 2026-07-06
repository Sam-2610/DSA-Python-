def majority_element():
    arr = []
    n = int(input("Enter the Number of Elements : "))
    for i in range(n):
        x = int(input(f"Enter the Element {i + 1} : "))
        arr.append(x)

    # Step 1 - Boyer Moore Voting Algorithm
    count = 0
    element = 0

    for i in range(n):
        if count == 0:
            count += 1
            element = arr[i]
        elif arr[i] == element:
            count += 1
        else:
            count -= 1

    # Step 2 - Verify the candidate
    count1 = 0
    for i in range(n):
        if arr[i] == element:
            count1 += 1

    if count1 > (n // 2):   # ✅ outside loop
        print("Element : ", element)
    else:
        print("-1")

majority_element()