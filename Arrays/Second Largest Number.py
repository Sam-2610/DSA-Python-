def get_input():
    """Reads array elements from the user and returns (n, arr)."""
    arr = []
    n = int(input("Enter the Number of Elements : "))
    for i in range(n):
        x = int(input(f"Enter the Element {i + 1} : "))
        arr.append(x)
    return n, arr


def second_smallest(n, arr):
    """Returns the second smallest distinct element, or -1 if not possible."""
    if n < 2:
        return -1

    small = float('inf')          # FIX: was float() -> 0.0, now true +infinity
    second_small = float('inf')   # FIX: same issue

    for i in range(n):
        if arr[i] < small:
            # New smallest found -> old smallest becomes second smallest
            second_small = small
            small = arr[i]
        elif arr[i] < second_small and arr[i] != small:
            # New second-smallest found (must differ from current smallest)
            second_small = arr[i]
        # NOTE: no 'else: return' here anymore — FIX: that caused early exit
        # We just let the loop continue to the next element.

    # After scanning everything, check if a valid second smallest was found
    if second_small == float('inf'):
        return -1
    return second_small


def second_largest(n, arr):
    """Returns the second largest distinct element, or -1 if not possible."""
    if n < 2:
        return -1

    large = float('-inf')
    second_large = float('-inf')

    for i in range(n):
        if arr[i] > large:
            # New largest found -> old largest becomes second largest
            second_large = large
            large = arr[i]
        elif arr[i] > second_large and arr[i] != large:
            # New second-largest found (must differ from current largest)
            second_large = arr[i]
        # FIX: removed the 'else: return second_large' that caused early exit

    if second_large == float('-inf'):
        return -1
    return second_large


if __name__ == "__main__":
    n, arr = get_input()
    print("Second Smallest:", second_smallest(n, arr))
    print("Second Largest:", second_largest(n, arr))