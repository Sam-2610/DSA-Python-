from math import ceil

def find_max(arr):
    maxi = float('-inf')

    for i in range(len(arr)):
        maxi = max(maxi, arr[i])

    return maxi  # largest pile size -> upper bound for possible eating rate


def total_hours(arr, h):
    # h here represents the eating RATE (bananas/hour), despite the name
    totalh = 0

    for i in range(len(arr)):
        totalh += ceil(arr[i] / h)  # hours needed to finish pile i at rate h

    return totalh  # total hours needed across all piles at this rate


def minimum_rate(arr, v):
    # v = maximum hours allowed to finish all piles
    low = 1                 # slowest possible rate
    high = find_max(arr)    # fastest useful rate (no need to go beyond largest pile)

    while low <= high:
        mid = (low + high) // 2       # candidate eating rate
        totalh = total_hours(arr, mid)  # hours needed at this rate

        if totalh <= v:
            # rate is fast enough (or faster than needed) -> try a slower rate
            high = mid - 1
        else:
            # rate is too slow, need to eat faster
            low = mid + 1

    return low  # smallest rate that still finishes within v hours


def main():
    arr = list(map(int, input("Enter the Element : ").split()))
    h = int(input("Enter the Hours : "))
    print(minimum_rate(arr, h))


if __name__ == "__main__":
    main()