# Binary Search — Practice Set

Brief description and time complexity for each file.

## Core Binary Search

| File | Description | Time Complexity |
|---|---|---|
| `Iterative Code.py` | Standard iterative binary search, returns index of target. | O(log n) |
| `Recursive Code.py` | Same, recursive version. | O(log n) |

## Bounds & Insert Position

| File | Description | Time Complexity |
|---|---|---|
| `Lower Bound.py` | First index with value `>= x`. | O(log n) |
| `Upper Bound.py` | First index with value `> x`. | O(log n) |
| `Search Insert Position.py` | Index where `x` would be inserted to keep array sorted. | O(log n) |
| `Floor and Ceil in Sorted Array.py` | Largest element `<= x` and smallest element `>= x`. | O(log n) |

## Occurrence Counting

| File | Description | Time Complexity |
|---|---|---|
| `Last occurrence in a sorted array.py` | First and last index of `x` using lower/upper bound. | O(log n) |
| `Count Occurrences in Sorted Array.py` | Counts how many times `x` appears. | O(log n) |

## Rotated Sorted Arrays

| File | Description | Time Complexity |
|---|---|---|
| `Search Element in a Rotated Sorted Array(1).py` | Search `x` in a rotated array (no duplicates), returns index. | O(log n) |
| `Search Element in a Rotated Sorted Array(2).py` | Same, with duplicates allowed, returns True/False. | O(log n) average, O(n) worst case (all duplicates) |
| `Minimum in Rotated Sorted Array.py` | Finds the minimum value in a rotated sorted array. | O(log n) |
| `Find out how many times the array has been rotated.py` | Finds rotation count (index of the minimum element). | O(log n) |

## Peak Element

| File | Description | Time Complexity |
|---|---|---|
| `Peak element in Array.py` | Finds an index greater than both neighbors, in a 1D array. | O(log n) |
| `Find Peak Element (2D Matrix).py` | Finds a 2D peak via binary search over columns. | O(n log m) |

## 2D Matrix Search

| File | Description | Time Complexity |
|---|---|---|
| `Search in a Sorted 2d Matrix.py` | Matrix fully sorted row-major; searched as one flattened array. | O(log(n*m)) |
| `Search in a row and column wise sorted matrix.py` | Rows and columns independently sorted; staircase search from top-right. | O(n + m) |
| `Find the row with maxm number of 1s.py` | Row with the most 1s in a binary matrix, each row sorted. | O(n log m) |

## Merge-Based Search (Two Sorted Arrays / Matrices)

| File | Description | Time Complexity |
|---|---|---|
| `Median of 2 Sorted Arrays.py` | Median of two sorted arrays via partitioning. | O(log(min(n1,n2))) |
| `K-th Element of two Sorted Arrays.py` | K-th smallest element across two sorted arrays. | O(log(min(n1,n2))) |
| `Median of Row wise Sorted Matrix.py` | Median of a matrix with each row sorted, via value-range binary search. | O(n log m * log(maxVal - minVal)) |

## Binary Search on the Answer

| File | Description | Time Complexity |
|---|---|---|
| `Finding Sqrt of a number using Binary Search.py` | Integer square root. | O(log n) |
| `Nth Root of a Number using Binary Search.py` | Integer n-th root. | O(n log m) |
| `Find the Smallest Divisior Given a Threshold.py` | Smallest divisor keeping sum of `ceil(arr[i]/div)` within a threshold. | O(n log(max(arr))) |
| `Koko Eating Bananas.py` | Minimum eating rate to finish all piles within `h` hours. | O(n log(max(arr))) |
| `Capacity to ship packages within D days.py` | Minimum ship capacity to deliver within `d` days. | O(n log(sum(weights))) |
| `Allocate Minimum Number of Pages.py` | Minimize the max pages assigned to any student. | O(n log(sum(arr))) |
| `Painters Partition.py` | Same structure as page allocation, applied to painting boards. | O(n log(sum(arr))) |
| `Split Array Largest Sum.py` | Minimize the largest subarray sum over `k` splits. | O(n log(sum(arr))) |
| `Minimum days to make M bouquets.py` | Minimum day to make `m` bouquets of `k` adjacent bloomed flowers. | O(n log(max(arr))) |
| `Aggressive Cows.py` | Maximize the minimum distance between `k` cows in stalls. | O(n log n) for sort + O(n log(maxDist)) search |
| `Minimise Max dist between Gas Stations.py` | Minimize the largest gap after adding `k` gas stations (real-valued search). | O(n log(maxGap / precision)) |
| `Kth Missing Positive Number.py` | Finds the k-th missing positive integer. | O(log n) |