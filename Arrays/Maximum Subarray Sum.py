def kadanes_algo():
    arr = []
    n = int(input("Enter the Number of Elements : "))
    for i in range(n):
        x = int(input(f"Enter the Element {i + 1} : "))
        arr.append(x)

    curr_sum = 0
    maxi = 0

    for i in range(n):
        curr_sum = curr_sum + arr[i]  # Rule 1 - keep adding

        if curr_sum > maxi:
            maxi = curr_sum           # Rule 2 - update max if better

        if curr_sum < 0:
            curr_sum = 0              # Rule 3 - reset if negative

    if maxi < 0:
        maxi = 0
        
    print("Maximum Subarray Sum : ", maxi)

kadanes_algo()