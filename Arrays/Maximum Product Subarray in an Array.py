def max_prod():
    arr = list(map(int, input("Enter the Numbers sepated by space : ").split()))

    # Two running products: one scanning left-to-right (pre), one right-to-left (suff)
    # Why both directions? A negative number can flip a small product into a large one
    # later on — scanning from both ends ensures we never miss that flip
    pre = 1
    suff = 1
    ans = float('-inf')
    n = len(arr)

    for i in range(n):
        # If either running product hit 0, "restart" it from 1 —
        # a 0 anywhere breaks the product chain, so we can't carry it forward
        if pre == 0:
            pre = 1
        if suff == 0:
            suff = 1

        # FIX: this must be MULTIPLICATION, not addition — we're tracking a running
        # product of the subarray, not a sum. The original code had:
        #     pre = pre + arr[i]
        # which computes a prefix SUM instead of a prefix PRODUCT, giving wrong results.
        pre = pre * arr[i]
        suff = suff * arr[n - i - 1]

        # Track the best product seen so far from either direction
        ans = max(ans, max(pre, suff))

    print(ans)

max_prod()