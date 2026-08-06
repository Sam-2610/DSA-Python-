def merge_sorted_array(arr1, arr2, ind1, ind2):
    if arr1[ind1] > arr2[ind2]:
        arr1[ind1], arr2[ind2] = arr2[ind2], arr1[ind1]


def merge(arr1, arr2):
    n = len(arr1)
    m = len(arr2)

    length = n + m
    gap = (length // 2) + (length % 2)

    while gap > 0:
        left = 0
        right = left + gap

        while right < length:

            # left in arr1, right in arr2
            if left < n and right >= n:
                merge_sorted_array(arr1, arr2, left, right - n)

            # both in arr2
            elif left >= n:
                if arr2[left - n] > arr2[right - n]:
                    arr2[left - n], arr2[right - n] = arr2[right - n], arr2[left - n]

            # both in arr1
            else:
                if arr1[left] > arr1[right]:
                    arr1[left], arr1[right] = arr1[right], arr1[left]

            left += 1
            right += 1

        if gap == 1:
            break

        gap = (gap // 2) + (gap % 2)

    print(arr1)
    print(arr2)


# Driver code
arr1 = list(map(int, input("Enter sorted array1: ").split()))
arr2 = list(map(int, input("Enter sorted array2: ").split()))

merge(arr1, arr2)