# Write a Program to reverse the Array by swapping the Numbers.

def func8(i : int, arr : list, n : int) -> None:
    # Base condition: stop when we reach the middle
    if i >= n // 2:
        return
    
    # Swap elements (Python way)
    arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]
    
    # Recursive call
    func8(i + 1, arr, n)


# Main program
n = int(input())  # size of array

# Input array elements
arr = list(map(int, input().split()))

# Call function
func8(0, arr, n)

# Print reversed array
for num in arr:
    print(num, end=" ")