def merge_overlapping_intervals():
    # Take flat input like "1 3 2 6 8 10" and read it as pairs: (1,3), (2,6), (8,10)
    elements = list(map(int, input("Enter the Element Separated by Space : ").split()))

    # FIX: guard against odd-length input — without this check, an odd number of
    # elements causes elements[i+1] to go out of bounds on the last pair (IndexError)
    if len(elements) % 2 != 0:
        print("Error: please enter an even number of elements (each interval needs a start and end).")
        return

    # Group flat list into (start, end) tuples, two at a time
    arr = [(elements[i], elements[i+1]) for i in range(0, len(elements), 2)]
    n = len(arr)

    # Sort intervals by start time (and by end time as a tiebreaker, since these are tuples)
    # This is essential — merging only works correctly on sorted intervals
    arr.sort()

    ans = []
    for i in range(n):
        # Start a new interval in the result if:
        # - it's the very first interval, OR
        # - the current interval's start is AFTER the last merged interval's end (no overlap)
        if len(ans) == 0 or arr[i][0] > ans[-1][1]:
            ans.append(list(arr[i]))  # stored as a list (not tuple) so it can be mutated below
        else:
            # Overlapping (or touching) interval — merge by extending the end
            # of the last interval to cover whichever end is further out
            ans[-1][1] = max(ans[-1][1], arr[i][1])
        
    print(ans)

merge_overlapping_intervals()