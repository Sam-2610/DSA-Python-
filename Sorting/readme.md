# Sorting Algorithms in DSA — Python
 
A complete collection of fundamental **Sorting Algorithms** implemented in Python, ranging from basic O(n²) sorts to efficient O(n log n) divide-and-conquer algorithms.
 
---
 
## Files Included
 
| # | File | Algorithm | Time Complexity | Space | Strategy |
|---|------|-----------|----------------|-------|----------|
| 1 | `Swap_Two_Numbers.py` | Swap | O(1) | O(1) | Temp variable |
| 2 | `Bubble_Sort.py` | Bubble Sort | O(n²) | O(1) | Swap adjacent |
| 3 | `Selection_Sort.py` | Selection Sort | O(n²) | O(1) | Find minimum |
| 4 | `Insertion_Sort.py` | Insertion Sort | O(n²) | O(1) | Insert in place |
| 5 | `Merge_Sort.py` | Merge Sort | O(n log n) | O(n) | Divide & Conquer |
| 6 | `Quick_Sort.py` | Quick Sort | O(n log n) avg | O(log n) | Pivot & Partition |
 
---
 
## Program Details
 
---
 
### 1. Swap Two Numbers
**File:** `Swap_Two_Numbers.py`
 
The foundation of all sorting — swapping two values using a temporary variable.
 
```python
temp = a
a = b
b = temp
```
 
**How it works:**
 
| Step | `a` | `b` | `temp` |
|------|-----|-----|--------|
| Start | 5 | 9 | — |
| temp = a | 5 | 9 | 5 |
| a = b | 9 | 9 | 5 |
| b = temp | 9 | 5 | 5 |
 
```
Input  : a = 5, b = 9
Output : a = 9, b = 5
```
 
> In Python you can also swap without a temp variable: `a, b = b, a`
 
---
 
### 2. Bubble Sort
**File:** `Bubble_Sort.py`
 
Repeatedly compares adjacent elements and swaps them if out of order. The largest element **bubbles to the end** after each pass.
 
```python
for j in range(n - 1):
    for k in range(n - 1 - j):     # shrink from right each pass
        if arr[k] > arr[k + 1]:
            temp = arr[k + 1]
            arr[k + 1] = arr[k]
            arr[k] = temp
```
 
**Dry run with `arr = [5, 3, 8, 1]`:**
 
| Pass | Action | Array |
|------|--------|-------|
| j=0 | 8 bubbles to end | [3, 5, 1, **8**] |
| j=1 | 5 bubbles to position | [3, 1, **5**, 8] |
| j=2 | 3 bubbles to position | [1, **3**, 5, 8] |
 
```
Output : Sorted Array : [1, 3, 5, 8]
```
 
**Key detail:** `range(n - 1 - j)` skips already-sorted elements at the end, avoiding unnecessary comparisons.
 
---
 
### 3. Selection Sort
**File:** `Selection_Sort.py`
 
Finds the **minimum element** in the unsorted portion and places it at the front.
 
```python
for j in range(n - 1):
    mini = j
    for k in range(j + 1, n):      # scan unsorted portion
        if arr[k] < arr[mini]:
            mini = k
 
    temp = arr[mini]                # swap minimum to front
    arr[mini] = arr[j]
    arr[j] = temp
```
 
**Dry run with `arr = [5, 3, 8, 1]`:**
 
| Pass | Min found | Swap | Array |
|------|-----------|------|-------|
| j=0 | 1 at index 3 | arr[0] ↔ arr[3] | [**1**, 3, 8, 5] |
| j=1 | 3 at index 1 | no swap | [1, **3**, 8, 5] |
| j=2 | 5 at index 3 | arr[2] ↔ arr[3] | [1, 3, **5**, 8] |
 
```
Output : Sorted Array : [1, 3, 5, 8]
```
 
**Key detail:** Inner loop starts at `j + 1` to skip the already-sorted left portion.
 
---
 
### 4. Insertion Sort
**File:** `Insertion_Sort.py`
 
Picks each element and **inserts it into its correct position** among the already-sorted elements to its left.
 
```python
for j in range(1, n):              # start from index 1
    k = j
    while k > 0 and arr[k - 1] > arr[k]:
        temp = arr[k - 1]
        arr[k - 1] = arr[k]
        arr[k] = temp
        k = k - 1
```
 
**Dry run with `arr = [5, 3, 8, 1]`:**
 
| Pass | Pick | Action | Array |
|------|------|--------|-------|
| j=1 | 3 | 3 < 5, shift left | [**3, 5**, 8, 1] |
| j=2 | 8 | 8 > 5, stays | [3, 5, **8**, 1] |
| j=3 | 1 | 1 < 8, 5, 3 — shift all | [**1**, 3, 5, 8] |
 
```
Output : Sorted Array : [1, 3, 5, 8]
```
 
**Key detail:** Outer loop starts at `range(1, n)` — index 0 has nothing to its left to compare against.
 
---
 
### 5. Merge Sort
**File:** `Merge_Sort.py`
 
A **Divide and Conquer** algorithm. Keeps splitting the array in half until single elements remain, then merges them back in sorted order.
 
```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left  = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)
 
def merge(left, right):
    sorted_arr = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_arr.append(left[i]); i += 1
        else:
            sorted_arr.append(right[j]); j += 1
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])
    return sorted_arr
```
 
**Visualization:**
 
```
         [5, 3, 8, 1]
            /      \
        [5, 3]    [8, 1]
        /    \    /    \
       [5]  [3] [8]  [1]
        \    /    \    /
        [3, 5]   [1, 8]
            \      /
         [1, 3, 5, 8]
```
 
**Dry run — merge `[3, 5]` and `[1, 8]`:**
 
| `i` | `j` | left[i] | right[j] | pick | result |
|-----|-----|---------|----------|------|--------|
| 0 | 0 | 3 | 1 | 1 | [1] |
| 0 | 1 | 3 | 8 | 3 | [1, 3] |
| 1 | 1 | 5 | 8 | 5 | [1, 3, 5] |
| — | 1 | done | 8 | 8 | [1, 3, 5, 8] |
 
```
Output : Sorted Array : [1, 3, 5, 8]
```
 
**Key detail:** `sorted_arr.extend(left[i:])` dumps any remaining elements after one pointer finishes — they're already sorted so no comparison needed.
 
---
 
### 6. Quick Sort
**File:** `Quick_Sort.py`
 
A **Divide and Conquer** algorithm. Picks a **pivot**, places it in its correct position, and recursively sorts everything to its left and right.
 
```python
def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)
 
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
```
 
**Visualization:**
 
```
[5, 3, 8, 1]   pivot=1
      ↓
[1, | 3, 8, 5]   pivot=5
         ↓
[1, 3, | 5, | 8]
↓
[1, 3, 5, 8]
```
 
**Dry run — partition `[5, 3, 8, 1]`, pivot=1:**
 
| `j` | arr[j] | ≤ pivot? | action | array |
|-----|--------|----------|--------|-------|
| 0 | 5 | no | skip | [5, 3, 8, 1] |
| 1 | 3 | no | skip | [5, 3, 8, 1] |
| 2 | 8 | no | skip | [5, 3, 8, 1] |
 
Place pivot: swap arr[0] ↔ arr[3] → `[1, 3, 8, 5]`, pivot_index = 0 ✓
 
```
Output : Sorted Array : [1, 3, 5, 8]
```
 
**Key detail:** `i` acts as the boundary — everything at or before `i` is ≤ pivot. After the loop, pivot is placed at `i + 1`.
 
---
 
## Bugs Fixed During Practice
 
| File | Bug | Fix |
|------|-----|-----|
| `Bubble_Sort.py` | Inner loop `range(j)` shrinking from wrong side | `range(n - 1 - j)` |
| `Selection_Sort.py` | Comparing `arr[j]` instead of `arr[k]` | `arr[k] < arr[mini]` |
| `Insertion_Sort.py` | Outer loop `range(n-1)` starting at 0 | `range(1, n)` |
 
---
 
## Full Comparison
 
| Algorithm | Best | Average | Worst | Space | Stable | Strategy |
|-----------|------|---------|-------|-------|--------|----------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) | Yes | Swap adjacent |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) | No | Find minimum |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) | Yes | Insert in place |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes | Divide & Conquer |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) | No | Pivot & Partition |
 
> **Stable** means equal elements maintain their original relative order after sorting.
 
---
 
## When to Use Which?
 
| Situation | Best Choice |
|-----------|-------------|
| Small array (< 20 elements) | Insertion Sort |
| Already nearly sorted | Insertion Sort |
| Guaranteed O(n log n) needed | Merge Sort |
| Average case speed on arrays | Quick Sort |
| Memory is limited | Quick Sort |
| Need stable sort | Merge Sort |
 
---
 
## How to Run
 
```bash
python Swap_Two_Numbers.py
python Bubble_Sort.py
python Selection_Sort.py
python Insertion_Sort.py
python Merge_Sort.py
python Quick_Sort.py
```
 
---
 
## Author
 
**Satyam Sagar**
📧 satyamsagar827@gmail.com