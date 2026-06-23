def subarray_with_maximum_subarray():
    arr = []
    n = int(input("Enter the Number of Elements : "))
    for i in range(n):
        x = int(input(f"Enter the Element {i + 1} : "))
        arr.append(x)

    curr_sum = 0
    maxi = float('-inf')   # ✅ handles all negative arrays too
    ans_st = -1
    ans_end = -1
    start = 0

    for i in range(n):
        if curr_sum == 0:
            start = i              # ✅ mark potential start

        curr_sum += arr[i]         # ✅ always add, outside the if block

        if curr_sum > maxi:
            maxi = curr_sum
            ans_st = start         # ✅ save start
            ans_end = i            # ✅ save end

        if curr_sum < 0:
            curr_sum = 0           # reset → next iteration start will update

    print("Maximum Sum : ", maxi)
    print("Subarray : ", arr[ans_st : ans_end + 1])

subarray_with_maximum_subarray()