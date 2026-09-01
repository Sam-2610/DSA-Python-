def number_of_gas_stations_required(dist, arr):
    """
    Helper: given an existing sorted array of gas station positions,
    return how many NEW stations must be inserted so that every gap
    between consecutive stations is at most `dist`.

    For a gap of length L = arr[i] - arr[i-1]:
      - We need floor(L / dist) new stations if L is not an exact
        multiple of dist.
      - We need floor(L / dist) - 1 if L IS an exact multiple of dist
        (splitting evenly needs one fewer station than the floor would
        suggest, since the boundary points already line up exactly).
      This is equivalent to the standard formula ceil(L / dist) - 1.
    """
    count = 0
    n = len(arr)

    for i in range(1, n):
        number_in_between = int((arr[i] - arr[i - 1]) / dist)

        if (arr[i] - arr[i - 1]) == dist * number_in_between:
            number_in_between -= 1

        count += number_in_between
    return count


def min_max_dist(arr, k):
    """
    Given sorted gas station positions `arr` and a budget of `k` new
    stations to add, find the minimum possible value for the largest
    gap between any two adjacent stations after optimally placing
    those k new stations.

    Binary search over the real-valued answer (the max-gap distance):
      - low starts at 0, high starts at the largest existing gap
        (that's the worst case, using 0 new stations).
      - For a candidate `mid` distance, count how many stations WOULD
        be required to make every gap <= mid.
      - If that required count is more than we're allowed (k), `mid`
        is too small/strict -> search larger distances.
      - Otherwise `mid` is achievable (or better than needed) ->
        search smaller distances, trying to shrink the answer.
      - Stop once the search interval is smaller than `diff` (a
        precision threshold), since we're searching over real numbers.

    NOTE: originally this had a stray `self` parameter (leftover from
    being a class method) and was never actually called from main() --
    both are fixed here.
    """
    low = 0
    high = max(arr[i + 1] - arr[i] for i in range(len(arr) - 1))
    diff = 1e-6  # FIX: was "1e - 6" (with a space), which is a SyntaxError

    while high - low > diff:
        mid = (low + high) / 2.0
        count = number_of_gas_stations_required(mid, arr)

        if count > k:
            low = mid
        else:
            high = mid
    return high


def main():
    arr = list(map(int, input("Enter the Elements : ").split()))
    k = int(input("Enter the Number of Gas Stations to add : "))

    # FIX: main() previously called number_of_gas_stations_required(arr, dist)
    # directly, with the arguments swapped relative to the function's
    # signature (dist, arr) -- that crashed with len() on an int. It also
    # never called min_max_dist at all, even though that's the function
    # that actually answers "minimize the max distance given k stations".
    result = min_max_dist(arr, k)
    print("Minimized Maximum Distance : ", result)


if __name__ == "__main__":
    main()