from math import ceil

def sumd(arr, div):
    total = 0

    for i in range(len(arr)):
        total = total + ceil(arr[i] / div)  # each element contributes ceil(value/div) to the sum

    return total  # total sum when every element is divided by `div` and rounded up


def smallest_div(arr, limit):
    if len(arr) > limit:
        return -1
        # if divisor were infinitely large, sumd would approach len(arr)
        # (each ceil(x/div) -> 1), so if even that minimum exceeds limit, it's impossible

    low = 1            # smallest possible divisor
    high = max(arr)     # largest useful divisor: dividing by more than the max element
                         # still gives ceil(x/div)=1 for every element, same as high itself

    while low <= high:
        mid = (low + high) // 2

        if sumd(arr, mid) <= limit:
            # this divisor keeps the sum within limit -> try a smaller divisor
            high = mid - 1
        else:
            # sum still too large -> need a bigger divisor
            low = mid + 1

    return low  # smallest divisor that keeps the sum within limit


def main():
    arr = list(map(int, input("Enter the Input : ").split()))
    div = int(input("Enter the Threshold : "))
    print(smallest_div(arr, div))


if __name__ == "__main__":
    main()