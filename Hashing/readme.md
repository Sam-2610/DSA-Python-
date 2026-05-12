# Hashing in DSA — Python

A collection of Python programs covering **Hashing** — one of the most powerful and frequently used techniques in Data Structures and Algorithms (DSA) for fast lookups and frequency counting.

---

## What is Hashing?

Hashing is a technique to **store and retrieve data in O(1) time** (constant time). Instead of searching through an array one by one, you map each value to a specific index or key, so lookups are instant.

- **Array-based hashing** — use the value itself as an index (works for small, bounded values)
- **Dictionary-based hashing** — use a key-value pair (works for any values)

---

## Files Included

| # | File | Concept | Time Complexity |
|---|------|---------|-----------------|
| 1 | `Count_Zeros.py` | Count zeros in an array | O(n) |
| 2 | `Hashing.py` | Frequency count using a dictionary | O(n) precompute, O(1) query |
| 3 | `Character_Hashing.py` | Character frequency using ASCII array | O(n) precompute, O(1) query |

---

## Program Details

---

### 1. Count Zeros
**File:** `Count_Zeros.py`

Counts how many zeros are present in a user-provided array.

```python
def count_zeros():
    arr = []
    count = 0
    n = int(input("Enter the Number : "))
    for i in range(n):
        x = int(input(f"Enter the Element {i + 1} : "))
        arr.append(x)
    
    for num in arr:
        if num == 0:
            count = count + 1

    if count:
        print(f"The Count of Zeros is : {count}")
    else:
        print("No Zeros")

count_zeros()
```

**Line by line:**

| Code | Description |
|------|-------------|
| `for i in range(n)` | Takes `n` elements from the user one by one |
| `arr.append(x)` | Adds each element to the list |
| `if num == 0: count += 1` | Increments counter for every zero found |
| `if count:` | Evaluates to `False` if count is 0 (Pythonic way to check) |

**Dry run with `arr = [1, 0, 3, 0, 0]`:**

| `num` | is zero? | `count` |
|-------|----------|---------|
| 1     | no       | 0       |
| 0     | yes      | 1       |
| 3     | no       | 1       |
| 0     | yes      | 2       |
| 0     | yes      | 3       |

```
Output: The Count of Zeros is : 3
```

---

### 2. Hashing (Frequency Count)
**File:** `Hashing.py`

Counts the frequency of each number in an array using a **dictionary (hash map)**, then answers multiple queries in O(1) time.

```python
def hashing():
    n = int(input("Enter the Value of n : "))
    arr = []
    for i in range(n):
        x = int(input(f"Enter the Element {i + 1} : "))
        arr.append(x)

    hash_dict: dict[int, int] = {}

    for num in arr:
        if num in hash_dict:
            hash_dict[num] += 1
        else:
            hash_dict[num] = 1

    q = int(input("Enter the Queries : "))
    for _ in range(q):
        number = int(input("Enter the Number : "))
        print(hash_dict.get(number, 0))

hashing()
```

**Line by line:**

| Code | Description |
|------|-------------|
| `hash_dict: dict[int, int] = {}` | Creates an empty dictionary with type hint — keys and values are both integers |
| `if num in hash_dict` | Checks if the number has been seen before |
| `hash_dict[num] += 1` | Increments count if already exists |
| `hash_dict[num] = 1` | Initializes count to 1 for a new number |
| `hash_dict.get(number, 0)` | Returns the frequency, or 0 if the number was never in the array |

**Dry run with `arr = [1, 2, 1, 3, 2, 1]`:**

| Step | `num` | `hash_dict` |
|------|-------|-------------|
| 1    | 1     | `{1: 1}` |
| 2    | 2     | `{1: 1, 2: 1}` |
| 3    | 1     | `{1: 2, 2: 1}` |
| 4    | 3     | `{1: 2, 2: 1, 3: 1}` |
| 5    | 2     | `{1: 2, 2: 2, 3: 1}` |
| 6    | 1     | `{1: 3, 2: 2, 3: 1}` |

```
Query: 1 → Output: 3
Query: 2 → Output: 2
Query: 5 → Output: 0   (not in array)
```

**Why is querying O(1)?**
Because dictionary lookups in Python use hashing internally — no matter how large the dictionary, finding a key takes constant time.

---

### 3. Character Hashing
**File:** `Character_Hashing.py`

Counts the frequency of each character in a string using an **ASCII-indexed array**, then answers multiple character queries in O(1) time.

```python
s = input("Enter the string: ")

hash_arr = [0] * 256        # Array of size 256 (all ASCII characters)

for ch in s:
    hash_arr[ord(ch)] += 1  # ord(ch) gives the ASCII value of the character

q = int(input("Enter number of queries: "))
for _ in range(q):
    c = input("Enter character: ")
    print(hash_arr[ord(c)])
```

**Line by line:**

| Code | Description |
|------|-------------|
| `[0] * 256` | Creates an array of 256 zeros — one slot for each ASCII character |
| `ord(ch)` | Converts a character to its ASCII integer value (e.g. `'a'` → 97) |
| `hash_arr[ord(ch)] += 1` | Uses ASCII value as index to increment that character's count |
| `hash_arr[ord(c)]` | Instantly retrieves count for a queried character |

**ASCII reference (common characters):**

| Character | ASCII Value |
|-----------|-------------|
| `'A'` | 65 |
| `'Z'` | 90 |
| `'a'` | 97 |
| `'z'` | 122 |
| `'0'` | 48 |
| `'9'` | 57 |

**Dry run with `s = "hello"`:**

| `ch` | `ord(ch)` | `hash_arr[index]` |
|------|-----------|-------------------|
| `h`  | 104       | hash_arr[104] = 1 |
| `e`  | 101       | hash_arr[101] = 1 |
| `l`  | 108       | hash_arr[108] = 1 |
| `l`  | 108       | hash_arr[108] = 2 |
| `o`  | 111       | hash_arr[111] = 1 |

```
Query: 'l' → Output: 2
Query: 'h' → Output: 1
Query: 'z' → Output: 0
```

---

## Hashing vs Linear Search

| Operation | Linear Search | Hashing |
|-----------|--------------|---------|
| Build | O(n) | O(n) |
| Query | O(n) | **O(1)** |
| Best for | Rare lookups | Multiple queries |

Hashing shines when you need to answer **many queries** on the same data — build once, query instantly.

---

## Key Concepts Summary

| Concept | Used In | How |
|---------|---------|-----|
| Array as hash map | `Character_Hashing.py` | ASCII value as index |
| Dictionary as hash map | `Hashing.py` | Number as key |
| O(1) query | Both hashing files | Precompute, then instant lookup |
| `ord(ch)` | `Character_Hashing.py` | Convert char → ASCII integer |
| `dict.get(key, default)` | `Hashing.py` | Safe lookup with fallback value |

---

## How to Run

```bash
python Count_Zeros.py
python Hashing.py
python Character_Hashing.py
```

Each program will prompt you to enter input via the terminal.

---

## Author

**Satyam Sagar**
📧 satyamsagar827@gmail.com