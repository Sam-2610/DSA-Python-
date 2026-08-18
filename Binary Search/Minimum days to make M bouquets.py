def possible(arr, day, m, k):
    cnt = 0    # consecutive bloomed-flower streak length
    nofb = 0   # number of bouquets makeable so far

    for i in range(len(arr)):
        if arr[i] <= day:
            cnt += 1  # flower has bloomed by this day, extend streak
        else:
            nofb += cnt // k  # streak broken: convert it into bouquets (integer division)
            cnt = 0            # reset streak

    nofb += cnt // k  # account for a streak that runs to the end of the array

    return nofb >= m  # can we make at least m bouquets?


def rose_garden(arr, m, k):
    val = m * k  # total flowers needed

    if val > len(arr):
        return -1  # not enough flowers to ever satisfy the requirement

    mini = float('inf')
    maxi = float('-inf')

    for i in range(len(arr)):
        mini = min(mini, arr[i])
        maxi = max(maxi, arr[i])

    low = mini   # earliest possible answer day
    high = maxi  # latest possible answer day (every flower has bloomed by then)

    while low <= high:
        mid = (low + high) // 2

        if possible(arr, mid, m, k):
            # day `mid` already works, try an even earlier day
            high = mid - 1
        else:
            # day `mid` doesn't work, need to wait longer
            low = mid + 1

    return low  # smallest day where m bouquets of k flowers each are possible


def main():
    arr = list(map(int, input("Enter the Elements : ").split()))
    m = int(input("Enter the number of bouquets (m): "))
    k = int(input("Enter flowers per bouquet (k): "))
    print(rose_garden(arr, m, k))


if __name__ == "__main__":
    main()