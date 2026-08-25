def can_we_place(arr, dist, cows):
    cnt_cows = 1     # first cow always placed at the first stall
    last = arr[0]     # position of the most recently placed cow

    for i in range(1, len(arr)):
        if arr[i] - last >= dist:
            # this stall is far enough from the last placed cow -> place a cow here
            cnt_cows += 1
            last = arr[i]

        if cnt_cows >= cows:
            # already managed to place all cows with at least `dist` gap -> success
            return True

    return False  # ran out of stalls before placing all cows


def aggressive_cows(arr, k):
    arr.sort()  # positions must be sorted for the greedy placement to work

    low = 1                    # smallest possible minimum distance
    high = arr[-1] - arr[0]    # largest possible minimum distance (first to last stall span)

    while low <= high:
        mid = (low + high) // 2  # candidate minimum distance

        if can_we_place(arr, mid, k):
            # this distance works, try an even larger distance
            low = mid + 1
        else:
            # this distance is too large, cows don't fit -> try smaller
            high = mid - 1

    return high  # largest distance that still allows placing all cows


def main():
    arr = list(map(int, input("Enter the Elements : ").split()))
    cows = int(input("Enter the Number of Cows : "))
    print(aggressive_cows(arr, cows))


if __name__ == "__main__":
    main()