def find_days(weights, cap):
    days = 1   # at least one day is needed to ship anything
    load = 0    # weight loaded on the ship for the current day

    for i in range(len(weights)):
        if weights[i] + load > cap:
            # adding this package would exceed capacity -> start a new day
            days = days + 1
            load = weights[i]
        else:
            # package fits within today's remaining capacity
            load = load + weights[i]

    return days  # total days needed to ship everything at this capacity


def least_weights(weights, d):
    low = max(weights)   # minimum possible capacity: must fit the heaviest single package
    high = sum(weights)  # maximum possible capacity: ship everything in one day

    while low <= high:
        mid = (low + high) // 2
        number_of_days = find_days(weights, mid)  # days needed if capacity is `mid`

        if number_of_days <= d:
            # this capacity works within the day limit -> try a smaller capacity
            high = mid - 1
        else:
            # this capacity isn't enough, need more days than allowed -> increase capacity
            low = mid + 1

    return low  # smallest capacity that ships everything within d days

def main():
    weights = list(map(int, input("Enter the Elements : ").split()))
    d = int(input("Enter the Number of Days : "))
    print(least_weights(weights, d))

if __name__ == "__main__":
    main()