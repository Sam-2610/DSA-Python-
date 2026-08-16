def single_element(arr, n):
    if n == 1:
        return arr[0]  # only one element, must be the answer

    if arr[0] != arr[1]:
        return arr[0]  # single element sits at the very start

    if arr[n - 1] != arr[n - 2]:
        return arr[n - 1]  # single element sits at the very end

    low = 1
    high = n - 2

    while low <= high:  # fixed: was `low < high`, must include the case low == high
        mid = (low + high) // 2

        # mid itself doesn't match either neighbor -> mid IS the single element
        if arr[mid] != arr[mid + 1] and arr[mid] != arr[mid - 1]:
            return arr[mid]

        # figure out whether we're still in the "normal" (paired) zone before
        # the single element, or already past it, based on mid's parity
        if (mid % 2 == 1 and arr[mid] == arr[mid - 1]) or (mid % 2 == 0 and arr[mid] == arr[mid + 1]):
            # pairing looks normal up to here -> single element is further right
            low = mid + 1
        else:
            # pairing is disrupted -> single element is at or before mid
            high = mid - 1

    return -1  # shouldn't be reached if input is valid (guaranteed one single element)


def main():
    arr = list(map(int, input("Enter the Elements : ").split()))
    n = len(arr)
    print(single_element(arr, n))


if __name__ == "__main__":
    main()