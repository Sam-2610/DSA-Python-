# Recursion Programs in DSA — Python

A collection of beginner-friendly Python programs to learn and practice **Recursion** — one of the most fundamental concepts in Data Structures and Algorithms (DSA).

---

## What is Recursion?

Recursion is a technique where a **function calls itself** to solve a smaller version of the same problem. Every recursive function has two parts:

- **Base Case** — the condition where the function stops calling itself
- **Recursive Case** — the part where the function calls itself with a smaller input

---

## Programs Included

| # | File | Description | Difficulty |
|---|------|-------------|------------|
| 1 | `Program_1.py` | Print "Hello World" N times *(has a bug)* | Beginner |
| 2 | `Program_2.py` | Print "Hello World" 5 times using recursion | Beginner |
| 3 | `Program_3.py` | Print numbers from 1 to N | Beginner |
| 4 | `Program_4.py` | Print numbers from N to 1 | Beginner |
| 5 | `Program_5.py` | Sum of first N numbers | Beginner |
| 6 | `Program_6.py` | Factorial of a number | Beginner |
| 7 | `Program_7.py` | Nth Fibonacci number | Intermediate |
| 8 | `Program_8.py` | Check if a string is a Palindrome | Intermediate |
| 9 | `Program_9.py` | Reverse an array by swapping | Intermediate |

---

## Program Details

### 1. Print "Hello World" N Times ⚠️
**File:** `Program_1.py`

Intended to print "Hello World" N times recursively, but has a **bug** — the function calls itself with no base case and no arguments, causing **infinite recursion** and a `RecursionError`.

**Buggy Code:**
```python
def pattern1():
    print("Hello World")
    pattern1()       # no base case — runs forever!
```

**Fixed Code:**
```python
def pattern1(i, n):
    if i > n:        # base case
        return
    print("Hello World")
    pattern1(i + 1, n)

pattern1(1, 5)       # prints 5 times
```

```
Output:
Hello World
Hello World
Hello World
Hello World
Hello World
```

---

### 2. Print "Hello World" 5 Times
**File:** `Program_2.py`

Correctly prints "Hello World" exactly 5 times using recursion with a counter.

- **Base case:** `i > n` → stop
- **Recursive case:** print and call with `i + 1`

```python
Input  : program2(1, 5)
Output :
Hello World
Hello World
Hello World
Hello World
Hello World
```

---

### 3. Print 1 to N
**File:** `Program_3.py`

Prints numbers from 1 to N in ascending order.

- **Base case:** `i > n` → stop
- **Recursive case:** print `i`, then call with `i + 1`
- **Key idea:** print **before** the recursive call → ascending order

```python
Input  : program3(1, 5)
Output : 1 2 3 4 5
```

---

### 4. Print N to 1
**File:** `Program_4.py`

Prints numbers from N down to 1 in descending order.

- **Base case:** `i < 1` → stop
- **Recursive case:** print `i`, then call with `i - 1`
- **Key idea:** print **before** the recursive call but decrement → descending order

```python
Input  : program4(5, 5)
Output : 5 4 3 2 1
```

---

### 5. Sum of First N Numbers
**File:** `Program_5.py`

Calculates the sum of first N natural numbers recursively.

- **Base case:** `i < 1` → print total and return
- **Recursive case:** call with `i - 1` and add `i` to total
- **Example:** 3 + 2 + 1 = 6

```python
Input  : program5(3, 0)
Output : 6
```

---

### 6. Factorial of a Number
**File:** `Program_6.py`

Computes the factorial of a number using recursion.

- **Base case:** `n == 0` → return 1 (0! = 1)
- **Recursive case:** `n * factorial(n - 1)`
- **Example:** 5! = 5 × 4 × 3 × 2 × 1 = 120

**Recursive call stack for n = 5:**
```
program6(5) = 5 × program6(4)
            = 5 × 4 × program6(3)
            = 5 × 4 × 3 × program6(2)
            = 5 × 4 × 3 × 2 × program6(1)
            = 5 × 4 × 3 × 2 × 1 × program6(0)
            = 5 × 4 × 3 × 2 × 1 × 1 = 120
```

```python
Input  : program6(5)
Output : 120
```

---

### 7. Nth Fibonacci Number
**File:** `Program_7.py`

Returns the Nth number in the Fibonacci sequence using recursion.

> ⚠️ Note: "Fibnaachi" in the comment is a typo — should be "Fibonacci"

- **Base case:** `n <= 1` → return n (F(0) = 0, F(1) = 1)
- **Recursive case:** `F(n) = F(n-1) + F(n-2)`
- **Sequence:** 0, 1, 1, 2, 3, 5, 8, 13, ...

```python
Input  : program7(4)
Output : 3           # 0, 1, 1, 2, 3 → index 4 = 3
```

---

### 8. Check Palindrome (String)
**File:** `Program_8.py`

Checks whether a string is a palindrome by recursively comparing characters from both ends.

- **Base case:** `i >= len(s) / 2` → return True (all chars matched)
- **Recursive case:** if `s[i] != s[len(s) - i - 1]` → return False, else recurse
- **Input is lowercased** so comparison is case-insensitive

```python
Input  : "racecar"
Output : True

Input  : "hello"
Output : False
```

---

### 9. Reverse an Array by Swapping
**File:** `Program_9.py`

Reverses an array in-place by recursively swapping elements from both ends towards the middle.

- **Base case:** `i >= n // 2` → stop (reached the middle)
- **Recursive case:** swap `arr[i]` with `arr[n - i - 1]`, then recurse with `i + 1`
- **In-place** — no extra array needed

```python
Input  : n = 5, arr = [1, 2, 3, 4, 5]
Output : 5 4 3 2 1
```

---

## Concepts Covered

- **Base case and recursive case** — the foundation of every recursive function
- **Call stack** — how recursive calls build up and unwind
- **Tail recursion** — making the recursive call the last operation
- **Accumulator pattern** — passing a running total as a parameter (Program 5)
- **Two-pointer via recursion** — comparing from both ends (Program 8, 9)
- **Tree recursion** — a function making two recursive calls (Program 7 — Fibonacci)

---

## How to Run

Make sure you have Python 3 installed.

```bash
python Program_1.py
python Program_2.py
python Program_3.py
python Program_4.py
python Program_5.py
python Program_6.py
python Program_7.py
python Program_8.py
python Program_9.py
```

---

## Tip for Beginners

When writing a recursive function, always ask yourself:
1. **What is the base case?** (When should it stop?)
2. **What is the recursive case?** (How does it get closer to the base case?)

If you miss the base case, you get infinite recursion — like in Program 1! 🚨

---

## Author

**Satyam Sagar**
📧 satyamsagar827@gmail.com
