def median(arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)

    if n1 > n2:
        return median(arr2, arr1)

    low = 0
    high = n1
    left = (n1 + n2 + 1) // 2
    n = n1 + n2

    while low <= high:
        mid1 = (low + high) >> 1
        mid2 = left - mid1

        l1 = float('-inf')
        l2 = float('-inf')
        r1 = float('-inf')
        r2 = float('inf')

        if mid1 < n1:
            r1 = arr1[mid1]

        if mid2 < n2:
            r2 = arr2[mid2]

        if mid1 - 1 >= 0:
            l1 = arr1[mid1 - 1]

        if mid2 - 1 >= 0:
            l2 = arr2[mid2 - 1]

        if l1 <= r2 and l2 <= r1:
            if n % 2 == 1:
                return max(l1, l2)
            else:
                return (max(l1,l2) + min(r1,r2)) / 2.0
        elif l1 > r2:
            high = mid1 - 1
        else:
            low = mid1 + 1
    return 0

def main():
    arr1 = list(map(int, input("Enter the Element : ").split()))
    arr2 = list(map(int, input("Enter the Element : ").split()))
    print("Median : ", median(arr1, arr2))

if __name__ == "__main__":
    main()